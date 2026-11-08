# OfficeSmall, 90.1-2019, Denver: scorecard item → IDF object/field

**IDF (target):** `/srv/data1/EnergyPlus-22-2-0/ExampleFiles/ASHRAE901_OfficeSmall_STD2019_Denver.idf`. This is the PNNL June-2020 release transitioned to EnergyPlus 22.2, with three partial run periods. Where the current PNNL file (`pnnl_prototypes_energycodes/extracted/ASHRAE901_OfficeSmall_STD2019/…_Denver.idf`, 2023-10, EnergyPlus 22.1) differs, the value is given as **[2023: …]**.

**Descriptions:**
* **S23**: combined scorecard `PNNL_Prototype_Scorecards.xlsx` (2023-10). Its zone values come from the 90.1-2004 Buffalo model; see the `raw_data` sheet.
* **S20**: per-building scorecard `archive_2020-06/PNNL_Scorecard_Prototypes_Office_Small.xls`. Sheets: Building Description, Zone Summary, Outdoor Air, Schedules.

**Match codes:**
* ✓ = description value reproduces the IDF value.
* ≈ = consistent but not enough to write the field.
* ✗ = description value contradicts the IDF.
* → std = description says "Requirements in codes or standards", so the value must come from ASHRAE 90.1-2019 (copyrighted, not supplied).
* — = not mentioned.

## 1. Program, site, form and geometry

| Scorecard item (source) | Description value | IDF object.field | IDF value | Match |
|---|---|---|---|---|
| Location (S20, S23 Climate Zone) | 5B Denver, `USA_CO_Denver-Aurora-Buckley.AFB.724695_TMY3` | Site:Location; SizingPeriod:DesignDay ×2 | 39.72 N, −104.75, UTC−7, 1726 m. Htg 99.6% −17.9 °C, Clg 0.4% 33.9/14.8 °C, ASHRAETau 0.423/2.020 | ≈. The weather file is named; design-day percentiles and conditions are not stated. |
| Vintage, fuels (S20) | new construction; gas and electricity | (implicit in equipment fuels) | NaturalGas supplementary coil; electric SWH | ≈ |
| Total floor area (S20) | 5,500 ft² (90.8 × 60.5 ft) | BuildingSurface:Detailed floors; Zone | 511.16 m² = 5,502 ft². Footprint 27.69 × 18.46 m | ✓ |
| Aspect ratio, floors (S20, S23) | 1.5; 1 | geometry | 1.5; 1 storey + attic zone | ✓ |
| Building shape (S23 image, S20) | 3D rendering only | BuildingSurface:Detailed ×43, GlobalGeometryRules | UpperLeftCorner, Counterclockwise, Relative coordinates | ≈. The picture is undimensioned. |
| Azimuth (S20) | "non-directional" | Building.North Axis | 0° | ≈. Long façades face N and S. |
| Thermal zoning (S20) | perimeter depth 16.4 ft; 4 perimeter + core + attic; 70/30 % | Zone ×6; surfaces | Perimeter depth 5.0 m; core 149.66 m² (29 %); attic unconditioned | ✓ |
| Floor-to-floor / floor-to-ceiling (S20) | 10 ft / 10 ft | Zone height (autocalculate) from vertices | 3.05 m walls | ✓ |
| Roof geometry (S20) | hipped roof, 10.76 ft ridge, 2 ft overhang/soffit | attic surfaces; `ext_soffit_floor` ×4 | ridge z = 6.33 m (3.28 m above ceiling); 0.6 m overhang | ✓ |
| WWR (S20, S23) | 24.4 % S, 19.8 % E/N/W; total 0.2119; 6 × 5 ft windows, sill 3 ft | FenestrationSurface:Detailed ×23 | S 20.64 m² (6 windows + 1 glass door), N 16.72 m² glass + 2 opaque doors, E/W 11.16 m² each | ✓. The **glass door on S and two opaque swinging doors on N** are not stated; only "building entrance" infiltration hints at them. |
| Window locations, shading (S20) | evenly distributed; no shading | window vertices | 5–6 punched windows per façade; no shading objects | ≈. Exact positions are a free choice. |
| Skylights (S20) | not modelled | — | none | ✓ |

