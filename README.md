# Customer Segmentation Analysis for Robotics & Industrial Automation Products

## Overview
A beginner-friendly customer segmentation project using Python and K-Means clustering for a robotics and industrial automation business scenario.

> **Important:** The dataset is synthetic/illustrative and was created for educational/internship purposes. It does not represent real company customers.

## Task Coverage
- Customer segmentation using behavior and demographics
- K-Means clustering with scikit-learn
- Purchase-pattern and preference analysis
- Visualizations of customer segments and characteristics
- Interactive Streamlit dashboard

## Dataset
**360 synthetic customer records** covering Indian regions, industrial sectors and robotics/automation products.

Features include:
`Customer_ID`, `Age`, `Gender`, `Region`, `Company_Size`, `Industry`, `Product_Category`, `Annual_Spend`, `Number_of_Orders`, `Average_Order_Value`, `Recency_Days`, `Purchase_Frequency`, `Preferred_Product`, `Customer_Tenure_Months`.

## Tools
Python, Pandas, NumPy, Scikit-learn, Matplotlib, Plotly and Streamlit.

## Methodology
1. Generate/load synthetic data
2. Check missing values and duplicates
3. Clean data and recalculate derived behavior metrics
4. Explore spending, orders, categories and regions
5. Scale clustering variables with StandardScaler
6. Inspect K values using the Elbow Method
7. Apply K-Means with 4 clusters
8. Profile each cluster
9. Visualize the results
10. Explore the results through the Streamlit dashboard

## Cluster Summary
```text
 Cluster  Customers  Avg_Annual_Spend  Avg_Orders  Avg_Order_Value  Avg_Recency_Days  Avg_Purchase_Frequency Top_Product_Category          Top_Industry Top_Region                         Segment
       0        151     174611.316093    4.304636     42461.105468         39.801325                0.358720              Sensors Warehouse & Logistics       Pune         Active Growth Customers
       1         56     215841.945357    4.910714     46453.939212        120.392857                0.409226              Control   General Engineering  Bengaluru          Low-Activity Customers
       2         51     541260.557843    3.392157    169562.907165         48.568627                0.282680             Robotics            Automotive    Chennai High-Value Automation Customers
       3        102     356978.232157    8.421569     44356.797192         51.598039                0.701797              Sensors           Electronics       Pune      Frequent Automation Buyers
```

## Key Insights
1. High-Value Automation Customers has the highest average annual spend at approximately INR 541,261.
2. Frequent Automation Buyers has the highest average order frequency at approximately 8.4 orders per customer.
3. Active Growth Customers is the largest segment with 151 customers.
4. Robotics is the most common product category.
5. Chennai has the largest number of customers.
6. Segment-level differences can support targeted product recommendations and customer engagement strategies.
## Run on Windows
```powershell
python --version
cd customer-segmentation-robotics
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python src/generate_dataset.py
python src/data_cleaning.py
python src/eda.py
python src/clustering.py
python src/analysis.py
streamlit run dashboard/app.py
```

## Project Structure
```text
customer-segmentation-robotics/
├── data/
├── notebooks/
├── src/
├── dashboard/
├── outputs/
├── PROJECT_REPORT.md
├── README.md
├── requirements.txt
└── .gitignore
```
