# D. BEM validation, verification, benchmarking traditions and building-domain datasets

## 1. Query log (2026-11-07)
| date | source | query | hits | kept |
|---|---|---|---|---|
| 2026-11-07 | Crossref | calibration methodologies building energy models (Coakley; Fabrizio & Monetti) | 5+5 | 2 |
| 2026-11-07 | Crossref | DOE commercial reference buildings Deru | 5 | 2 |
| 2026-11-07 | Crossref | ComStock / end-use load profiles | 5 | 1 |
| 2026-11-07 | Crossref | ResStock residential building stock | 5 | 1 |
| 2026-11-07 | Crossref | BESTEST Judkoff Neymark | 5 | 2 |
| 2026-11-07 | Crossref | Building Data Genome Project 2 | 3 | 1 |
| 2026-11-07 | Crossref | Great Energy Predictor III | 5 | 2 |
| 2026-11-07 | Crossref | BOPTEST | 5 | 2 |
| 2026-11-07 | Crossref | CityLearn | 5 | 1 |
| 2026-11-07 | Crossref | BuildingsBench | 5 | 1 |
| 2026-11-07 | Crossref | Brick schema | 5 | 0 (original Balaji 2016 paper not found in Crossref; not listed) |
| 2026-11-07 | Crossref | modeller performance gap / modeler decisions | 5+5 | 3 |
| 2026-11-07 | Crossref | uncertainty analysis building performance simulation | 5 | 3 |
| 2026-11-07 | Crossref | sensitivity analysis building energy review | 3 | 1 |
| 2026-11-07 | Crossref | empirical validation building energy simulation programs | 5 | 1 |
| 2026-11-07 | Crossref | LLM benchmark building codes QA; AECBench | 5+5 | 1 |
| 2026-11-07 | Crossref | ASHRAE Guideline 14 CV(RMSE) NMBE | 5 | 0 (standard itself has no DOI) |
| 2026-11-07 | OpenAlex | not used | - | - |

Several guessed DOIs (e.g. Brick 2016, ComStock/ResStock papers) returned NOT FOUND in Crossref and were dropped. Web search was not run; items below are Crossref-verified unless marked "no DOI".