## 2. Envelope

| Scorecard item | Description value | IDF object.field | IDF value (Denver, 90.1-2019) | Match |
|---|---|---|---|---|
| Exterior wall construction (S20, S23) | wood-frame 2×4 @16 in: 1 in stucco + 5/8 in gyp + insulation + 5/8 in gyp | Construction `nonres_ext_wall`; Material F07, G01 16 mm; Material:NoMass `Nonres_Exterior_Wall_Insulation` | layer order as stated; insulation R = 3.069 m²K/W, giving U ≈ 0.29 W/m²K (≈ U-0.051 IP) | ✓ for layers; **→ std** for R/U |
| Roof (S20, S23) | attic roof, wood joist; insulation + 5/8 in gyp | `nonres_roof` / `nonres_roof_floor` on the ceiling; `AtticRoofDeck` (asphalt shingles + 16 mm plywood) | insulation R = 8.098 m²K/W, giving U ≈ 0.12 W/m²K (≈ U-0.021 IP) | ✓ type; **→ std** value. The roof-deck layers are not stated. |
| Window U, SHGC, VT (S20) | "hypothetical window with weighted U and SHGC"; → std | WindowMaterial:SimpleGlazingSystem | U 2.044 W/m²K (0.36 IP), SHGC 0.38, VT 0.418 **[2023: 2.061/0.378/0.4158, one per orientation]** | **→ std**. The VT = 1.1 × SHGC rule is not stated. |
| Operable area (S20) | 0 | — | none | ✓ |
| Foundation (S20) | slab-on-grade, unheated, 8 in slab | Construction:FfactorGroundFloor ×5; Site:GroundTemperature:FCfactorMethod | F = 0.90012 W/m·K, area/perimeter per zone; core floor boundary = Adiabatic | ≈. F-factor → std. The F-factor method, perimeter exposure and monthly ground temperatures are not stated. |
| Interior partitions (S20) | 2×4 uninsulated stud wall | Construction `int_wall` | 2 × 13 mm gypsum, no cavity layer | ✗ (simplified) |
| Internal mass (S20) | 6 in standard wood (16.6 lb/ft²) | InternalMass ×5, `InteriorFurnishings` = `Std Wood 6inch` | 1,022 m² total (2 × floor area) | ≈. **The area is not stated.** |
| Infiltration (S20) | peak 0.2016 cfm/ft² ext wall, 25 % when fans on; extra entrance infiltration; "may differ by code" | ZoneInfiltration:DesignFlowRate ×6; schedules `INFIL_QUARTER_ON_SCH`, `INFIL_Door_Opening_SCH` | 0.00056896 m³/s·m² (= 0.112 cfm/ft²), coefficients 0/0/0.224/0. Door: Flow/Zone 0.07646 m³/s on Perimeter_ZN_1. Attic 0.2001 m³/s | ✗ for the rate (the scorecard gives the 2004 value). S23 lists 0.2018 cfm/ft² and a door flow of 275 cfm. The wind coefficients are not stated. |

## 3. Internal loads

