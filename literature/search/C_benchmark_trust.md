# C. Benchmark quality, validity, contamination, leaderboard governance

## 1. Query log
Date 2026-11-07. Candidate list drawn from known literature; every item then existence-checked (arXiv API, DataCite arXiv DOI, Crossref). Hit counts are items checked, not search-engine totals. OpenAlex not used. Keyword Crossref/ACL/NeurIPS-D&B sweeps were not run in this pass (see gaps).

| date | source | query | hits | kept |
|---|---|---|---|---|
| 2026-11-07 | arXiv API | BetterBench / construct validity / everything benchmark / leaderboard illusion / Ladder / Dynabench / LiveBench / LiveCodeBench / error bars / datasheets / model cards / label errors / MT-bench / contamination survey / fair evaluators (15 ids) | 15 | 15 |
| 2026-11-07 | DataCite/doi.org (arXiv DOI) | rephrased-sample contamination, Show Your Work, reusable holdout, ImageNet v2, Data Cards, reproducibility, agentic benchmark practices, lm-eval lessons (8 ids) | 8 | 8 |
| 2026-11-07 | Crossref | datasheets, model cards DOIs | 2 | 2 |
| 2026-11-07 | Crossref | 10.1145/3442188.3445918 (probe, unrelated) | 1 | 0 |

## 2. Kept papers (25)
All DOIs verified (arXiv DOIs via arXiv API/DataCite; ACM DOIs via Crossref). Venue/number details are from my recall of the papers; flag for checking at the full-text stage.

