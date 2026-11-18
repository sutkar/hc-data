# hc-data: Data Engineering & Semantic Layer

## Purpose
Manages raw ingestion, dbt staging models (`stg_readmission`), and canonical semantic marts (`sv_encounters`) for hospital readmission analytics[cite: 1].

## Setup & Installation (Windows PowerShell)
1. Open PowerShell and navigate to `hc-data/hc_data_proj`.
2. Create and activate a virtual environment:
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1