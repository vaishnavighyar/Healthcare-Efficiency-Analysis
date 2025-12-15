# Healthcare-Efficiency-Analysis

**Aim:** To analyze 200K+ Medicare records to analyze Hospital Efficiency and suggest Optimization.

**Dataset used:** 200K+ Medical records from Centers for Medicare & Medicaid Services (**CMS**)

**KPIs:**
ALOS, readmission risk, revenue per organization, net earnings, discharge volume, resource utilization

**Dashboard**:

<img width="801" height="458" alt="Image" src="https://github.com/user-attachments/assets/d91a3d33-8ec3-4e26-a8cb-8018e47c2172" />

**Process:**

1. Imported the dataset into MySQL using the Python+SQL Connector method, as the dataset was too large to be directly imported into the MySQL server.
2. Defined the KPIs.
3. Perform data validation and cleaning.
4. Calculated KPIs by querying the dataset.
5. Exported the results to Power BI and built the above dashboard to communicate findings.

**Key Findings:**

- Analyzed 200K+ Medicare records identifying 5x variance in Average Length of Stay; 
  Recommended process improvements with **$500M+** annual cost savings potential (25% reduction).

- Conducted financial analysis of **$4B** revenue with $755M net (18.9% margin); 
  identified the top 5 hospitals generating 85% revenue, and proposed margin optimization to 25%.

- Performed readmission analysis across **32 facilities**; discovered 5 hospitals 
  driving 69% high-risk cases, designed interventions projected to save **$100M** annually.

- Built **6-KPI dashboard** (ALOS, readmission, revenue, utilization); automated ETL 
  pipeline reducing data prep time by 75% (8 hours → 2 hours) for monthly reporting.

Thank you.