| key | year | venue | DOI | problem | main finding / recommendation | implication for domain benchmark |
|---|---|---|---|---|---|---|
| reuel2024betterbench | 2024 | NeurIPS D&B | 10.48550/arXiv.2411.12990 | No quality standard for benchmarks | 46 best-practice criteria over lifecycle; 24 benchmarks scored, large quality spread, many lack reproducibility/stat significance | Use as audit checklist; publish score for own benchmark |
| bean2025construct | 2025 | NeurIPS D&B | 10.48550/arXiv.2511.04703 | Benchmarks may not measure target construct | Review of 445 LLM benchmarks; many have weak construct definition, convenience sampling, no uncertainty; 8 recommendations | Define "building-modeling competence" construct explicitly |
| raji2021everything | 2021 | NeurIPS D&B | 10.48550/arXiv.2111.15366 | "General" benchmarks overclaim | Task-specific, scoped claims; benchmarks cannot be general | Scope claims to NL->EnergyPlus, not "BEM ability" |
| singh2025leaderboard | 2025 | arXiv | 10.48550/arXiv.2504.20879 | Arena leaderboard distortion | Undisclosed private testing (27 variants for one provider), asymmetric data access, silent deprecation; overfitting to arena | Limit submission attempts; disclose all runs |
| blum2015ladder | 2015 | ICML | 10.48550/arXiv.1502.04585 | Holdout overfitting via repeated submissions | Ladder: report only significant improvements; error ~ n^(-1/3) | Rounded/thresholded public scores on hidden test |
| dwork2015reusable | 2015 | Science | 10.48550/arXiv.1411.2664 | Adaptive reuse invalidates holdout | Differential-privacy-based reusable holdout | Support for private test + noise/limits |
| kiela2021dynabench | 2021 | NAACL | 10.48550/arXiv.2104.14337 | Static benchmarks saturate | Human-and-model-in-loop dynamic collection | Plan versioned refresh of cases |
| white2024livebench | 2024 | ICLR 2025 | 10.48550/arXiv.2406.19314 | Contamination, judge bias | Monthly new questions, objective auto-scoring; top models <70% | Fresh, objectively scored cases |
| jain2024livecodebench | 2024 | ICLR 2025 | 10.48550/arXiv.2403.07974 | Code-benchmark contamination | Release-date time-splits reveal drops after model cutoff | Date-stamp cases; report pre/post-cutoff |
| miller2024errorbars | 2024 | arXiv | 10.48550/arXiv.2411.00640 | Evals lack uncertainty | Report SEs/CIs, clustered SEs, paired differences, power analysis | Multiple runs, CIs, paired tests on leaderboard |
| gebru2021datasheets | 2021 | CACM | 10.1145/3458723 | Undocumented datasets | Standard question set for dataset documentation | Ship datasheet |
| mitchell2019modelcards | 2019 | FAT* | 10.1145/3287560.3287596 | Opaque model reporting | Model cards with disaggregated results | Submission metadata card per entry |
| pushkarna2022datacards | 2022 | FAccT | 10.48550/arXiv.2204.01075 | Documentation hard to use | Data Cards, layered structured docs | Layered docs for stakeholders |
| northcutt2021labelerrors | 2021 | NeurIPS D&B | 10.48550/arXiv.2103.14749 | Test-set label errors | Avg ~3.4% errors in 10 test sets; model ranking flips with correction | Audit reference models/ground truth; error-correct rounds |
| recht2019imagenetv2 | 2019 | ICML | 10.48550/arXiv.1902.10811 | Adaptive overfitting to test set | 11-14% accuracy drop on fresh replication, ranking mostly preserved | Hold back fresh test split |
| zheng2023judge | 2023 | NeurIPS D&B | 10.48550/arXiv.2306.05685 | Scalable evaluation | GPT-4 judge >80% agreement with humans; position/verbosity/self bias | Prefer simulation-based scoring; if judge used, calibrate |
| wang2023fairevaluators | 2023 | ACL 2024 | 10.48550/arXiv.2305.17926 | Judge order sensitivity | Rank flips by candidate order; calibration framework | Randomize order, human spot-check |
| xu2024contamsurvey | 2024 | arXiv | 10.48550/arXiv.2406.04244 | Contamination taxonomy | Survey of contamination and mitigation (dynamic, private) | Contamination plan |
| yang2023rephrased | 2023 | arXiv | 10.48550/arXiv.2311.04850 | n-gram decontamination insufficient | Rephrased test data beats n-gram detection; 13B models match GPT-4 on benchmarks | Do not rely on string-overlap checks |
| dodge2019showwork | 2019 | EMNLP | 10.48550/arXiv.1909.03004 | Compute/tuning budget unreported | Report expected validation performance vs. budget | Report prompting/agent budgets |
| pineau2020repro | 2020 | JMLR 2021 | 10.48550/arXiv.2003.12206 | Reproducibility | NeurIPS checklist program results | Reproducibility checklist for submissions |
| zhu2025abc | 2025 | arXiv | 10.48550/arXiv.2507.02825 | Agentic benchmark flaws | ABC checklist; flaws cause up to 100% relative misestimation | Checklist for task validity and outcome validity of executable tasks |
| biderman2024lessons | 2024 | arXiv | 10.48550/arXiv.2405.14782 | Irreproducible LM evals | Prompt/implementation sensitivity; shared harness | Release harness and fixed prompts |
| dror2018testing | - | - | unverified | Significance tests in NLP (ACL 2018) | not checked | https://aclanthology.org/P18-1128/ |
| vania2021irt | - | - | unverified | Saturation via IRT (ACL Findings 2021) | not checked | https://arxiv.org/abs/2106.00840 |

(23 verified papers kept; 2 listed as unverified, not counted. Total kept = 23.)

## 3. Synthesis: trustworthiness requirements
1. Define construct and scope claims narrowly (bean2025construct, raji2021everything, reuel2024betterbench).
2. Audit ground truth / test items for errors (northcutt2021labelerrors, zhu2025abc).
3. Contamination control: private/held-out test, date-stamped refreshable items, no reliance on n-gram checks (jain2024livecodebench, white2024livebench, kiela2021dynabench, xu2024contamsurvey, yang2023rephrased).
4. Leaderboard governance: submission limits, disclosure of all variants, thresholded score release (blum2015ladder, dwork2015reusable, singh2025leaderboard, recht2019imagenetv2).
5. Statistical rigor: CIs, paired tests, repeats (miller2024errorbars, dodge2019showwork).
6. Judge reliability: prefer objective scoring; calibrate and debias any LLM judge (zheng2023judge, wang2023fairevaluators).
7. Documentation and reproducibility: datasheet, cards, checklist, open harness (gebru2021datasheets, mitchell2019modelcards, pushkarna2022datacards, pineau2020repro, biderman2024lessons).
