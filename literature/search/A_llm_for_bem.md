# Angle A: GenAI / LLMs / agents for building energy modeling

Note: search was short (Crossref flaky/rate-limited, no OpenAlex used). Evaluation columns come from web-search snippets and titles; full texts were NOT read. Treat "eval" cells marked (?) as to-be-verified. Coverage is incomplete (target 15-30 not reached).

## 1. Query log
| date | source | query | hits | kept |
|---|---|---|---|---|
| 2026-11-07 | Crossref | large language model EnergyPlus | 12 (irrelevant) | 0 |
| 2026-11-07 | Crossref | large language model building HVAC control | 12 | 2 |
| 2026-11-07 | Crossref (bibliographic) | 13 title/topic lookups (EPlus-LLM, Zhang agentic, MCP, fine-tuning, BIM, Modelica, calibration, QA, Guideline 36) | ~3 each | 11 |
| 2026-11-07 | Web search | Eplus-LLM large language model EnergyPlus building energy modeling | 10 | 4 |
| 2026-11-07 | Web search | LLM agent EnergyPlus OpenStudio automated building energy model generation arXiv | 10 | 3 |
| 2026-11-07 | OpenAlex | not used | 0 | 0 |

## 2. Kept papers (all DOIs resolved via Crossref)
| key | year | venue | DOI | problem | method | evaluation (?=unverified) | limitation for benchmarking |
|---|---|---|---|---|---|---|---|
| jiang2024eplus | 2024 | Applied Energy | 10.1016/j.apenergy.2024.123431 | NL description to EnergyPlus IDF | fine-tuned T5, then script runs EnergyPlus | project page claims 100% modeling accuracy, >95% time saved; small set of case buildings (?) | self-reported; test set not a public benchmark; simple buildings |
| jiang2024eplusashrae | 2024 | ASHRAE Annual Conf. | 10.63044/s24jia28 | same, conference version | same | (?) | as above |
| zhang2024advancing | 2024 | Energy and Buildings | 10.1016/j.enbuild.2024.114788 | ChatGPT/GPT-4 with EnergyPlus | prompt engineering, RAG, multi-agent; 3 case studies (iUnit testbed) | qualitative case studies; runs in EnergyPlus (?) | few cases, no metrics suite; arXiv 2402.09579 |
| zhang2024advancingibpsa | 2024 | IBPSA-USA SimBuild | 10.26868/30680611.2024.2104 | conference version | same | (?) | as above |
| zhang2025agentic | 2025 | Energy and Buildings | 10.1016/j.enbuild.2024.115116 | auto IDF generation and debugging | four-agent workflow (preprocess, extract, generate objects, debug via simulation) | error-free simulation on iUnit case (?) | single case; no public test set |
| jiang2025finetune | 2025 | Automation in Construction | 10.1016/j.autcon.2025.106223 | complex-case BEM from NL | efficient fine-tuning of LLMs | accuracy on complex cases (?) | numbers unverified; data availability unknown |
| zhang2025schema | 2025 | Automation in Construction | 10.1016/j.autcon.2025.106244 | agent for energy analysis and modeling | LLM agent with schema and library | (?) | unverified |
| liu2026driven | 2026 | Energy and Buildings | 10.1016/j.enbuild.2026.117255 | LLM-driven BEM generation | (?) | (?) | needs reading |
| jiang2026ashraecomplex | 2026 | ASHRAE Winter Conf. | 10.63044/w26jia171 | complex BEM from NL, real-world cases | (?) | real-world cases (?) | needs reading |
| li2025energyplusmcp | 2025 | SoftwareX | 10.1016/j.softx.2025.102367 | LLM tool access to EnergyPlus | MCP server, 35 tools | software description; no accuracy benchmark | tooling, not evaluation |
| ball2026openstudiomcp | 2026 | SoftwareX | 10.1016/j.softx.2026.103020 | LLM agents with OpenStudio | MCP server | software description (?) | tooling only |
| zhang2024interpretable | 2024 | Energy and Buildings | 10.1016/j.enbuild.2024.114278 | LLM-aided interpretable ML control | LLM + ML control | energy/comfort in simulation (?) | control, not model generation |
| jiang2026hvaccode | 2026 | Buildings | 10.3390/buildings16091722 | HVAC control code generation | LLM + RAG, simulation-model validation, iterative repair | code accuracy checked by simulation (abstract) | numbers not read; control not BEM |
| wan2025genai | 2025 | Building Simulation | 10.1007/s12273-025-1279-x | review of Gen-AI in building research | review (arXiv 2410.01098) | n/a | no benchmark |
| guo2025uavbim | 2025 | Energy and Buildings | 10.1016/j.enbuild.2024.115120 | UAV-to-BIM-to-BEM automation | non-LLM pipeline (context) | (?) | not GenAI; context only |

Unverified / not yet found: LLM Modelica generation, LLM building-energy QA, LLM calibration (SSRN 10.2139/ssrn.6086104 "Model-agnostic calibration ... LLM", 2026, preprint, not read), BIM-to-BEM with LLMs, DARLIN (SSRN 10.2139/ssrn.7135996, LLM HVAC, 2026, not read), urban BEM with LLM (10.5194/icuc12-542, not read).

## 3. Synthesis
The literature shows that LLMs (fine-tuned T5, GPT-4 with prompting, RAG, multi-agent debugging loops, and MCP tool servers) can produce runnable EnergyPlus models from natural language, mostly for single-zone or small-building cases, with a simulation-in-the-loop debug step. Evaluation is largely success-of-execution or qualitative case study on a few buildings (e.g., iUnit), with self-reported near-perfect accuracy. Missing: shared public test sets, standard prompts/tasks of graded difficulty, metrics beyond "it runs" (fidelity versus reference energy use, geometry/schedule/HVAC correctness), repeated-trial variance, cross-model comparison, contamination control, and a common leaderboard. Modelica, BIM-to-BEM and calibration with LLMs are thinly covered. Full-text verification of the evaluation columns is still needed.
