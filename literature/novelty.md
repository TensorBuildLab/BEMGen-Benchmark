# Novelty check: open, simulation-graded, grader-validated, governed benchmark for NL-to-EnergyPlus generation (+ reusable benchmark-building workflow)
**Verdict:** Partial overlap | **Date:** 2026-11-07 | **Searches:** 21 queries across web search (12), arXiv API (7 id lookups + 6 keyword searches), Crossref (5 keyword + 7 DOI lookups), OpenAlex (5 calls: 1 id lookup, 2 forward-citation searches on EPlus-LLM, 1 batch abstract lookup, 1 failed call), doi.org handle check (27 DOIs)

No paper found does the whole combination: (a) a public NL-to-EnergyPlus generation benchmark with (b) a hidden, procedurally generated test split, (c) three-layer simulation grading with ensemble-calibrated per-task tolerances, (d) grader validation through false-reject and false-accept rates measured against EUI ±10% and Guideline 14 criteria, and (e) a governed leaderboard. Each component has close precedents, though. The nearest is **Buildrix** (Jiang & Dong, arXiv 2606.25139, June 2026). It is a community benchmarking platform for agentic AI skills in building engineering, and it includes an EnergyPlus IDF-generation skill, expert-verified "golden" test cases and a leaderboard. The second nearest is **BEMEval** (Jia, Fu, Zhang, 2026), a declared benchmark *suite* for LLM BEM tasks. Its first task is document-to-schema extraction, not IDF generation, but the suite says later BEM-task benchmarks are planned, so this space may be claimed next. Abstracts are below. Full texts were read only for Buildrix (via arXiv HTML).

## Direct overlaps
None found. No paper builds a public benchmark for NL-to-EnergyPlus model generation with simulation-based multi-layer grading and validated grader error rates.

