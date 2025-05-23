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

```bash
# Clone the repository
git clone https://github.com/aarshdesai-ds/loan-risk-dashboard.git
cd loan-risk-dashboard

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app/streamlit_app.py
