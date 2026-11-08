"""Reference EnergyPlus 22.2 IDF generator.

A task is a parameter dict (see params.py). `build_idf(p, choices)` writes the
model. `choices` holds the modelling decisions the task text leaves open
(timestep, wall layering, window placement, interior partitions, ...). The
nominal reference uses DEFAULT_CHOICES; the equivalence ensemble samples the
alternatives to measure how much valid modellers could differ.
"""
from __future__ import annotations

DEFAULT_CHOICES = {
    "timestep": 4,
    "wall_variant": 0,              # 0: standard layering; 1: alternative layering with the same U-factor
    "roof_variant": 0,
    "sill": 0.9,                     # window sill height [m]
    "window_split": 1,               # number of equal windows per facade segment
    "interior": "interzone",        # interzone | adiabatic (zone-to-zone partitions and floors)
    "solar": "FullExterior",        # FullExterior | FullInteriorAndExterior
    "light_frac": (0.0, 0.0),        # (radiant, visible) fractions of lighting heat
    "equip_frac": (0.0, 0.0),        # (latent, radiant) fractions of equipment heat
    "start_vertex": 0,               # which footprint corner starts the vertex lists
    "ins_nomass": False,             # v1.0.1: insulation as Material:NoMass (same R)
    "win_layout": "default",         # v1.0.1: "wide" = one window, 90% of facade width, vertically centred
}

# Film resistances used by EnergyPlus' EnvelopeSummary "U-Factor with Film" (m2K/W),
# calibrated against EnergyPlus 22.2 output (see test_films in build script).
R_FILM_WALL = 0.0299387 + 0.1197548
R_FILM_ROOF = 0.0299387 + 0.1067109

MAT = {  # name: (thickness m, conductivity W/mK, density kg/m3, specific heat J/kgK)
    "Stucco25": (0.0253, 0.6918, 1858.0, 837.0),
    "Gypsum13": (0.0127, 0.16, 784.9, 830.0),
    "Concrete200": (0.2032, 1.311, 2240.0, 836.8),
    "Membrane10": (0.0095, 0.16, 1121.3, 1460.0),
    "MetalDeck": (0.0015, 45.006, 7680.0, 418.4),
    "Concrete100": (0.1016, 1.311, 2240.0, 836.8),
    "Carpet": (0.0127, 0.06, 288.0, 1380.0),
    "Plywood16": (0.0159, 0.12, 544.0, 1210.0),
    "MetalSiding": (0.0015, 44.96, 7688.9, 410.0),
}
K_INS = 0.049  # insulation conductivity W/mK


def _r(mat):
    t, k, _, _ = MAT[mat]
    return t / k


def wall_layers(u_target, wtype, variant=0):
    """Layers (outside -> inside) as (outer list, insulation thickness, inner list)."""
    if wtype == "light":
        outer, inner = (["Stucco25"], ["Gypsum13"]) if variant == 0 else (["MetalSiding", "Plywood16"], ["Gypsum13"])
        ins_out = True
    else:  # mass: 200 mm concrete, insulation inside (variant 0) or outside (variant 1, EIFS-like)
        outer, inner = (["Concrete200"], ["Gypsum13"]) if variant == 0 else (["Stucco25"], ["Concrete200", "Gypsum13"])
    r_ins = 1.0 / u_target - R_FILM_WALL - sum(_r(m) for m in outer + inner)
    if r_ins <= 0.01:
        raise ValueError("wall U too high for layer set")
    return outer, r_ins * K_INS, inner


def roof_layers(u_target, rtype, variant=0):
    if rtype == "light":
        outer, inner = (["Membrane10"], ["MetalDeck"]) if variant == 0 else (["Membrane10", "Plywood16"], ["MetalDeck"])
    else:  # mass: 100 mm concrete deck, insulation above (variant 0) or below (variant 1)
        outer, inner = (["Membrane10"], ["Concrete100"]) if variant == 0 else (["Membrane10", "Concrete100"], ["Gypsum13"])
    r_ins = 1.0 / u_target - R_FILM_ROOF - sum(_r(m) for m in outer + inner)
    if r_ins <= 0.01:
        raise ValueError("roof U too high for layer set")
    return outer, r_ins * K_INS, inner


