# Project Report
## Customer Segmentation Analysis for Robotics & Industrial Automation Products

### 1. Introduction
This project demonstrates customer analytics and unsupervised machine learning in a robotics and industrial automation context.

### 2. Problem Statement
Customers can differ in spending, order frequency, recency and product preferences. Segmentation helps organize customers into behaviorally similar groups.

### 3. Objective
Segment synthetic automation-equipment customers based on behavior and relevant demographic/business characteristics.

### 4. Dataset
The project uses 360 synthetic customer records. The dataset is educational and does not represent real company customers.

### 5. Technology
Python, Pandas, NumPy, Scikit-learn, Matplotlib, Plotly and Streamlit.

### 6. Data Cleaning
Missing age values were filled with the median. Missing categorical values were filled with the mode. Average order value and purchase frequency were recalculated from order and spending fields.

### 7. Exploratory Data Analysis
The project explores annual spending, orders, product categories and regional distribution.

### 8. Clustering
K-Means was used after standardizing five purchasing-behavior variables:
- Annual Spend
- Number of Orders
- Average Order Value
- Recency Days
- Purchase Frequency

### 9. Elbow Method
Inertia was calculated for K=2 through K=8. Four clusters were used for the final beginner-friendly segmentation model.

### 10. Cluster Summary
```text
 Cluster  Customers  Avg_Annual_Spend  Avg_Orders  Avg_Order_Value  Avg_Recency_Days  Avg_Purchase_Frequency Top_Product_Category          Top_Industry Top_Region                         Segment
       0        151     174611.316093    4.304636     42461.105468         39.801325                0.358720              Sensors Warehouse & Logistics       Pune         Active Growth Customers
       1         56     215841.945357    4.910714     46453.939212        120.392857                0.409226              Control   General Engineering  Bengaluru          Low-Activity Customers
       2         51     541260.557843    3.392157    169562.907165         48.568627                0.282680             Robotics            Automotive    Chennai High-Value Automation Customers
       3        102     356978.232157    8.421569     44356.797192         51.598039                0.701797              Sensors           Electronics       Pune      Frequent Automation Buyers
```

### 11. Key Insights
1. High-Value Automation Customers has the highest average annual spend at approximately INR 541,261.
2. Frequent Automation Buyers has the highest average order frequency at approximately 8.4 orders per customer.
3. Active Growth Customers is the largest segment with 151 customers.
4. Robotics is the most common product category.
5. Chennai has the largest number of customers.
6. Segment-level differences can support targeted product recommendations and customer engagement strategies.
### 12. Business Applications
The segmentation can support targeted product recommendations, customer prioritization, service plans and regional sales analysis.

### 13. Limitations
- Synthetic dataset
- Educational use only
- K-Means results depend on feature selection and scaling
- Four clusters are used for a clear demonstration

### 14. Future Scope
- Use real CRM/ERP data
- Compare additional clustering algorithms
- Add customer lifetime value
- Add churn prediction
- Connect to a live database

### 15. Conclusion
The project demonstrates a complete workflow from data preparation and exploratory analysis to K-Means segmentation, visualization and an interactive dashboard.

**Synthetic-data statement:** The dataset used in this project is synthetic and created for educational purposes.
