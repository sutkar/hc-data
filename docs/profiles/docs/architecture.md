# Architecture & Design: Healthcare Metrics & Predictions Platform (MVP)

## 1. System Overview & Data Flow
The platform is built on a decoupled, multi-repo microservices architecture ensuring strict PHI protection, verifiable data governance, and zero-cost local reproducibility using DuckDB and dbt-core[cite: 1, 2].

## 2. Core Architectural Decisions (D1 - D8)
* **D1 & D2 (Warehouse & Transformation):** Replaced Snowflake and dbt Cloud with local **DuckDB + dbt-core** to maintain zero operating cost while preserving exact SQL and semantic modeling semantics.
* **D3 (MVP Use Case):** Focused on **30-Day Hospital Readmission Risk Prediction** using Kaggle Dataset K3 (18,000 rows, 0% missing values).
* **D4 (Secondary Use Case):** NSCLC survival analysis reserved as a secondary use case using prior R/Python artifacts.
* **D5 (Scale Strategy):** Heavy distributed compute (Spark/Ray) omitted from MVP; handled via local DuckDB batch efficiency.
* **D6 & D7 (AI Safety & Chat):** The LLM never touches raw patient rows or executes arbitrary SQL. It interacts exclusively via allow-listed, parameterized Python functions (`get_kpi`, `drill_down`, `get_explanation`), receiving only aggregated metrics or de-identified values[cite: 1].
* **D8 (Multi-Repo Structure):** Maintained strict repository separation (`hc-data`, `hc-ml`, `hc-chat`) sharing a single synchronized DuckDB warehouse file (`warehouse/hc.duckdb`)[cite: 1].