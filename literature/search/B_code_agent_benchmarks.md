# B: Code / agent / scientific benchmarks as design precedents

## 1. Query log
|date|source|query|hits|kept|
|-|-|-|-|-|
|2026-11-07|arXiv|HumanEval Codex|1|1|
|2026-11-07|arXiv|code generation benchmark|8|8|
|2026-11-07|arXiv|SWE-bench|1|1|
|2026-11-07|arXiv|agent benchmark|6|6|
|2026-11-07|arXiv|scientific coding benchmark|3|2|
|2026-11-07|arXiv|Verilog benchmark LLM|2|2|
|2026-11-07|arXiv|text-to-CAD|1|1|
|2026-11-07|arXiv|OpenFOAM LLM|2|2|
|2026-11-07|arXiv|HELM BIG-bench|2|2|

DOIs: all are arXiv DOIs 10.48550/arXiv.<id>, existence checked via export.arxiv.org API (title matched). Journal/proceedings DOIs not checked (Crossref not used). Facts on size/scoring are from memory; spot-check before citing.

## 2. Kept papers (25)
|key|year|venue|DOI|task|scoring|ground truth|contamination|size|
|-|-|-|-|-|-|-|-|-|
|chen2021codex|2021|arXiv (Codex)|10.48550/arXiv.2107.03374|NL docstring->Python fn (HumanEval)|unit tests, pass@k (unbiased estimator)|164 hand-written problems|handwritten to avoid GitHub training data|164|
|austin2021mbpp|2021|arXiv|10.48550/arXiv.2108.07732|short NL->Python (MBPP, MathQA-Python)|3 asserts, pass rate|crowd-written + hand-verified subset|none|974 / 399 verified|
|hendrycks2021apps|2021|NeurIPS D&B|10.48550/arXiv.2105.09938|competition NL->program|test cases pass fraction|scraped sites, tests from solutions|train/test split only|10,000|
|lai2022ds1000|2022|ICML 2023|10.48550/arXiv.2211.11501|StackOverflow data-science code|execution tests + API-surface constraints|perturbed SO problems, expert tests|perturbation against memorisation|1,000|
|liu2023evalplus|2023|NeurIPS|10.48550/arXiv.2305.01210|augmented HumanEval/MBPP|extended tests (80x), pass@k|LLM+mutation test generation|n/a|164 x ~764 tests|
|du2023classeval|2023|arXiv|10.48550/arXiv.2308.01861|class-level code gen|unit tests, pass@k|manual crafting|manually written post-cutoff-ish|100 classes|
|zhuo2024bigcodebench|2024|ICLR 2025|10.48550/arXiv.2406.15877|library-heavy function composition|tests, calibrated pass@1|LLM-human synthesis, 5.6 tests/task avg|private-ish variants, Hard subset|1,140|
|jain2024livecodebench|2024|ICLR 2025|10.48550/arXiv.2403.07974|contest problems, repair, execution, test prediction|pass@k|scraped contests, tests generated|time-split by release date|~500-1000+ rolling|
|jimenez2023swebench|2023|ICLR 2024|10.48550/arXiv.2310.06770|repo issue->patch|FAIL_TO_PASS + PASS_TO_PASS tests in Docker|real PRs with test patches|time cutoff; Verified human-filtered subset (OpenAI blog, no DOI)|2,294|
|liu2023agentbench|2023|ICLR 2024|10.48550/arXiv.2308.03688|8 interactive environments|task success, weighted score|per-env scripts/human annotation|n/a|~1,000+ test|
|zhou2023webarena|2023|ICLR 2024|10.48550/arXiv.2307.13854|web tasks in self-hosted sites|functional programmatic checks of end state|human-written intents + evaluators|self-hosted reproducible|812|
|mialon2023gaia|2023|ICLR 2024|10.48550/arXiv.2311.12983|tool-use QA|exact-match short answer|human-authored, unambiguous answers|private test answers, leaderboard|466|
|xu2024agentcompany|2024|arXiv|10.48550/arXiv.2412.14161|simulated software-company tasks|checkpoint-based partial credit|expert-designed checkpoints/evaluators|self-hosted|175|
|chan2024mlebench|2024|ICLR 2025|10.48550/arXiv.2410.07095|Kaggle competitions|medal thresholds on held-out score|Kaggle leaderboards, own splits|contamination/plagiarism checks|75|
|pan2023mlagentbench|2023|ICML 2024|10.48550/arXiv.2310.03302|ML experimentation tasks|improvement over baseline|curated tasks|n/a|13|
|xie2024osworld|2024|NeurIPS D&B|10.48550/arXiv.2404.07972|computer-use tasks in real OS|per-task execution-based scripts|human-written tasks and checkers|VM reproducible|369|
|tian2024scicode|2024|NeurIPS D&B|10.48550/arXiv.2407.13168|scientific research code, multi-step subproblems|unit tests with numeric tolerance vs gold values|scientists write solutions + tests|held-out gold, no public solutions|80 problems / 338 subproblems|
|mirza2024chembench|2024|Nature Chem. 2025 (arXiv)|10.48550/arXiv.2404.01475|chemistry QA MCQ+open|exact/numeric match|curated + expert-written|kept corpus withheld part; human expert baseline|~2,700|
|liu2023verilogeval|2023|ICCAD|10.48550/arXiv.2309.07544|spec->Verilog module|simulation vs reference testbench, pass@k|HDLBits + LLM-described, verified|none|156|
|lu2023rtllm|2023|ASP-DAC 2024|10.48550/arXiv.2308.05345|design spec->RTL|syntax, functionality sim, PPA synth|hand-curated designs+testbenches|open|29-50 designs|
|hong2025text2cad|2024|NeurIPS D&B|10.48550/arXiv.2409.17106|text->sequential CAD model|geometry (Chamfer), command accuracy|DeepCAD + LLM-annotated prompts|dataset split|~170k models|
|feng2025openfoamgpt|2025|arXiv|10.48550/arXiv.2501.06327|NL->OpenFOAM case via RAG agent|case runs/ results vs reference|literature cases|n/a|small case set|
|yue2025foamagent|2025|arXiv|10.48550/arXiv.2505.04997|NL->OpenFOAM multi-agent|executability, success rate|benchmark of cases from tutorials|n/a|~100 cases|
|liang2022helm|2022|TMLR 2023|10.48550/arXiv.2211.09110|multi-scenario/multi-metric eval|accuracy, calibration, robustness, fairness, etc.|per scenario|transparent raw outputs|42 scenarios|
|srivastava2022bigbench|2022|TMLR 2023|10.48550/arXiv.2206.04615|community-contributed tasks|task metrics; canary GUID|200+ authors|canary string|204 tasks|

Unverified: SWE-bench Verified (https://openai.com/index/introducing-swe-bench-verified/), no DOI; FoamBench not found.

## 3. Synthesis
Transferable: execution as the primary oracle (HumanEval, SWE-bench, WebArena); hidden or augmented tests (EvalPlus, SciCode); numeric tolerance against expert gold values (SciCode); time-split and rolling releases (LiveCodeBench); canary strings and withheld answers (BIG-bench, GAIA); partial-credit checkpoints (TheAgentCompany); reproducible containers; hosted leaderboards with medal-style thresholds (MLE-bench). For BEM: score staged (parses, runs, no severe errors, then result metrics within tolerance of a reference). Different: no unit-test notion, since correct models are non-unique and many inputs are equivalent, so scoring must be on simulation outputs (EUI, loads, schedules) with tolerances and on geometry/zone fidelity. Ground truth needs expert models and weather files, runs are slow and version-dependent (EnergyPlus version pinning), and small task counts mean wide confidence intervals. Reference-free validity (energy balance, severe errors) can complement it. CFD/CAD benchmarks are the closest domain precedents but are immature, with small sizes and no contamination controls.