def fmt(x):
    return f"{x:.4f}".rstrip("0").rstrip(".") if isinstance(x, float) else str(x)


def obj(kind, *fields):
    out = [f"{kind},"]
    for i, f in enumerate(fields):
        end = ";" if i == len(fields) - 1 else ","
        out.append(f"    {fmt(f) if isinstance(f, float) else f}{end}")
    return "\n".join(out) + "\n"


# ---------------------------------------------------------------- geometry
def zone_polygons(p):
    """Footprint polygons (counter-clockwise from above) for one storey."""
    L, W = p["length"], p["width"]
    if p["zoning"] == "single":
        return {"Zone": [(0, 0), (L, 0), (L, W), (0, W)]}
    d = p["perim_depth"]
    return {
        "South": [(0, 0), (L, 0), (L - d, d), (d, d)],
        "East": [(L, 0), (L, W), (L - d, W - d), (L - d, d)],
        "North": [(L, W), (0, W), (d, W - d), (L - d, W - d)],
        "West": [(0, W), (0, 0), (d, d), (d, W - d)],
        "Core": [(d, d), (L - d, d), (L - d, W - d), (d, W - d)],
    }


def facade_of(p1, p2, L, W, eps=1e-6):
    (x1, y1), (x2, y2) = p1, p2
    if abs(y1) < eps and abs(y2) < eps:
        return "S"
    if abs(x1 - L) < eps and abs(x2 - L) < eps:
        return "E"
    if abs(y1 - W) < eps and abs(y2 - W) < eps:
        return "N"
    if abs(x1) < eps and abs(x2) < eps:
        return "W"
    return None


def rot(poly, k):
    k %= len(poly)
    return poly[k:] + poly[:k]


def v3(pts):
    return [f"{fmt(float(x))},{fmt(float(y))},{fmt(float(z))}" for x, y, z in pts]


def surface(name, stype, cons, zone, bc, bc_obj, sun, wind, verts):
    fields = [name, stype, cons, zone, "", bc, bc_obj, sun, wind, "autocalculate", str(len(verts))]
    fields += v3(verts)
    return obj("BuildingSurface:Detailed", *fields)


def window(name, host, verts):
    fields = [name, "Window", "Win_Cons", host, "", "autocalculate", "", "1"]
    fields += [str(len(verts))] + v3(verts)
    return obj("FenestrationSurface:Detailed", *fields)


# ---------------------------------------------------------------- schedules
SCHED = {  # occupied periods: list of (day spec, start hour, end hour)
    "office": [("Weekdays", 8, 18)],
    "retail": [("AllDays", 9, 21)],
    "school": [("Weekdays", 7, 16)],
    "clinic": [("Weekdays", 7, 19), ("Saturday", 8, 13)],
}


def compact(name, limits, sched_type, occ, unocc):
    periods = SCHED[sched_type]
    f = [name, limits, "Through: 12/31"]
    used = []
    for days, a, b in periods:
        dd = "Weekdays SummerDesignDay WinterDesignDay" if days == "Weekdays" else days
        if days == "AllDays":
            dd = "AllDays"
        f += [f"For: {dd}", f"Until: {a:02d}:00", fmt(float(unocc)), f"Until: {b:02d}:00", fmt(float(occ)),
              "Until: 24:00", fmt(float(unocc))]
        used.append(days)
    if "AllDays" not in used:
        f += ["For: AllOtherDays", "Until: 24:00", fmt(float(unocc))]
    return obj("Schedule:Compact", *f)