| Scorecard item | Description value | IDF object.field | IDF value | Match |
|---|---|---|---|---|
| Lighting power density | S20: "→ std; see Zone Summary" (1.0 W/ft², labelled 90.1-2004). S23: 0.99 W/ft² | Lights.Watts per Zone Floor Area | 6.8889 W/m² = 0.64 W/ft² **[2023: 6.98149]** | ✗ (both scorecards give 2004) |
| Lighting fractions | — | Lights: return-air 0, radiant 0.7, visible 0.2 | as listed | — |
| Daylighting, occupancy sensors (S20) | → std | Daylighting:Controls ×4, Daylighting:ReferencePoint ×8; EMS programs ×5, sensors ×11, actuators ×5 | continuous/off, 377 lux, 2 points per perimeter zone (fractions 0.2399/0.0302). EMS sets lighting to 0.02 W/ft² when the zone is unoccupied | **→ std**. The control algorithm and reference points are free choices. |
| Plug loads (S20 Zone Summary, S23) | 0.63 W/ft² | ElectricEquipment.Watts per Zone Floor Area | 6.78 W/m² | ✓ |
| Occupancy (S20 / S23) | S20: 178.6 ft²/person. S23: 5.0 people per 1,000 ft² (200 ft²/person) | People.Zone Floor Area per Person | 16.588 m²/person (178.6 ft²) **[2023: 18.58 m² = 200 ft²]** | ✓ against the contemporaneous scorecard; ✗ across releases |
| People details | — | People: fraction radiant 0.3, sensible fraction autocalculate, ACTIVITY_SCH 120 W, CLOTHING_SCH, AIR_VELO_SCH, WORK_EFF_SCH | as listed | — |
| Gas equipment, elevators (S20) | none / NA | — | none | ✓ |
| Exterior lighting (S20) | "based on façade, parking, entrance … → std" | Exterior:Lights ×3, astronomical clock | 50.7 + 115.1 + 445.5 W **[2023: 87.95 + 200.47 + 773.25 W]**; schedules a, b_2016, c_2016 | **→ std / design assumption**. Not reproducible from the description. |

## 4. Schedules

| Scorecard item | Description value | IDF object | IDF value | Match |
|---|---|---|---|---|
| Occupancy (S20, S23) | weekday 0.11/0.21/1.0…, lunch dip | Schedule:Compact `BLDG_OCC_SCH_wo_SB`; Perimeter_ZN_2 uses `BLDG_OCC_SCH_w_SB` | S23 profile matches `wo_SB`. ZN_2 has a 10–11 h unoccupied "standby" hour | ✓ / ≈. The ZN_2 standby variant is only hinted at ("All except Perimeter_mid_ZN_2"). |
| Lighting (S20, S23) | weekday peak 0.90, night 0.18 | `BLDG_LIGHT_SCH` | weekday peak 0.699, 0.18 night (scaled for 90.1-2019 lighting-control credits) | ✗ |
| Equipment (S20, S23) | weekday 1.0 peak, 0.5 night, 0.2 weekend | `BLDG_EQUIP_SCH` | weekday peak 0.9595, night 0.41/0.16 (receptacle-control adjustment) | ✗ |
| HVAC operation (S20, S23) | on 6:00 to 19:00 weekdays | `HVACOperationSchd`; ZN_2 `HVACOperationSchd_w_SB`; `MinOA_MotorizedDamper_Sched` (07:00–19:00) | as listed | ✓ / ≈. The OA damper hours are not stated. |
| Setpoints (S20) | 75 °F cool / 70 °F heat; setback 85/60 °F | ThermostatSetpoint:DualSetpoint; `CLGSETP_SCH_NO_OPTIMUM`, `HTGSETP_SCH_NO_OPTIMUM` (+ `_w_SB` for ZN_2) | 23.89/21.11 °C occupied; 29.44/15.56 °C setback | ✓ (S20). S23 shows **no cooling setback** (✗). |
| SWH use (S20, S23) | weekday fraction profile | `BLDG_SWH_SCH` | as listed | ✓ (shape only) |
| Infiltration (S20, S23) | 1.0 off / 0.25 on | `INFIL_QUARTER_ON_SCH` | as listed | ✓ |
| Door opening | — | `INFIL_Door_Opening_SCH` | 0.131 / 1.0 profile | — |
| Holidays, DST, run period | — | RunPeriodControl:SpecialDays ×10; DaylightSavingTime; RunPeriod | US holidays; DST Mar–Nov; **3 partial run periods** (Jan, Apr, Jul) **[2023: one annual]** | — |

## 5. HVAC