## Partial overlaps
| Paper (DOI) | What is shared | What is different | What the authors must say to set their work apart |
|---|---|---|---|
| Jiang & Dong 2026, *Buildrix: An Open Platform for Sharing and Benchmarking Agentic AI Skills in Building Engineering*, arXiv (10.48550/arXiv.2606.25139) | Open hub with leaderboard for building-engineering agent tasks; includes a ResStock EnergyPlus IDF-generation skill and runs EnergyPlus; expert-verified "golden" test cases; quantitative cases scored against expert reference data with weighted rubric + pass threshold | Benchmarks *skills* (packaged tools), not raw model generation; rubric thresholds are contributor-set, with no numerical tolerances and no ensemble calibration; no hidden or procedurally generated test split; no grader validation (no FAR/FRR, no mutants); no CIs, rank bands, rate limits or verified/self-reported tiers; no model results reported | Cite it as the closest platform. State that this work measures *model* capability on NL→IDF under a hidden, rotating split. State that tolerances are derived from an ensemble of valid models, not set by hand. Note that the grader's own error rates are measured, and that the leaderboard has statistical governance Buildrix lacks |
| Jia, Fu & Zhang 2026, *BEMEval-Doc2Schema*, arXiv (10.48550/arXiv.2602.16926) and IBPSA-USA SimBuild 2026 (10.26868/30680611.2026.1360) | Declares an open, community-driven *benchmark framework for LLM BEM tasks* with curated data, ground truth and metrics; GPT-5 vs Gemini 2.5 comparison | Task is document→HPXML/EPC schema extraction scored by key-value overlap (KVOR); no simulation, no IDF generation, no hidden split, no grader validation, no leaderboard governance | Position this work as the first *simulation-graded generation* benchmark, either inside or alongside the BEMEval suite. If the authors are the same group, say explicitly how the two relate |
| Jiang et al. 2025, *Benchmarking Knowledge and Capability of LLMs in Building Science Domain*, Energy Use (10.59717/ipj.energy-use.2025.100026) | Benchmarks 15 LLMs on building science (1,487 questions); AI-Judger validated against humans | Knowledge QA, not model generation; LLM-judge scoring, not simulation | Present it as the knowledge-level counterpart. Simulation scoring removes judge bias |
| *Knowledge-Guided Self-Reflection LLM Agents for HVAC Simulation in EnergyPlus*, ACM e-Energy/BuildSys 2026 (10.1145/3744256.3812593) | NL→EnergyPlus (via OpenStudio Measures) over 1,320 tasks; 4 LLM backends; execution-feedback self-reflection, which overlaps RQ3 | Measure argument selection, not whole-model generation; correctness is translation accuracy, not end-use fidelity with tolerances; no public hidden split or leaderboard | Cite it for RQ3 (execution feedback). Contrast its translation-accuracy scoring with this work's spec-conformance and end-use layers |
| *Text-To-EnergyPlus*, BuildSys 2025 poster (10.1145/3736425.3772120) | NL→executable EnergyPlus HVAC scripts evaluated on a dataset | Method paper (KG + actor-evaluator); dataset and metrics not described as a benchmark | Cite it as a method; its dataset is not a governed benchmark |
| *Localized LLM selection for agentic BEM worker routing*, The Innovation Energy 2026 (10.59717/j.xinn-energy.2026.100194) | Benchmark of 7 LLM backends on 100 manually checked BEM agent tasks per language (prototype generation, modification, simulation) | Scores routing/tool-call correctness, not generated-model fidelity; no hidden split or grader validation | Distinguish routing accuracy from model-output correctness |
| *Tool-augmented vs. autonomous LLM agents for BEM modifications (NECB)*, Energy and AI 2026 (10.1016/j.egyai.2026.100896) | LLM edits to EnergyPlus IDFs on 7 reference models × 3 complexity tiers; energy results compared | IDF modification, not generation; small fixed task set; no tolerance calibration | Cite it for task tiers and modification tasks |
| ModiGen, arXiv 2025 (10.48550/arXiv.2503.18460) | Benchmark for LLM Modelica generation; staged grading (load → simulate → RMSE vs reference within a tolerance) | Modelica, not EnergyPlus; fixed tolerance, not ensemble-calibrated; no grader FAR/FRR | Note that the staged-grading idea exists in Modelica; the novelty here is calibrated tolerance + grader validation |
| CFDLLMBench / FoamBench, arXiv 2025 (10.48550/arXiv.2509.20374) | Simulation-graded benchmark for LLM-generated OpenFOAM cases (executability, solution accuracy, convergence); parameter-variation (procedural) cases | CFD domain; no hidden split, no grader validation, no governance | Cite it as the closest *engineering-simulation* analogue of the three-layer grader |
| EngDesign, NeurIPS D&B 2025 (10.48550/arXiv.2509.16204) | Engineering-design benchmark scored by executable domain simulations (SPICE, FEA, control) | Multi-domain; no BEM; no grader-error validation | Cite it as the precedent for simulation-based grading of LLM designs |
| CodeAssay, arXiv 2026 (10.48550/arXiv.2608.03535) | Hidden grading tests + mutation-based validation of the test suite; audited ground truth; significance tests between models | Python code, not engineering simulation; mutation score, not paired FAR/FRR against conventional criteria | Cite it for the grader-validation method; claim the first application to simulation graders and comparison against Guideline 14 / EUI ±10% |
| *Beyond Mutation Coverage: Auditing Verdict Reliability in RTL Generation Benchmarks*, NeurIPS 2026 (no DOI; https://neurips.cc/virtual/2026/161622) and *Red-Teaming the Grader: Mutation-Validated Constraint Checking for Tool-Agent Benchmarks*, NeurIPS 2026 (no DOI; https://neurips.cc/virtual/2026/172887) | Measure both false accepts (mutants) and false rejects (correct candidates rejected) of benchmark graders, close to RQ2's design | Hardware RTL / tool agents, not BEM; no simulation-tolerance calibration | Cite both as direct methodological precedent for RQ2. Do not claim grader mutation validation is new in general, only for BEM/simulation graders. **DOI not verified (NeurIPS virtual pages only).** |

## Related work the authors don't list
| Paper (DOI) | Why it matters |
|---|---|
| Liu, Zhou, Li 2026, *Large language model–driven building energy model generation*, Energy and Buildings (10.1016/j.enbuild.2026.117255) | Same task (LLM BEM generation, LoRA → simulation-ready IDF per web snippet). Abstract not retrievable (403). **Authors must read it** to check whether it releases a test set |
| Jiang, Ma, Zhang, Chen 2025, *Prompt engineering to inform LLM in automated BEM*, Energy (10.1016/j.energy.2025.134548) | Prompting baseline for NL→IDF; evaluation set and code public |
| LLM-BEM-engineer, Adv. Eng. Informatics 2026 (10.1016/j.aei.2026.105209) | Multi-agent NL→BEM system (Jiang et al. line); likely candidate system to evaluate on the benchmark |
| Data2BEM, iScience 2025 (10.1016/j.isci.2025.113867) | LLM multi-agent BEM generation + calibration meeting Guideline 14-type accuracy, a precedent for using calibration criteria as acceptance |
| Pagri et al. 2026, fine-tuning vs prompting for IDF with rooftop PV, E3S Web Conf. (10.1051/e3sconf/202671606011) | Executability failures of prompting on complex IDFs; tier evidence |
| Zhang & Xu 2026, LLM+RAG automated BEM, E3S Web Conf. (10.1051/e3sconf/202668908004) | Reports load agreement vs manual models, an informal fidelity criterion |
| Eppy-LLM, SimBuild 2026 (10.26868/30680611.2026.1305) | Agentic NL→EnergyPlus workflow (abstract not available) |
| OptAgent, arXiv 2026 (10.48550/arXiv.2601.20005) | ~4,000-run benchmark of agentic building-energy workflows (accuracy, tokens, cost) |
| AutoB2G, arXiv 2026 (10.48550/arXiv.2603.26005) | NL→building–grid co-simulation pipelines scored on execution success, config correctness and simulation validity by tier, close to the three-layer idea |
| BuildThermBench (Liu et al.), SSRN 2026 (10.2139/ssrn.7300712) | EnergyPlus-grounded LLM benchmark (thermal reasoning + closed-loop control); deterministic scenario IDs; not generation. Full text not read (403) |
| KebGraph agentic grounding, Energy and Buildings 2026 (10.1016/j.enbuild.2026.118187) | 213-question building benchmark across 4 LLMs, plus agentic thermal-model building |
| Building Control Description Language Modelica generation, arXiv 2025 (10.48550/arXiv.2509.14623) | LLM building-control Modelica; finds AI evaluation inferior to human for behavioural correctness, which supports simulation-based grading |
| Stürmer et al. 2026, Fluid-system simulation code generation benchmark, arXiv (10.48550/arXiv.2607.29389) | "Runnable ≠ correct" finding; 10 LLMs on Modelica/WNTR |
| OpenStudio-MCP, SoftwareX 2026 (10.1016/j.softx.2026.103020) | Tool access that benchmark agent tracks may allow |

## Queries
| # | Source | Query | Hits (relevant) |
|---|---|---|---|
| 1 | Web | benchmark large language models EnergyPlus model generation dataset 2025 | 10 (BEMEval, E3S PV, Energy Use benchmark) |
| 2 | Web | LLM building energy modeling benchmark leaderboard IDF generation evaluation | 10 (BEMEval) |
| 3 | Web | arXiv benchmark LLM agents building energy simulation tasks EnergyPlus OpenStudio | 10 (AutoB2G, BEMEval) |
| 4 | Web | LLM Modelica code generation benchmark evaluation simulation | 10 (ModiGen, CDL, fluid systems) |
| 5 | Web | "Benchmarking knowledge and capability of large language models in building science domain" | 10 (Energy Use paper, AECBench, Qwen-BIM) |
| 6 | Web (extended) | EnergyPlus LLM benchmark 2026 arXiv natural language to building energy model tasks hidden test | 9 (Buildrix, BuildThermBench, Liu 2026) |
| 7 | Web | mutation testing validate benchmark grader false accept LLM code generation test adequacy | 10 (CodeAssay, RTL audit, Red-Teaming the Grader, evalmut) |
| 8 | Web | LLM HVAC system design benchmark dataset simulation-based evaluation 2026 | 10 (HVAC review, OptAgent) |
| 9 | Web | "Large language model–driven building energy model generation" Energy and Buildings 2026 | 10 (none exact) |
| 10 | Web | "Prompt engineering to inform large language model in automated building energy modeling" | 10 (1) |
| 11 | Web | Liu Zhou Li 2026 building energy model generation ... 117255 | 10 (0) |
| 12 | Web | CFD LLM benchmark OpenFOAM FoamBench CFDLLMBench | 10 (CFDLLMBench) |
| 13 | Web | "LLM-BEM-engineer" ... | 10 (HF card, Data2BEM) |
| 14 | Web | EngDesign benchmark engineering design LLM simulation-based evaluation | 10 (EngDesign) |
| 15 | arXiv API | EnergyPlus AND (LLM OR "language model") | 7 (0 new benchmarks) |
| 16 | arXiv API | "building energy" AND benchmark AND "language model" | 8 (BEMEval) |
| 17 | arXiv API | OpenStudio AND "language model" | 1 (0) |
| 18 | arXiv API | "building energy model" AND LLM | 4 (BEMEval) |
| 19 | arXiv API | "engineering simulation" AND benchmark AND LLM | 1 (0) |
| 20 | arXiv API | id lookups: 2606.25139, 2602.16926, 2601.20005, 2603.26005, 2607.29389, 2608.03535 | 6 (6) |
| 21 | Crossref | benchmark LLM EnergyPlus / LLM BEM generation benchmark / benchmarking LLM building science / BuildThermBench (failed) / LLM IDF generation evaluation (from 2025) | 12 each (≈10 kept) |
| 22 | OpenAlex | cites:W4396986140 (EPlus-LLM) + search "benchmark" | 69 (≈12 relevant) |
| 23 | OpenAlex | cites:W4396986140, from 2025-06 + search "evaluation dataset" | 58 (≈8 new) |
| 24 | OpenAlex | batch abstract lookup, 12 DOIs | 12 |

Not covered: no direct IBPSA BS2025 / ASHRAE 2026 proceedings sweep; Google Scholar not queried directly; full texts read only for Buildrix. Liu et al. 2026 (E&B 117255) and BuildThermBench could not be read (publisher 403).
