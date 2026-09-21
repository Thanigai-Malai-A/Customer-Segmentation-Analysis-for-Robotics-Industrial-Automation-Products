from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
ROOT=Path(__file__).resolve().parents[1]
df=pd.read_csv(ROOT/"outputs"/"cleaned_customer_data.csv")
features=["Annual_Spend","Number_of_Orders","Average_Order_Value","Recency_Days","Purchase_Frequency"]
X=StandardScaler().fit_transform(df[features])
ks=range(2,9); inertias=[]
for k in ks:
    inertias.append(KMeans(n_clusters=k,random_state=42,n_init=20).fit(X).inertia_)
OUT=ROOT/"outputs"; FIG=OUT/"figures"; FIG.mkdir(parents=True,exist_ok=True)
plt.figure(figsize=(8,5)); plt.plot(list(ks),inertias,marker="o"); plt.title("Elbow Method for K-Means"); plt.xlabel("Number of Clusters (K)"); plt.ylabel("Inertia"); plt.tight_layout(); plt.savefig(FIG/"04_elbow_method.png",dpi=160); plt.close()
model=KMeans(n_clusters=4,random_state=42,n_init=20)
df["Cluster"]=model.fit_predict(X)
df.to_csv(OUT/"segmented_customers.csv",index=False)
plt.figure(figsize=(9,6)); plt.scatter(df["Annual_Spend"],df["Number_of_Orders"],c=df["Cluster"],cmap="viridis",alpha=.75); plt.title("Customer Segments: Annual Spend vs Number of Orders"); plt.xlabel("Annual Spend (INR)"); plt.ylabel("Number of Orders"); plt.colorbar(label="Cluster"); plt.tight_layout(); plt.savefig(FIG/"05_customer_clusters.png",dpi=160); plt.close()
print("K-Means completed with 4 clusters.")
