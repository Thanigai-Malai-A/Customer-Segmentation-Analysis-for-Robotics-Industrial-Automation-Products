from pathlib import Path
import pandas as pd
import plotly.express as px
import streamlit as st
ROOT=Path(__file__).resolve().parents[1]
df=pd.read_csv(ROOT/"outputs"/"segmented_customers.csv")
st.set_page_config(page_title="Robotics Customer Segmentation",page_icon="🤖",layout="wide")
st.title("🤖 Robotics & Industrial Automation Customer Segmentation Dashboard")
st.caption("Educational project using a synthetic dataset.")
with st.sidebar:
    st.header("Filters")
    region=st.multiselect("Region",sorted(df.Region.unique()))
    industry=st.multiselect("Industry",sorted(df.Industry.unique()))
    category=st.multiselect("Product Category",sorted(df.Product_Category.unique()))
    size=st.multiselect("Company Size",sorted(df.Company_Size.unique()))
    segment=st.multiselect("Customer Segment",sorted(df.Segment.unique()))
f=df.copy()
if region: f=f[f.Region.isin(region)]
if industry: f=f[f.Industry.isin(industry)]
if category: f=f[f.Product_Category.isin(category)]
if size: f=f[f.Company_Size.isin(size)]
if segment: f=f[f.Segment.isin(segment)]
a,b,c,d,e=st.columns(5)
a.metric("Total Customers",f"{len(f):,}")
b.metric("Total Annual Spend",f"₹{f.Annual_Spend.sum():,.0f}")
c.metric("Average Customer Spend",f"₹{f.Annual_Spend.mean():,.0f}")
d.metric("Average Orders",f"{f.Number_of_Orders.mean():.1f}")
e.metric("Number of Segments",f.Segment.nunique())
l,r=st.columns(2)
with l:
    x=f.Segment.value_counts().reset_index(); x.columns=["Segment","Customers"]
    st.plotly_chart(px.bar(x,x="Segment",y="Customers",title="Customer Segment Distribution"),use_container_width=True)
with r:
    x=f.groupby("Segment",as_index=False).Annual_Spend.mean()
    st.plotly_chart(px.bar(x,x="Segment",y="Annual_Spend",title="Average Annual Spend by Segment"),use_container_width=True)
l,r=st.columns(2)
with l:
    st.plotly_chart(px.scatter(f,x="Annual_Spend",y="Number_of_Orders",color="Segment",hover_data=["Customer_ID","Region","Industry","Product_Category"],title="Annual Spend vs Number of Orders"),use_container_width=True)
with r:
    x=f.Product_Category.value_counts().reset_index(); x.columns=["Product_Category","Customers"]
    st.plotly_chart(px.bar(x,x="Product_Category",y="Customers",title="Customers by Product Category"),use_container_width=True)
st.subheader("Segment Characteristics")
s=f.groupby("Segment").agg(Customers=("Customer_ID","count"),Avg_Annual_Spend=("Annual_Spend","mean"),Avg_Orders=("Number_of_Orders","mean"),Avg_Order_Value=("Average_Order_Value","mean"),Avg_Recency_Days=("Recency_Days","mean")).reset_index()
st.dataframe(s,use_container_width=True)
st.subheader("Customer Data")
st.dataframe(f,use_container_width=True)
