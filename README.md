# Loan Default Risk Analysis Dashboard

### Python | Power BI | DAX | Power Query | Financial Risk Analytics

## Project Overview

Financial institutions face significant losses due to **loan defaults**. Identifying high-risk borrowers early can help banks improve approval strategies and reduce financial risk.

This project builds an **interactive Power BI dashboard** to analyze borrower characteristics, loan attributes, and repayment patterns in order to uncover **key drivers of loan default risk**.

The dashboard enables stakeholders to monitor loan performance and explore relationships between **income, credit score, loan amount, and borrower demographics**.

---

# Business Problem

Banks and lending institutions must answer critical questions:

* Which customers are **most likely to default on loans**?
* Do **credit scores or income levels** strongly influence loan repayment?
* Are there **regional patterns** in loan default risk?
* Which **loan purposes** are associated with higher default rates?

This dashboard provides insights that support **data-driven lending decisions**.

---

# Solution

Using **Power BI**, the dataset was transformed, modeled, and visualized to build a comprehensive **Loan Risk Analytics Dashboard**.

The solution includes:

* Data cleaning and transformation using **Power Query**
* Business metrics created using **DAX**
* Interactive visualizations for risk analysis
* Dynamic filtering using slicers for deeper exploration

---

# Data Preparation (Power Query)

The raw dataset required several preprocessing steps before analysis.

Key transformations include:
* null value imputation using python (median value safe approach)
* Data type correction and column formatting
* Mapping loan status values (0 → Paid, 1 → Default)
* Handling missing or inconsistent data
* Creating derived features such as **Age Groups**
* Preparing financial metrics for analysis

These steps ensured the dataset was **clean, structured, and analysis-ready**.

---

# Key DAX Measures

The following business metrics were created to evaluate loan performance.

### Total Loans

Counts the total number of loans issued.

### Total Defaults

Counts loans that resulted in default.

### Default Rate

Percentage of loans that defaulted.

default_rate = total_defaults / total_loans

### Average Loan Amount

Measures the typical loan size issued to borrowers.

### Average Interest Rate

Tracks lending cost across borrowers.

---

# Dashboard Features

## KPI Metrics

The dashboard highlights important lending indicators:

* Total Loans Issued
* Total Loan Defaults
* Default Rate
* Average Loan Amount

These KPIs provide a quick overview of **portfolio health**.

---

## Visual Analytics

### Loan Status Distribution

Shows the proportion of **paid vs defaulted loans**.

### Default Rate by Region

Identifies geographical areas with **higher lending risk**.

### Income vs Loan Amount (Scatter Plot)

Explores the relationship between **borrower income and loan size**, revealing potential risk clusters.

### Loan Amount by Loan Purpose

Analyzes which loan categories involve **larger financial exposure**.

### Credit Score Distribution

Shows borrower credit quality across the dataset.

---

# Interactive Filters

Users can explore the dashboard dynamically using slicers:

* Region
* Gender
* Risk Category
* Loan Purpose

These filters allow stakeholders to analyze **specific customer segments**.

---

# Key Insights

The dashboard helps uncover important patterns such as:

* Borrowers with **lower credit scores** showing higher default probability
* Certain **regions having higher loan default rates**
* A relationship between **income levels and loan size**
* Specific **loan purposes carrying greater financial risk**

These insights can support **better lending policies and risk management**.

---

# Technology Stack

| Tool               | Purpose                         |
| ------------------ | ------------------------------- |
| Power BI           | Dashboard creation              |
| Power Query        | Data cleaning & transformation  |
| DAX                | Business metrics & calculations |
| Data Visualization | Analytical storytelling         |
| Python             | Null value Treatment


# Skills Demonstrated

This project showcases the following analytical and technical skills:

* Data Cleaning & Transformation
* Financial Risk Analysis
* Data Modeling in Power BI
* DAX Measure Creation
* Interactive Dashboard Design
* Business Insight Generation

---

# Author

**Venkatesan**

M.Sc Physics | Aspiring Data Analyst

Skills:
 • Python • Power BI • Data Analytics • Data Visualization • SQL • Python

---

# Future Improvements

Potential enhancements include:

* Predictive modeling for **default probability**
* Credit risk scoring using machine learning
* Time-based loan performance analysis
* Advanced financial KPIs

---

# Conclusion

This project demonstrates how **business intelligence tools can transform raw financial data into actionable insights**, helping lending institutions better understand borrower behavior and manage loan risk.