## 2. Kept items
| key | year | venue | DOI/URL | what it is | key criterion / finding | how it informs GenAI-BEM benchmark |
|---|---|---|---|---|---|---|
| ashrae140_2020 | 2020 (rev.) | ANSI/ASHRAE Std 140 | no DOI; https://www.ashrae.org/technical-resources/bookstore/standard-140 | Method of test for building energy simulation software (BESTEST-derived) | Compare tool outputs against a range of reference-program results | Template for case-based diagnostic test suite design |
| judkoff2004iea | 2004 | NREL/IEA report | 10.2172/15015114 | IEA BESTEST/diagnostic method for HVAC equipment (NREL OSTI) | Comparative testing methodology: inter-program ranges as acceptance bands | Reference ranges rather than single truth for tolerances |
| judkoff2002iea | 2002 | NREL/IEA report | 10.2172/15000340 | IEA BESTEST HVAC diagnostic method (earlier volume) | Same | Same; staged diagnostic cases |
| judkoff2011bestestex | 2011 | NREL preprint | 10.2172/1029029 | BESTEST-EX methodology for existing-home calibration/test | Test of tools' ability to predict retrofit savings | Tests derived quantities, not just totals |
| neymark2010bestestex | 2010 | NREL report | 10.2172/988600 | BESTEST-EX Phase 1 test procedure | Procedural test spec | Template for written test procedure |
| henninger_empirical1997 | 1997 | Energy and Buildings | 10.1016/s0378-7788(97)00007-8 | Empirical validation of simulation programs (title as indexed; author/details unverified) | Analytical, comparative and empirical validation trio | Validation taxonomy for benchmark claims |
| coakley2014review | 2014 | Renewable Sustainable Energy Rev. | 10.1016/j.rser.2014.05.007 | Review of calibration methods | Cites Guideline 14 / IPMVP / FEMP thresholds; calibration is under-determined | Justifies metric thresholds and warns of equifinality |
| fabrizio2015calibration | 2015 | Energies | 10.3390/en8042548 | Calibration methodology review | Monthly NMBE +/-5%, CV(RMSE) 15%; hourly +/-10% / 30% (Guideline 14, as commonly quoted) | Direct source for score tolerances |
| chong2016autotune | 2016 | Applied Energy | 10.1016/j.apenergy.2016.08.073 | Autotune vs manual calibration | Automated vs manual calibration comparison | Automated vs human-generated reference |
| deru2011reference | 2011 | NREL/TP-5500-46861 | 10.2172/1009264 | DOE Commercial Reference Building Models | 16 building types x 16 climates | Candidate reference/ground-truth models |
| field2010reference | 2010 | IBPSA-USA BSC | 10.26868/30680611.2010.ts02b-02-field | Using DOE Reference Buildings for studies | Usage guidance | Prototype baselines |
| wilson2022elp | 2022 | NREL report | 10.2172/1906716 | End-Use Load Profiles (ComStock/ResStock) practical guidance | Stock models calibrated against utility data | Large source of diverse reference models |
| resstock2025sa | 2025 | IBPSA BSC | 10.26868/25222708.2025.1632 | Sensitivity analysis of US housing stock with ResStock | Ranks influential characteristics | Which inputs to weight in scoring |
| robinson2017modellers | 2017 | Building Serv. Eng. Res. Technol. | 10.1177/0143624416684641 | "The building performance gap: Are modellers literate?" | Modeller competence contributes to the gap | Human-error baseline for LLM output |
| modeler2015decisions | 2015 | IBPSA BSC | 10.26868/25222708.2015.2739 | Effect of modeler decisions on simulation uncertainty | Different modelers, same building, differing results | Inter-modeler spread as tolerance floor |
| modeler2014impact | 2014 | ASHRAE/IBPSA-USA | 10.26868/25746308.2014.26 | Impact of modeler decisions on results | Same | Same |
| hopfe2016uncertainty | 2016 | J. Build. Perform. Simul. | 10.1080/19401493.2017.1261641 | Treating uncertainty in BPS | Uncertainty taxonomy | Separate model-form vs input uncertainty |
| sensitivity2024 | 2024 | J. Build. Perform. Simul. | 10.1080/19401493.2024.2387071 | Advanced UA/SA of building energy performance | Methods | Perturbation-test design |
| qa2023stock | 2023 | J. Build. Perform. Simul. | 10.1080/19401493.2023.2248063 | QA for building-stock energy models (eleven UQ methods) | Method comparison | QA tradition for generated model sets |
| tian2013sensitivity | 2013 | Renewable Sustainable Energy Rev. | 10.1016/j.rser.2012.12.014 | Review of SA methods in building energy | Method survey | Weights for input importance |
| miller2020bdg2 | 2020 | Scientific Data | 10.1038/s41597-020-00712-x | Building Data Genome Project 2 | Open meter data, 1,636 buildings (as commonly cited) | Data-governance exemplar |
| miller2020gepiii | 2020 | Sci. Technol. Built Environ. | 10.1080/23744731.2020.1795514 | GEPIII competition overview | Public leaderboard, large-scale benchmark | Leaderboard design |
| miller2022gepiii_limits | 2022 | Sci. Technol. Built Environ. | 10.1080/23744731.2022.2067466 | Limits of ML for building energy prediction (GEPIII) | Leaderboard overfitting / data quality issues | Benchmark trustworthiness pitfalls |
| blum2021boptest | 2021 | IBPSA BSC | 10.26868/25222708.2021.11134 | BOPTEST intro | Standardised KPIs for control benchmarking | KPI/API-based scoring |
| vazquez2019citylearn | 2019 | ACM BuildSys | 10.1145/3360322.3360998 | CityLearn v1.0 | RL challenge environment | Challenge-style benchmark |
| emami2023buildingsbench | 2023 | NeurIPS D&B | 10.52202/075280-0871 | BuildingsBench: 900K simulated buildings, load-forecasting benchmark | Synthetic-to-real transfer | Closest building-ML benchmark precedent |
| aecbench2026 | 2026 | Adv. Eng. Informatics | 10.1016/j.aei.2026.104314 | AECBench, hierarchical LLM knowledge benchmark for AEC | Knowledge-level tasks | Related LLM benchmark; no simulation-based scoring |

Caveat: author names in keys for some items are placeholders from partial metadata; confirm authors and quoted figures before citing.

## 3. Synthesis
The simulation community has a mature validation tradition (analytical, comparative, empirical) built on BESTEST and ASHRAE 140, which uses inter-program ranges rather than single truths as acceptance bands. Calibration practice (Guideline 14, IPMVP, FEMP) supplies concrete tolerances, NMBE and CV(RMSE), usable for scoring generated models. Studies of modeler decisions show humans building the same building differ appreciably, so a GenAI benchmark should calibrate tolerances to inter-modeler spread and report human baselines. DOE reference buildings and ComStock/ResStock are natural reference-model sources. ML benchmarks (GEPIII, BuildingsBench, BOPTEST, CityLearn) show leaderboard design and the pitfalls of overfitting and data quality. Existing AEC LLM benchmarks (AECBench) test knowledge, not simulation outcomes, so the gap this paper targets remains open.
