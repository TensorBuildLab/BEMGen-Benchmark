"""Seeded sampling of task parameters for the four task tiers.

T1  single-zone box, ideal loads
T2  multi-zone (perimeter-core and/or multi-storey), ideal loads
T3  T1/T2 geometry with a packaged HVAC system (PTAC, PTHP, PSZ gas furnace)
TE  edit an existing model (base IDF given): 1-3 parameter changes
"""
from __future__ import annotations

import copy
import random

CITIES = ["San Francisco", "Golden", "Tampa", "Chicago", "Washington Dulles"]
USES = {  # schedule, area per person [m2/person], LPD, EPD ranges
    "office": ("office", (15, 25), (6.0, 11.0), (6.0, 12.0)),
    "retail": ("retail", (8, 16), (9.0, 15.0), (2.0, 6.0)),
    "school": ("school", (4, 8), (7.0, 11.0), (4.0, 9.0)),
    "clinic": ("clinic", (10, 18), (8.0, 12.0), (8.0, 14.0)),
}


def r2(x, step):
    return round(round(x / step) * step, 4)


def base_params(rng, tier):
    use = rng.choice(list(USES))
    sched, app, lpd, epd = USES[use]
    H = r2(rng.uniform(3.0, 4.2), 0.1)
    p = {
        "use": use,
        "schedule": sched,
        "city": rng.choice(CITIES),
        "north_axis": rng.choice([0, 0, 0, 15, -20, 30]),
        "length": r2(rng.uniform(15, 50), 0.5),
        "width": r2(rng.uniform(12, 30), 0.5),
        "floor_height": H,
        "n_floors": 1,
        "zoning": "single",
        "perim_depth": None,
        "wall_type": rng.choice(["light", "mass"]),
        "roof_type": rng.choice(["light", "mass"]),
        "wall_u": r2(rng.uniform(0.25, 0.9), 0.01),
        "roof_u": r2(rng.uniform(0.15, 0.5), 0.01),
        "win_u": r2(rng.uniform(1.4, 3.5), 0.1),
        "win_shgc": r2(rng.uniform(0.22, 0.6), 0.01),
        "win_vt": None,
        "lpd": r2(rng.uniform(*lpd), 0.1),
        "epd": r2(rng.uniform(*epd), 0.1),
        "area_per_person": r2(rng.uniform(*app), 0.5),
        "activity": rng.choice([110, 120, 130]),
        "ach": r2(rng.uniform(0.1, 0.6), 0.05),
        "occ_frac": (1.0, 0.0),
        "ltg_frac": (r2(rng.uniform(0.8, 1.0), 0.05), r2(rng.uniform(0.05, 0.2), 0.05)),
        "eqp_frac": (r2(rng.uniform(0.8, 1.0), 0.05), r2(rng.uniform(0.2, 0.5), 0.05)),
        "heat_sp": (r2(rng.uniform(20, 22), 0.5), r2(rng.uniform(13, 17), 0.5)),
        "cool_sp": (r2(rng.uniform(23, 25), 0.5), r2(rng.uniform(27, 30), 0.5)),
        "hvac": "ideal",
    }
    p["win_vt"] = r2(min(0.75, p["win_shgc"] * rng.uniform(1.1, 1.6)), 0.01)
    if p["length"] < p["width"]:
        p["length"], p["width"] = p["width"], p["length"]
    cap = 0.45 if H >= 3.3 else 0.4
    p["wwr"] = {f: r2(rng.uniform(0.1, cap), 0.05) for f in "NESW"}
    if rng.random() < 0.25:
        p["wwr"][rng.choice("NEW")] = 0.0
    if tier in ("T2", "T3", "TE"):
        layout = rng.choice(["pc", "pc", "stack"]) if tier == "T2" else rng.choice(["single", "pc", "stack"])
        if layout == "pc":
            p["zoning"] = "perimeter_core"
            p["perim_depth"] = r2(rng.uniform(3.0, 5.0), 0.5)
            p["n_floors"] = rng.choice([1, 2])
        elif layout == "stack":
            p["n_floors"] = rng.choice([2, 3])
    if tier == "T3":
        p["hvac"] = rng.choice(["ptac", "pthp", "psz_gas"])
        p["cool_cop"] = r2(rng.uniform(2.8, 3.6), 0.1)
        p["oa_per_person"] = r2(rng.uniform(0.0025, 0.01), 0.0005)
        if p["hvac"] == "psz_gas":
            p["fan_eff"], p["fan_dp"] = r2(rng.uniform(0.5, 0.7), 0.05), r2(rng.uniform(400, 700), 50)
            p["burner_eff"] = r2(rng.uniform(0.78, 0.92), 0.01)
        else:
            p["fan_eff"], p["fan_dp"] = r2(rng.uniform(0.5, 0.7), 0.05), r2(rng.uniform(75, 300), 25)
        if p["hvac"] == "pthp":
            p["heat_cop"] = r2(rng.uniform(2.8, 3.4), 0.1)
    return p


