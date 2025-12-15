import pandas as pd
import mysql.connector
import os

# File path
csv_path = r"C:\Users\vaish\OneDrive\Documents\Portfolio projects\SQL Healthcare analysis\by_provider.CSV"

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="your_username",       # 🔁 Replace with your MySQL username
    password="your_password",   # 🔁 Replace with your MySQL password
    database="your_database"    # 🔁 Replace with your DB name (e.g., healthcare_analysis)
)

cursor = conn.cursor()

# Read in chunks
chunksize = 1000
df_iter = pd.read_csv(csv_path, chunksize=chunksize)

for chunk in df_iter:
    for _, row in chunk.iterrows():
        values = tuple(row)
        sql = """
            INSERT INTO healthcare_provider (
                Rndrng_Prvdr_CCN, Rndrng_Prvdr_Org_Name, Rndrng_Prvdr_St,
                Rndrng_Prvdr_City, Rndrng_Prvdr_Zip5, Rndrng_Prvdr_State_Abrvtn,
                Rndrng_Prvdr_State_FIPS, Rndrng_Prvdr_RUCA, Rndrng_Prvdr_RUCA_Desc,
                Tot_Benes, Tot_Submtd_Cvrd_Chrg, Tot_Pymt_Amt, Tot_Mdcr_Pymt_Amt,
                Tot_Dschrgs, Tot_Cvrd_Days, Tot_Days, Bene_Avg_Age,
                Bene_Age_LT_65_Cnt, Bene_Age_65_74_Cnt, Bene_Age_75_84_Cnt, Bene_Age_GT_84_Cnt,
                Bene_Feml_Cnt, Bene_Male_Cnt, Bene_Race_Wht_Cnt, Bene_Race_Black_Cnt,
                Bene_Race_API_Cnt, Bene_Race_Hspnc_Cnt, Bene_Race_NatInd_Cnt, Bene_Race_Othr_Cnt,
                Bene_Dual_Cnt, Bene_Ndual_Cnt, CC_BH_ADHD_OthCD_Pct, CC_BH_Alcohol_Drug_Pct,
                CC_BH_Tobacco_Pct, CC_BH_Alz_Dem_Pct, CC_BH_Anxiety_Pct, CC_BH_Bipolar_Pct,
                CC_BH_Mood_Pct, CC_BH_Depress_Pct, CC_BH_PD_Pct, CC_BH_PTSD_Pct,
                CC_BH_Schizo_Pct, CC_PH_Asthma_Pct, CC_PH_Afib_Pct, CC_PH_Cancer_Pct,
                CC_PH_CKD_Pct, CC_PH_COPD_Pct, CC_PH_Diabetes_Pct, CC_PH_HF_NonIHD_Pct,
                CC_PH_Hyperlipid_Pct, CC_PH_Hypertension_Pct, CC_PH_IschemicHeart_Pct,
                CC_PH_Osteoporosis_Pct, CC_PH_Parkinson_Pct, CC_PH_Arthritis_Pct,
                CC_PH_Stroke_TIA_Pct, Bene_Avg_Risk_Scre
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, values)
    conn.commit()

print("✅ Data import complete.")
cursor.close()
conn.close()