| Scorecard item | Description value | IDF object.field | IDF value | Match |
|---|---|---|---|---|
| System type (S20, S23) | ASHP with gas furnace backup; single-zone CAV; one unit per zone (S23: "4.2 PSZ-HP with gas auxiliary heat") | AirLoopHVAC ×5; AirLoopHVAC:UnitaryHeatPump:AirToAir; Fan:OnOff; Coil:Cooling:DX:SingleSpeed; Coil:Heating:DX:SingleSpeed; Coil:Heating:Fuel; AirTerminal:SingleDuct:ConstantVolume:NoReheat | 5 loops, blow-through | ✓ topology. Node and branch wiring is a free choice. |
| Sizing (S20) | autosized to design day | Sizing:Parameters; Sizing:Zone ×5; Sizing:System ×5 | global factors 1.2/1.2; SAT 12.8/40 °C; humidity ratios 0.0085/0.008; NonCoincident; sensible-load sizing | ≈. **The sizing factors are not stated.** |
| Supply air temperature (S20) | max 104 °F, min 55 °F | Sizing:Zone/System; SetpointManager:SingleZone:Cooling/Heating | 40 °C / 12.8 °C | ✓ |
| Cooling efficiency (S20) | → std (packaged HP minimum) | Coil:Cooling:DX:SingleSpeed.Gross Rated COP | 4.117 | **→ std**, plus PNNL's SEER→COP conversion (not stated) |
| Heating efficiency (S20) | → std | Coil:Heating:DX:SingleSpeed.Gross Rated COP; Coil:Heating:Fuel.Efficiency | 3.359; gas 0.81 **[2023: 0.80]** | **→ std** |
| HP details | — | Coil:Heating:DX: min compressor OAT −12.2 °C; max defrost OAT 1.67 °C; crankcase heater 50 W below 4.4 °C; ReverseCycle/OnDemand defrost. Unitary: max supplementary-heater OAT 4.44 °C; rated fan power per flow 934.4 W/(m³/s) | as listed | — |
| Performance curves | — | Curve:Biquadratic ×12, Quadratic ×19, Cubic ×3 | HPACCool*/HPACHeat* **[2023: SmDXalt_* cooling curves]** | — (free choice; changes the physics) |
| Supply fan (S20) | efficiency "depending on motor size → std"; pressure "depending on cfm" | Fan:OnOff | total eff 0.55575, Δp 622.5 Pa, motor eff 0.855, motor in air 1.0 | **→ std** |
| Economizer (S20) | → std | Controller:OutdoorAir.Economizer Control Type | NoEconomizer | **→ std** |
| Ventilation (S20 Outdoor Air; S23) | S20: 62.1 table → 0.085 cfm/ft² (90.1-2007/2010 columns). S23: 20 cfm/person (62-1999) | DesignSpecification:OutdoorAir ×5 | Flow/Area 0.000431773 m³/s·m² (= 0.085 cfm/ft²) | ✓ (S20); ✗ (S23) |
| DCV, energy recovery (S20) | → std | — **[2023: Controller:MechanicalVentilation ×5, ZoneSum, DCV = No]** | none | **→ std** |
| Night cycling | — | AvailabilityManager:NightCycle ×5 | CycleOnAny, 1.0 K tolerance, 1800 s | — |
| Thermostat control | — | ZoneControl:Thermostat ×5, control type 4 (dual) | as listed | ≈ |
| Chilled/hot water, pumps, tower (S20) | NA | — | none for HVAC | ✓ |

## 6. Service water heating

