# 📊 Loan Default Risk Dashboard

This project explores loan default risk using a comprehensive **exploratory data analysis (EDA)** pipeline and an interactive **Streamlit dashboard**.  
The dashboard enables users to explore how demographic and loan-related factors such as **age range**, **region**, **gender**, and **loan type** influence default behavior.

---

## 📦 Dataset

- **Source**: Public loan application dataset (cleaned)
- **Target**: `loan_status` (0 = Fully Paid, 1 = Defaulted)  
- **Features**:
  - Demographics: Gender, Region, Age Group (categorical ranges)
  - Loan Details: Type, Purpose, Amount, Term
  - Financials: Interest Rate, Property Value, LTV, Income
  - Application Info: Submission type, Occupancy, Credit Worthiness

🗂 File: `data/loan_data.csv`

---

## 🧠 EDA & Visualization

### 🧹 Data Preparation
- Renamed `Status` to `loan_status`
- Converted `age` to **ordered categorical ranges** (`<25`, `25–34`, `35–44`, …)
- Handled missing values and cleaned numeric columns

### 📊 Visualizations (25+ Plots)
- Countplots: Age group, Region, Loan Type, Credit Worthiness, Occupancy
- Histograms: Loan Amount, Upfront Charges, Income
- Boxplots: Interest Rate, Term, Property Value, LTV
- Correlation heatmap of numeric + encoded categorical features

---

## 💻 Streamlit Dashboard

> A fully interactive local app to explore default trends with live filtering.

### 🧾 Features
- Sidebar filters: Gender, Region, Loan Type
- Visual panels:
  - 🎯 Default by Age Group
  - 🏘️ Region vs Default
  - 🧾 Loan Purpose vs Default
  - 💼 Credit Worthiness Breakdown
  - 💰 Loan Amount Distribution
  - 🏠 Occupancy Type vs Default

---

## 🚀 How to Run Locally


1. Clone the repository
`git clone https://github.com/aarshdesai-ds/loan-risk-dashboard.git`

2. Install dependencies
`pip install -r requirements.txt`

3. Run the Streamlit app
`streamlit run app/streamlit_app.py`


# ✅ Key Takeaways

This project combines exploratory data analysis with an interactive Streamlit dashboard to help users investigate the risk factors behind loan default behavior. Below are the major insights and outcomes:

---

## 🔍 Demographic and Financial Insights

- Default rates vary significantly across **age groups**, **regions**, and **loan purposes**.
- Younger applicants (<25) and certain regions show **higher default tendencies**, indicating potential demographic risk factors.
- **Credit worthiness** and **loan purpose** are key determinants of repayment behavior.

---

## 📊 Rich, Visual-First Exploration

- The dashboard includes **25+ visualizations** to help users spot trends and anomalies at a glance.
- Plots such as boxplots, countplots, and histograms provide a **multi-dimensional view** of loan risk.
- A **correlation heatmap** reveals relationships between numeric and encoded categorical features.

---

## 🧹 Clean, Structured Data Pipeline

- Age transformed into **ordered categorical bins** enables better cohort analysis.
- Numeric fields (e.g., Loan Amount, Interest Rate) cleaned and standardized for visualization and filtering.
- Missing values handled robustly to maintain data quality throughout the dashboard.

---

## 🖥️ Streamlit Dashboard for Stakeholders

- Users can interactively filter data by **gender**, **region**, **loan type**, and more.
- Visual panels are tailored to business questions, including:
  - 📈 Default by Age Group  
  - 🏘️ Region vs Default Rate  
  - 💼 Credit Worthiness Impact  
  - 🧾 Loan Purpose vs Default  
  - 💰 Loan Amount Distribution  
- Helps **non-technical stakeholders** derive insights quickly and clearly.

---

## 📈 Conclusion

The Loan Default Risk Dashboard offers a **powerful, visual way** to analyze default trends across multiple factors.  
With a clean EDA pipeline and intuitive Streamlit interface, it enables organizations to **identify risk patterns**, **optimize lending criteria**, and **communicate findings effectively**.

