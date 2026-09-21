from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"outputs"; FIG=OUT/"figures"
df=pd.read_csv(OUT/"segmented_customers.csv")
summary=df.groupby("Cluster").agg(Customers=("Customer_ID","count"),Avg_Annual_Spend=("Annual_Spend","mean"),Avg_Orders=("Number_of_Orders","mean"),Avg_Order_Value=("Average_Order_Value","mean"),Avg_Recency_Days=("Recency_Days","mean"),Avg_Purchase_Frequency=("Purchase_Frequency","mean")).reset_index()
def modev(s): 
    m=s.mode(); return m.iloc[0] if len(m) else "N/A"
summary["Top_Product_Category"]=summary["Cluster"].map(df.groupby("Cluster")["Product_Category"].agg(modev))
summary["Top_Industry"]=summary["Cluster"].map(df.groupby("Cluster")["Industry"].agg(modev))
summary["Top_Region"]=summary["Cluster"].map(df.groupby("Cluster")["Region"].agg(modev))
spend_order=summary.sort_values("Avg_Annual_Spend",ascending=False)["Cluster"].tolist()
order_order=summary.sort_values("Avg_Orders",ascending=False)["Cluster"].tolist()
recent_order=summary.sort_values("Avg_Recency_Days",ascending=True)["Cluster"].tolist()
labels={}
for c in summary["Cluster"]:
    labels[c] = ("High-Value Automation Customers" if c==spend_order[0] else
                 "Frequent Automation Buyers" if c==order_order[0] else
                 "Active Growth Customers" if c==recent_order[0] else
                 "Low-Activity Customers")
summary["Segment"]=summary["Cluster"].map(labels); df["Segment"]=df["Cluster"].map(labels)
summary.to_csv(OUT/"cluster_summary.csv",index=False); df.to_csv(OUT/"segmented_customers.csv",index=False)
# Charts
counts=df["Segment"].value_counts()
plt.figure(figsize=(9,5)); plt.bar(counts.index,counts.values); plt.title("Customer Distribution by Segment"); plt.xticks(rotation=25,ha="right"); plt.ylabel("Customers"); plt.tight_layout(); plt.savefig(FIG/"06_segment_distribution.png",dpi=160); plt.close()
g=df.groupby("Segment")["Annual_Spend"].mean().sort_values(ascending=False)
plt.figure(figsize=(9,5)); plt.barh(g.index,g.values); plt.title("Average Annual Spend by Segment"); plt.xlabel("INR"); plt.tight_layout(); plt.savefig(FIG/"07_spend_by_segment.png",dpi=160); plt.close()
g=df.groupby("Segment")["Number_of_Orders"].mean().sort_values(ascending=False)
plt.figure(figsize=(9,5)); plt.barh(g.index,g.values); plt.title("Average Orders by Segment"); plt.xlabel("Orders"); plt.tight_layout(); plt.savefig(FIG/"08_orders_by_segment.png",dpi=160); plt.close()
pivot=pd.crosstab(df["Segment"],df["Product_Category"])
pivot.plot(kind="bar",stacked=True,figsize=(10,6)); plt.title("Product Category Preference by Segment"); plt.xticks(rotation=25,ha="right"); plt.tight_layout(); plt.savefig(FIG/"09_category_by_segment.png",dpi=160); plt.close()
g=df.groupby("Segment")["Average_Order_Value"].mean().sort_values(ascending=False)
plt.figure(figsize=(9,5)); plt.barh(g.index,g.values); plt.title("Average Order Value by Segment"); plt.xlabel("INR"); plt.tight_layout(); plt.savefig(FIG/"10_aov_by_segment.png",dpi=160); plt.close()
plt.figure(figsize=(9,6))
for seg,grp in df.groupby("Segment"):
    plt.scatter(grp["Recency_Days"],grp["Annual_Spend"],label=seg,alpha=.7)
plt.title("Recency vs Annual Spend"); plt.xlabel("Recency (Days)"); plt.ylabel("Annual Spend (INR)"); plt.legend(fontsize=8); plt.tight_layout(); plt.savefig(FIG/"11_recency_vs_spend.png",dpi=160); plt.close()
top_spend=summary.sort_values("Avg_Annual_Spend",ascending=False).iloc[0]; top_orders=summary.sort_values("Avg_Orders",ascending=False).iloc[0]; largest=summary.sort_values("Customers",ascending=False).iloc[0]
insights=[
f"{top_spend['Segment']} has the highest average annual spend at approximately INR {top_spend['Avg_Annual_Spend']:,.0f}.",
f"{top_orders['Segment']} has the highest average order frequency at approximately {top_orders['Avg_Orders']:.1f} orders per customer.",
f"{largest['Segment']} is the largest customer segment, containing {int(largest['Customers'])} of {len(df)} customers.",
f"{df['Product_Category'].value_counts().idxmax()} is the most common product category in the generated customer base.",
f"{df['Region'].value_counts().idxmax()} has the largest number of customers in the generated dataset.",
"Segment-level differences can support targeted product recommendations and customer engagement strategies."
]
(OUT/"business_insights.txt").write_text("\n".join(f"{i}. {x}" for i,x in enumerate(insights,1)),encoding="utf-8")
print(summary.to_string(index=False))