# ---------------------------------------------------------------- HVAC
def hvac_objects(p, zones):
    out = [obj("HVACTemplate:Thermostat", "Tstat", "HTGSETP_SCH", "", "CLGSETP_SCH", "")]
    h = p["hvac"]
    for z in zones:
        if h == "ideal":
            out.append(obj("HVACTemplate:Zone:IdealLoadsAirSystem", z, "Tstat"))
        elif h == "ptac":
            out.append(obj("HVACTemplate:Zone:PTAC", z, "Tstat", "autosize", "autosize", "", "", "",
                           "Flow/Person", fmt(p["oa_per_person"]), "", "", "", "", "DrawThrough",
                           fmt(p["fan_eff"]), fmt(p["fan_dp"]), "0.9", "SingleSpeedDX", "", "autosize",
                           "autosize", fmt(p["cool_cop"]), "Electric", "", "autosize", "1.0"))
        elif h == "pthp":
            out.append(obj("HVACTemplate:Zone:PTHP", z, "Tstat", "autosize", "autosize", "", "", "",
                           "Flow/Person", fmt(p["oa_per_person"]), "", "", "", "", "DrawThrough",
                           fmt(p["fan_eff"]), fmt(p["fan_dp"]), "0.9", "SingleSpeedDX", "", "autosize",
                           "autosize", fmt(p["cool_cop"]), "SingleSpeedDXHeatPump", "", "autosize",
                           fmt(p["heat_cop"]), "-8", "5", "", "", "", "Electric", "", "autosize", "21"))
        elif h == "psz_gas":
            out.append(obj("HVACTemplate:Zone:Unitary", z, f"PSZ_{z}", "Tstat", "autosize", "", "",
                           "Flow/Person", fmt(p["oa_per_person"])))
            out.append(obj("HVACTemplate:System:Unitary", f"PSZ_{z}", "", z, "autosize", "",
                           fmt(p["fan_eff"]), fmt(p["fan_dp"]), "0.9", "1.0", "SingleSpeedDX", "", "",
                           "autosize", "autosize", fmt(p["cool_cop"]), "Gas", "", "", "autosize",
                           fmt(p["burner_eff"]), "", "autosize", "autosize", "", "NoEconomizer"))
        else:
            raise ValueError(h)
    return out


