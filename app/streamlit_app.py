# streamlit_app.py

# 📊 Interactive Loan Default Risk Dashboard (EDA-Only Version)

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set Streamlit layout
st.set_page_config(page_title="Loan Default Risk Dashboard", layout="wide")

# =============================
# 📥 Load Dataset
# =============================
@st.cache_data
def load_data():
    df = pd.read_csv('../data/loan_data.csv')
    df.rename(columns={'Status': 'loan_status'}, inplace=True)
    
    # Ensure 'age' is treated as an ordered categorical variable
    age_order = ['<25', '25-34', '35-44', '45-54', '55-64', '65-74', '>74']
    df['age'] = pd.Categorical(df['age'], categories=age_order, ordered=True)
    
    return df

df = load_data()

# =============================
# 🧭 Sidebar Filters
# =============================
st.sidebar.header("🔍 Filter the Data")

selected_gender = st.sidebar.multiselect(
    "Select Gender:", options=df['Gender'].unique(), default=list(df['Gender'].unique())
)

selected_region = st.sidebar.multiselect(
    "Select Region:", options=df['Region'].unique(), default=list(df['Region'].unique())
)

selected_loan_type = st.sidebar.multiselect(
    "Select Loan Type:", options=df['loan_type'].unique(), default=list(df['loan_type'].unique())
)

# Apply filters
filtered_df = df[
    (df['Gender'].isin(selected_gender)) &
    (df['Region'].isin(selected_region)) &
    (df['loan_type'].isin(selected_loan_type))
]

# =============================
# 📊 Dashboard Title
# =============================
st.title("📉 Loan Default Risk Dashboard")

# =============================
# 📈 Default Distribution by Age Group
# =============================
st.markdown("### 🎯 Default Distribution by Age Group")
fig1, ax1 = plt.subplots()
sns.countplot(data=filtered_df, x='age', hue='loan_status', order=['<25', '25-34', '35-44', '45-54', '55-64', '65-74', '>74'], ax=ax1)
plt.xticks(rotation=45)
st.pyplot(fig1)

# =============================
# 🏘️ Default Distribution by Region
# =============================
st.markdown("### 🏘️ Default Distribution by Region")
fig2, ax2 = plt.subplots()
sns.countplot(data=filtered_df, y='Region', hue='loan_status', ax=ax2)
st.pyplot(fig2)

# =============================
# 🧾 Loan Purpose vs Loan Status
# =============================
st.markdown("### 🧾 Loan Purpose vs Loan Status")
fig3, ax3 = plt.subplots()
sns.countplot(data=filtered_df, y='loan_purpose', hue='loan_status', ax=ax3)
st.pyplot(fig3)

# =============================
# 💼 Credit Worthiness vs Loan Status
# =============================
st.markdown("### 💼 Credit Worthiness vs Loan Status")
fig4, ax4 = plt.subplots()
sns.countplot(data=filtered_df, y='Credit_Worthiness', hue='loan_status', ax=ax4)
st.pyplot(fig4)

# =============================
# 💰 Loan Amount Distribution
# =============================
st.markdown("### 💰 Loan Amount Distribution")
fig5, ax5 = plt.subplots()
sns.histplot(data=filtered_df, x='loan_amount', bins=30, kde=True, ax=ax5)
st.pyplot(fig5)

# =============================
# 🏠 Occupancy Type vs Loan Status
# =============================
st.markdown("### 🏠 Loan Status by Occupancy Type")
fig6, ax6 = plt.subplots()
sns.countplot(data=filtered_df, x='occupancy_type', hue='loan_status', ax=ax6)
plt.xticks(rotation=45)
st.pyplot(fig6)

# =============================
# ✅ Done
# =============================
st.success("Dashboard loaded successfully.")
