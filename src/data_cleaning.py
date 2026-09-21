from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
df=pd.read_csv(ROOT/"data"/"robotics_customer_data.csv")
print("Rows:",len(df))
print("Duplicate rows:",df.duplicated().sum())
print("Missing values before cleaning:\n",df.isna().sum())
df["Age"]=df["Age"].fillna(df["Age"].median())
for c in ["Industry","Company_Size"]:
    df[c]=df[c].fillna(df[c].mode()[0])
df["Average_Order_Value"]=df["Annual_Spend"]/df["Number_of_Orders"]
df["Purchase_Frequency"]=df["Number_of_Orders"]/12
df.to_csv(ROOT/"outputs"/"cleaned_customer_data.csv",index=False)
print("Cleaned data saved.")
