select
    -- Identifiers / Surrogate keys
    row_number() over() as encounter_id,
    'K3' as source_dataset,

    -- Demographics
    CAST(Age AS INTEGER) as age,
    CASE 
        -- Documented age bands for reporting/grouping
        WHEN Age < 40 THEN '<40'
        WHEN Age BETWEEN 40 and 64 THEN '40-64'
        ELSE '65+' 
    end as age_band,
    TRIM(Gender) as sex,
    TRIM(Insurance_Type) as insurance_type,

    -- Clinical & Historical Features (Known at prediction time)
    CAST(Socioeconomic_Risk_Score AS INTEGER) as socioeconomic_risk_score,
    CAST(Previous_Admissions_6M AS INTEGER) as prior_admissions_6m,
    CAST(Previous_Readmissions_1Y AS INTEGER) as prior_readmissions_1y,
    CAST(Time_Since_Last_Discharge AS INTEGER) as time_since_last_discharge_days,
    CAST(Length_of_Stay AS NUMERIC) as length_of_stay_days,
    TRIM(Admission_Type) as admission_type,
    TRIM(Primary_Diagnosis_Group) as primary_dx_group,
    CAST(Comorbidity_Index AS INTEGER) as comorbidity_index,
    CAST(Chronic_Disease_Count AS INTEGER) as chronic_disease_count,
    CAST(ICU_Stay_Flag AS INTEGER) as icu_stay_flag,
    CAST(Severity_Score AS INTEGER) as severity_score,

    -- Labs & Vitals
    CAST(HbA1c_Level AS DOUBLE) as hba1c_level,
    CAST(Creatinine_Level AS DOUBLE) as creatinine_level,
    CAST(Hemoglobin_Level AS DOUBLE) as hemoglobin_level,
    CAST(Average_Systolic_BP AS INTEGER) as avg_systolic_bp,

    -- Medications
    CAST(Number_of_Medications AS INTEGER) as num_medications,
    CAST(Medication_Change_Count AS INTEGER) as medication_change_count,
    CAST(High_Risk_Medication_Flag AS INTEGER) as high_risk_med_flag,
    CAST(Medication_Adherence_Score AS DOUBLE) as medication_adherence_score,

    -- Operational / Follow-up
    CAST(Followup_Appointment_Scheduled AS INTEGER) as followup_appt_scheduled,
    TRIM(Discharge_Disposition) as discharge_disposition,

    -- Target Label (Readmission within 30 days)
    CAST(Readmitted_Within_30_Days AS INTEGER) as readmitted

from {{ source('main', 'raw_readmission') }}