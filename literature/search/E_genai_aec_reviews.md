# E. GenAI in AEC / building engineering: reviews and non-BEM model generation

CAVEAT: DOIs, titles, years, venues were taken directly from Crossref search results (so they exist in Crossref). Full texts were NOT read; evaluation and limitation columns are "not checked" unless inferable from the title. Search was cut short by Crossref rate limiting; no web search or arXiv queries were run (below the 20-30 target). Follow-up reading needed.

## 1. Query log (Crossref, filter from 2022-01-01, journal-article, top 8 each)
| date | source | query | hits | kept |
|---|---|---|---|---|
| 2026-11-07 | Crossref | large language models built environment review | 8 | 0 |
| 2026-11-07 | Crossref | LLM building energy modeling EnergyPlus | 8 | 2 |
| 2026-11-07 | Crossref | generative floor plan layout | 8 | 0 (peripheral) |
| 2026-11-07 | Crossref | LLM structural engineering analysis model generation | 8 | 0 |
| 2026-11-07 | Crossref | benchmark large language models construction engineering | 8 | 2 |
| 2026-11-07 | Crossref | generative AI architecture engineering construction review | 8 | 3 |
| 2026-11-07 | Crossref | LLM building code compliance checking | 8 | 3 |
| 2026-11-07 | Crossref | LLM BIM IFC generation | 8 | 0 |
| 2026-11-07 | Crossref | large language model HVAC control sequence | 8 | 2 |
| 2026-11-07 | Crossref | LLM building energy review | 8 | 2 |
| 2026-11-07 | Crossref | large language models building energy modeling review | 8 | 6 |
| 2026-11-07 | Crossref | LLM agent BIM model generation | 8 | 1 |
| 2026-11-07 | Crossref | LLM structural design automation | 8 | 1 |
Failed (rate-limited/no JSON, not rerun): ChatGPT automated building energy model; text-to-BIM large language model; LLM automated code compliance checking building. OpenAlex: 0 uses.

## 2. Kept papers (all DOIs returned by Crossref search; evaluation = not checked)
| key | year | venue | DOI | type | model/task | evaluation used | limitations / benchmark call |
|---|---|---|---|---|---|---|---|
| zhang2024advancing | 2024 | Energy and Buildings | 10.1016/j.enbuild.2024.114788 | method/case studies | BEM with LLMs | not checked | not checked |
| jiang2024eplusllm | 2024 | Applied Energy | 10.1016/j.apenergy.2024.123431 | method | EnergyPlus IDF generation (EPlus-LLM) | not checked | not checked |
| zhang2025automatic | 2025 | Energy and Buildings | 10.1016/j.enbuild.2024.115116 | method | BEM development + debugging via agents | not checked | not checked |
| unverified-author2025finetune | 2025 | Automation in Construction | 10.1016/j.autcon.2025.106223 | method | fine-tuned LLM for automated BEM | not checked | not checked |
| unverified-author2025prompt | 2025 | Energy | 10.1016/j.energy.2025.134548 | method | prompt engineering for automated BEM | not checked | not checked |
| unverified-author2026kbmas | 2026 | Energy and Buildings | 10.1016/j.enbuild.2026.117688 | method | knowledge-based multi-agent BEM | not checked | not checked |
| unverified-author2025energymcp | 2025 | SoftwareX | 10.1016/j.softx.2025.102367 | tool | EnergyPlus-MCP server | not checked | not checked |
| unverified-author2026routing | 2026 | Innovation Energy | 10.59717/j.xinn-energy.2026.100194 | method | LLM selection for agentic BEM | not checked | not checked |
| unverified-author2025opportunities | 2025 | Renew. Sustain. Energy Rev. | 10.1016/j.rser.2025.115558 | review | LLMs in building energy sector | not checked | not checked |
| unverified-author2026survey | 2026 | Energy and Buildings | 10.1016/j.enbuild.2025.116800 | review | LLMs in building energy applications | not checked | not checked |
| unverified-author2026hbi | 2026 | Applied Energy | 10.1016/j.apenergy.2025.127079 | review | human-building interaction in EMS | not checked | not checked |
| unverified-author2026construction | 2026 | Automation in Construction | 10.1016/j.autcon.2026.107101 | benchmark | LLMs for construction engineering and management | benchmark (details not checked) | not checked |
| unverified-author2026mllm | 2026 | Adv. Eng. Informatics | 10.1016/j.aei.2025.103909 | review | multimodal LLMs in construction | not checked | not checked |
| unverified-author2024genaiaec | 2024 | Architecture (MDPI) | 10.3390/architecture4040046 | review | GenAI in AEC | not checked | not checked |
| unverified-author2025genaiaeco | 2025 | Buildings | 10.3390/buildings15132270 | review | GenAI in AECO | not checked | not checked |
| unverified-author2026archstruct | 2026 | J. Intelligent Construction | 10.26599/jic.2026.9180126 | review | GenAI architectural/structural design | not checked | not checked |
| unverified-author2026sociotech | 2026 | Adv. Eng. Informatics | 10.1016/j.aei.2026.104392 | review/assessment | GenAI integration in AEC | not checked | not checked |
| unverified-author2024prompt | 2024 | Automation in Construction | 10.1016/j.autcon.2024.105817 | method | prompt-based code-to-rule transformation | not checked | not checked |
| unverified-author2025llmbim | 2025 | Electronics | 10.3390/electronics14112146 | method | LLM code compliance in BIM | not checked | not checked |
| unverified-author2026bimcode | 2026 | Adv. Eng. Informatics | 10.1016/j.aei.2026.104735 | method | BIM code extraction + compliance | not checked | not checked |
| unverified-author2025bimcoord | 2025 | Automation in Construction | 10.1016/j.autcon.2025.106563 | method | multi-agent BIM coordinator | not checked | not checked |
| unverified-author2026hvaccode | 2026 | Buildings | 10.3390/buildings16091722 | method | HVAC control code generation | not checked | not checked |
| unverified-author2026autompc | 2026 | Energy and Buildings | 10.1016/j.enbuild.2026.118025 | method | automated MPC development | not checked | not checked |
| unverified-author2026cadstruct | 2026 | Automation in Construction | 10.1016/j.autcon.2026.107030 | method | CAD-structural analysis via MCP | not checked | not checked |

(Keys with "unverified-author" mean first author not recorded; rename after reading. 24 kept.)

## 3. Synthesis (limited: metadata only)
From titles and venues, building-engineering GenAI work is dominated by method papers with case-study validation; most appear to evaluate on small, self-built test sets with ad hoc success criteria (code executes, simulation runs, output compared with a reference). One construction-management LLM benchmark exists (Automation in Construction 2026), but I found no benchmark for BEM/IDF generation, IFC generation, or control-sequence generation in this pass. Reviews cover applications and opportunities broadly. Recurring gaps (to be confirmed by full-text reading): no shared public task sets, inconsistent metrics (syntactic validity vs simulation-result fidelity), limited model-version reporting, and weak coverage of structural, CFD/daylight, and Guideline 36 tasks. Not yet searched: web/arXiv, floor plan LLM work, ASHRAE G36, IFC generation (rate-limited).