# ---------------------------------------------------------------- main
def build_idf(p, choices=None):
    c = dict(DEFAULT_CHOICES)
    c.update(choices or {})
    c.update(p.get("fixed") or {})  # v1.1: choices the brief pins down cannot vary
    L, W, H, nF = p["length"], p["width"], p["floor_height"], p["n_floors"]
    o = []
    o.append(obj("Version", "22.2"))
    o.append(obj("Building", p["name"], fmt(float(p["north_axis"])), "Suburbs", "0.04", "0.4", c["solar"], "25", "6"))
    o.append(obj("Timestep", str(c["timestep"])))
    o.append(obj("GlobalGeometryRules", "UpperLeftCorner", "Counterclockwise", "Relative"))
    o.append(obj("ScheduleTypeLimits", "Fraction", "0", "1", "Continuous"))
    o.append(obj("ScheduleTypeLimits", "Temperature", "-60", "200", "Continuous"))
    o.append(obj("ScheduleTypeLimits", "Any", "", "", "Continuous"))

    # materials and constructions
    used = set()
    wo, w_ins, wi = wall_layers(p["wall_u"], p["wall_type"], c["wall_variant"])
    ro, r_ins, ri = roof_layers(p["roof_u"], p["roof_type"], c["roof_variant"])
    for m in wo + wi + ro + ri + ["Concrete100", "Carpet", "Gypsum13"]:
        if m not in used:
            t, k, d, cp = MAT[m]
            o.append(obj("Material", m, "MediumRough", fmt(t), fmt(k), fmt(d), fmt(cp), "0.9", "0.7", "0.7"))
            used.add(m)
    if c.get("ins_nomass"):
        o.append(obj("Material:NoMass", "WallIns", "MediumRough", f"{w_ins / K_INS:.5f}", "0.9", "0.7", "0.7"))
        o.append(obj("Material:NoMass", "RoofIns", "MediumRough", f"{r_ins / K_INS:.5f}", "0.9", "0.7", "0.7"))
    else:
        o.append(obj("Material", "WallIns", "MediumRough", f"{w_ins:.5f}", fmt(K_INS), "265", "836.8", "0.9", "0.7", "0.7"))
        o.append(obj("Material", "RoofIns", "MediumRough", f"{r_ins:.5f}", fmt(K_INS), "265", "836.8", "0.9", "0.7", "0.7"))
    o.append(obj("Construction", "ExtWall_Cons", *wo, "WallIns", *wi))
    o.append(obj("Construction", "Roof_Cons", *ro, "RoofIns", *ri))
    o.append(obj("Construction", "Slab_Cons", "Concrete100", "Carpet"))
    # errata 2026-11-07: layer order is outside -> inside. A floor faces down, so concrete is outside and carpet
    # inside; the ceiling below is its reverse. (v1.0-v1.0.2 / v1.1-v1.1.1 had the two swapped.)
    if p.get("legacy_floor"):  # edit tasks keep the layer order of the base model that systems received
        o.append(obj("Construction", "IntFloor_Cons", "Carpet", "Concrete100"))
        o.append(obj("Construction", "IntCeil_Cons", "Concrete100", "Carpet"))
    else:
        o.append(obj("Construction", "IntFloor_Cons", "Concrete100", "Carpet"))
        o.append(obj("Construction", "IntCeil_Cons", "Carpet", "Concrete100"))
    o.append(obj("Construction", "Partition_Cons", "Gypsum13", "Gypsum13"))
    o.append(obj("WindowMaterial:SimpleGlazingSystem", "Glazing", fmt(p["win_u"]), fmt(p["win_shgc"]), fmt(p["win_vt"])))
    o.append(obj("Construction", "Win_Cons", "Glazing"))

    # geometry
    polys = zone_polygons(p)
    zone_names = []
    surf = []
    edge_owner = {}
    for f in range(nF):
        for zn, poly in polys.items():
            edge_owner.setdefault(f, {})
            for i in range(4):
                a, b = poly[i], poly[(i + 1) % 4]
                edge_owner[f][(a, b)] = zn
    for f in range(nF):
        z0, z1 = f * H, (f + 1) * H
        for zn, poly0 in polys.items():
            zname = f"F{f + 1}_{zn}" if nF > 1 else zn
            zone_names.append(zname)
            o.append(obj("Zone", zname, "0", "0", "0", "0", "1", "1", "autocalculate", "autocalculate"))
            poly = rot(poly0, c["start_vertex"])
            for i in range(4):
                a, b = poly[i], poly[(i + 1) % 4]
                fac = facade_of(a, b, L, W)
                sname = f"{zname}_Wall{i}"
                verts = [(a[0], a[1], z1), (a[0], a[1], z0), (b[0], b[1], z0), (b[0], b[1], z1)]
                if fac:
                    surf.append(surface(sname, "Wall", "ExtWall_Cons", zname, "Outdoors", "", "SunExposed", "WindExposed", verts))
                    wwr = p["wwr"][fac]
                    if wwr > 0:
                        seg = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5
                        area = wwr * seg * H
                        n = c["window_split"]
                        hgt = min(H - c["sill"] - 0.3, 2.4)
                        wid = area / hgt / n
                        sill = c["sill"]
                        if c.get("win_layout") == "wide":
                            n, wid = 1, 0.9 * seg
                            hgt = area / wid
                            sill = (H - hgt) / 2
                        gap = (seg - n * wid) / (n + 1)
                        if gap < 0.05:
                            raise ValueError("window does not fit")
                        ux, uy = (b[0] - a[0]) / seg, (b[1] - a[1]) / seg
                        for k in range(n):
                            s0 = gap + k * (wid + gap)
                            s1 = s0 + wid
                            P0 = (a[0] + ux * s0, a[1] + uy * s0)
                            P1 = (a[0] + ux * s1, a[1] + uy * s1)
                            zs, zt = z0 + sill, z0 + sill + hgt
                            surf.append(window(f"{sname}_Win{k}", sname,
                                               [(P0[0], P0[1], zt), (P0[0], P0[1], zs), (P1[0], P1[1], zs), (P1[0], P1[1], zt)]))
                else:
                    other = edge_owner[f][(b, a)]
                    oname = f"F{f + 1}_{other}" if nF > 1 else other
                    # find the index of edge (b,a) in the other zone's rotated polygon
                    op = rot(polys[other], c["start_vertex"])
                    j = [k for k in range(4) if op[k] == b and op[(k + 1) % 4] == a][0]
                    if c["interior"] == "interzone":
                        surf.append(surface(sname, "Wall", "Partition_Cons", zname, "Surface", f"{oname}_Wall{j}", "NoSun", "NoWind", verts))
                    else:
                        surf.append(surface(sname, "Wall", "Partition_Cons", zname, "Adiabatic", "", "NoSun", "NoWind", verts))
            top = [(x, y, z1) for x, y in poly]
            bot = [(x, y, z0) for x, y in reversed(poly)]
            if f == 0:
                surf.append(surface(f"{zname}_Floor", "Floor", "Slab_Cons", zname, "Ground", "", "NoSun", "NoWind", bot))
            else:
                below = f"F{f}_{zn}"
                if c["interior"] == "interzone":
                    surf.append(surface(f"{zname}_Floor", "Floor", "IntFloor_Cons", zname, "Surface", f"{below}_Ceiling", "NoSun", "NoWind", bot))
                else:
                    surf.append(surface(f"{zname}_Floor", "Floor", "IntFloor_Cons", zname, "Adiabatic", "", "NoSun", "NoWind", bot))
            if f == nF - 1:
                surf.append(surface(f"{zname}_Roof", "Roof", "Roof_Cons", zname, "Outdoors", "", "SunExposed", "WindExposed", top))
            else:
                above = f"F{f + 2}_{zn}"
                if c["interior"] == "interzone":
                    surf.append(surface(f"{zname}_Ceiling", "Ceiling", "IntCeil_Cons", zname, "Surface", f"{above}_Floor", "NoSun", "NoWind", top))
                else:
                    surf.append(surface(f"{zname}_Ceiling", "Ceiling", "IntCeil_Cons", zname, "Adiabatic", "", "NoSun", "NoWind", top))
    o += surf

    # schedules
    st = p["schedule"]
    o.append(obj("Schedule:Compact", "ALWAYS_ON", "Fraction", "Through: 12/31", "For: AllDays", "Until: 24:00", "1"))
    o.append(compact("OCC_SCH", "Fraction", st, p["occ_frac"][0], p["occ_frac"][1]))
    o.append(compact("LTG_SCH", "Fraction", st, p["ltg_frac"][0], p["ltg_frac"][1]))
    o.append(compact("EQP_SCH", "Fraction", st, p["eqp_frac"][0], p["eqp_frac"][1]))
    o.append(compact("HTGSETP_SCH", "Temperature", st, p["heat_sp"][0], p["heat_sp"][1]))
    o.append(compact("CLGSETP_SCH", "Temperature", st, p["cool_sp"][0], p["cool_sp"][1]))
    o.append(obj("Schedule:Compact", "ACTIVITY_SCH", "Any", "Through: 12/31", "For: AllDays", "Until: 24:00", fmt(float(p["activity"]))))

    # internal loads per zone
    for z in zone_names:
        o.append(obj("People", f"{z}_People", z, "OCC_SCH", "Area/Person", "", "", fmt(float(p["area_per_person"])), "0.3", "autocalculate", "ACTIVITY_SCH"))
        o.append(obj("Lights", f"{z}_Lights", z, "LTG_SCH", "Watts/Area", "", fmt(float(p["lpd"])), "", "0", fmt(c["light_frac"][0]), fmt(c["light_frac"][1]), "1"))
        o.append(obj("ElectricEquipment", f"{z}_Equip", z, "EQP_SCH", "Watts/Area", "", fmt(float(p["epd"])), "", fmt(c["equip_frac"][0]), fmt(c["equip_frac"][1]), "0"))
        o.append(obj("ZoneInfiltration:DesignFlowRate", f"{z}_Infil", z, "ALWAYS_ON", "AirChanges/Hour", "", "", "", fmt(float(p["ach"])), "1", "0", "0", "0"))
    o += hvac_objects(p, zone_names)
    return "\n".join(o)