EDIT_KINDS = ["wwr", "wall_u", "win", "lpd", "setpoint", "schedule_unocc", "ach", "roof_u"]


def make_edit(rng, p):
    """Return (new params, list of edit descriptors)."""
    q = copy.deepcopy(p)
    kinds = rng.sample(EDIT_KINDS, rng.choice([1, 2, 3]))
    edits = []
    for k in kinds:
        if k == "wwr":
            f = rng.choice([x for x in "NESW" if q["wwr"][x] > 0])
            new = r2(min(0.45, max(0.1, q["wwr"][f] + rng.choice([-0.15, -0.1, 0.1, 0.15]))), 0.05)
            edits.append(("wwr", f, q["wwr"][f], new)); q["wwr"][f] = new
        elif k == "wall_u":
            new = r2(q["wall_u"] * rng.choice([0.5, 0.6, 0.7]), 0.01)
            edits.append(("wall_u", None, q["wall_u"], new)); q["wall_u"] = new
        elif k == "roof_u":
            new = r2(q["roof_u"] * rng.choice([0.5, 0.6, 0.7]), 0.01)
            edits.append(("roof_u", None, q["roof_u"], new)); q["roof_u"] = new
        elif k == "win":
            new = (r2(rng.uniform(1.2, 1.8), 0.1), r2(rng.uniform(0.22, 0.3), 0.01))
            edits.append(("win", None, (q["win_u"], q["win_shgc"]), new))
            q["win_u"], q["win_shgc"] = new
            q["win_vt"] = r2(min(q["win_vt"], new[1] * 1.6), 0.01)
            edits[-1] = ("win", None, edits[-1][2], (new[0], new[1], q["win_vt"]))
        elif k == "lpd":
            new = r2(q["lpd"] * rng.choice([0.6, 0.7, 0.75]), 0.1)
            edits.append(("lpd", None, q["lpd"], new)); q["lpd"] = new
        elif k == "setpoint":
            new = (q["heat_sp"][0] - 1.0, q["cool_sp"][0] + 1.0)
            edits.append(("setpoint", None, (q["heat_sp"][0], q["cool_sp"][0]), new))
            q["heat_sp"] = (new[0], q["heat_sp"][1]); q["cool_sp"] = (new[1], q["cool_sp"][1])
        elif k == "schedule_unocc":
            new = (r2(max(0.0, q["ltg_frac"][1] - 0.05), 0.05), r2(max(0.05, q["eqp_frac"][1] - 0.15), 0.05))
            edits.append(("schedule_unocc", None, (q["ltg_frac"][1], q["eqp_frac"][1]), new))
            q["ltg_frac"] = (q["ltg_frac"][0], new[0]); q["eqp_frac"] = (q["eqp_frac"][0], new[1])
        elif k == "ach":
            new = r2(max(0.05, q["ach"] * 0.5), 0.05)
            edits.append(("ach", None, q["ach"], new)); q["ach"] = new
    return q, edits


def sample_task(seed, tier, idx):
    rng = random.Random(seed)
    for _ in range(50):
        p = base_params(rng, tier if tier != "TE" else rng.choice(["T1", "T2", "T3"]))
        if tier == "TE":
            # edit tasks reuse any earlier-tier base model
            p0 = p
            p1, edits = make_edit(rng, p0)
            t = {"tier": tier, "base": p0, "target": p1, "edits": edits}
        else:
            t = {"tier": tier, "target": p}
        t["seed"] = seed
        return t