| Scorecard item | Description value | IDF object.field | IDF value | Match |
|---|---|---|---|---|
| SWH type, fuel (S20) | storage tank, electric | WaterHeater:Mixed | electricity, tank in CORE_ZN | ✓ |
| Tank volume, setpoint (S20) | 40 gal, 140 °F | WaterHeater:Mixed.Tank Volume; setpoint schedule | 0.1514 m³; 60 °C | ✓ |
| Thermal efficiency (S20) | → std | WaterHeater:Mixed.Heater Thermal Efficiency | 1.0 | **→ std** |
| Heater capacity, standby loss | — | WaterHeater:Mixed.Max Capacity; off/on-cycle loss coefficients | 11,722.84 W; 1.206 W/K; 2.0 K deadband; max 82.2 °C | — |
| Water consumption (S20) | "see schedules" (fraction only) | WaterUse:Equipment.Peak Flow Rate | 4.048 × 10⁻⁶ m³/s, 55 °C use temperature, sensible/latent 0.2/0.05 | ✗/— (**peak flow not stated**) |
| Distribution | — | PlantLoop, Pump:ConstantSpeed (Intermittent, 0 W), Pipe:Adiabatic ×5, Sizing:Plant 48.89 °C, Site:WaterMainsTemperature (correlation 9.95/23.7) | as listed | — |

## 7. IDF content with no counterpart in either scorecard (free choices or implicit conventions)

* **Simulation controls:**
  * Timestep 4/h.
  * HeatBalanceAlgorithm CTF, 200 °C limit.
  * Surface convection TARP inside and outside.
  * ShadowCalculation PolygonClipping every 30 days, 200 figures **[2023: 15000]**.
  * Building terrain City.
  * Convergence tolerances 0.04 W / 0.2 K; warm-up 6–15 days **[2023: 25]**.
  * SimulationControl flags.
  * ConvergenceLimits.
* **Run period and calendar:** run period(s), start day, holidays (10 RunPeriodControl:SpecialDays), daylight saving time.
* **Design days:** choice and parameters of the 2 design days.
* **Ground and water mains:** Site:GroundTemperature:FCfactorMethod values; Site:WaterMainsTemperature correlation.
* **Exact geometry:** vertex coordinates, window and door positions, two opaque north doors and the south glass door, attic geometry, soffits. These are reconstructible from S20 dimensions only to within window placement.
* **Material properties:** stucco, gypsum, plywood, shingles; insulation expressed as Material:NoMass. The unused res/semiheated constructions are harmless clutter.
* **Internal mass area**; People thermal-comfort schedules and activity level; Lights and equipment heat fractions.
* **Lighting controls:** EMS occupancy-sensor logic; daylighting reference-point positions and control type.
* **HVAC:** all equipment curves, fan efficiencies and pressure rise, DX coil auxiliary fields (crankcase, defrost, minimum OAT), supplementary-heater limits, night-cycle parameters, OA damper schedule, sizing factors and humidity ratios.
* **SWH:** heater capacity, loss coefficients, peak flow, use temperature, loop and pump details.
* **Exterior lighting:** wattages and schedules.
* **Outputs:** Output:Table:Monthly ×9, Output:Meter ×3, OutputControl. These are owned by the benchmark harness anyway.

## 8. Take-aways for a DOE-based track

1. **No 2019-specific description exists.** S23 is generated from 90.1-2004 models. S20 defers every edition-dependent value to "Requirements in codes or standards". A 90.1-2019 brief therefore needs values extracted from the IDF itself, or the copyrighted 90.1-2019 tables.
2. Even S20 plus 90.1-2019 leaves physics-relevant free choices unstated:
   * equipment curves and the SEER→COP conversion;
   * fan Δp and efficiency;
   * internal-mass area;
   * SWH peak flow and capacity;
   * exterior lighting;
   * lighting and plug schedule adjustments for controls;
   * infiltration rate after air-barrier credit;
   * daylighting and occupancy-sensor implementation;
   * the ZN_2 standby logic.
   Under the paper's terminology, these would either have to be stated in the brief or covered by ensemble-calibrated tolerances.
3. The description sources disagree with each other on occupancy density, door infiltration and the cooling setback. The brief must be built from one pinned IDF, not taken from the scorecards as published.
4. Multi-modal inputs exist only as spreadsheets, PDF tables and undimensioned 3D renderings. No floor plans or elevations are published. Drawings would have to be rendered from the IDF geometry.
