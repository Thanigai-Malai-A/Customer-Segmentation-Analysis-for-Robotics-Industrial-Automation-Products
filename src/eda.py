from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
df=pd.read_csv(ROOT/"outputs"/"cleaned_customer_data.csv")
OUT=ROOT/"outputs"/"figures"; OUT.mkdir(parents=True,exist_ok=True)
plt.figure(figsize=(8,5)); plt.hist(df["Annual_Spend"],bins=30); plt.title("Annual Spend Distribution"); plt.xlabel("Annual Spend (INR)"); plt.ylabel("Customers"); plt.tight_layout(); plt.savefig(OUT/"01_annual_spend_distribution.png",dpi=160); plt.close()
counts=df["Product_Category"].value_counts()
plt.figure(figsize=(9,5)); plt.bar(counts.index,counts.values); plt.title("Customers by Product Category"); plt.xticks(rotation=30,ha="right"); plt.ylabel("Customers"); plt.tight_layout(); plt.savefig(OUT/"02_customers_by_category.png",dpi=160); plt.close()
counts=df["Region"].value_counts()
plt.figure(figsize=(9,5)); plt.bar(counts.index,counts.values); plt.title("Customers by Region"); plt.xticks(rotation=30,ha="right"); plt.ylabel("Customers"); plt.tight_layout(); plt.savefig(OUT/"03_customers_by_region.png",dpi=160); plt.close()
print("EDA charts created.")
