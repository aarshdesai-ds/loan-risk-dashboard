
# 📊 Extended EDA for Loan Default Dataset (Categorical Age Ranges Only)
# Author: Aarsh Desai

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Global configs
sns.set(style='whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)

# Load dataset
df = pd.read_csv('../data/loan_data.csv')

# Ensure the 'assets' folder exists
os.makedirs('../assets', exist_ok=True)

# Rename 'Status' column for clarity
df.rename(columns={'Status': 'loan_status'}, inplace=True)

# Define correct age order (ordinal categories)
age_order = ['<25', '25-34', '35-44', '45-54', '55-64', '65-74', '>74']

# ========== Quick Overview ==========
print(df.info())
print(df['age'].value_counts())
print(df['loan_status'].value_counts())

# ========== Plot 1: Loan Status Distribution ==========
sns.countplot(x='loan_status', data=df)
plt.title('Loan Status Distribution')
plt.savefig('../assets/plot01_loan_status.png')
plt.clf()

# ========== Plot 2: Age Group vs Loan Status ==========
sns.countplot(x='age', hue='loan_status', data=df, order=age_order)
plt.title('Loan Status by Age Group')
plt.xticks(rotation=45)
plt.savefig('../assets/plot02_age_group.png')
plt.clf()

# ========== Plot 3: Gender vs Loan Status ==========
sns.countplot(x='Gender', hue='loan_status', data=df)
plt.title('Loan Status by Gender')
plt.savefig('../assets/plot03_gender.png')
plt.clf()

# ========== Plot 4: Year vs Loan Status ==========
sns.countplot(x='year', hue='loan_status', data=df)
plt.title('Loan Status by Year')
plt.savefig('../assets/plot04_year.png')
plt.clf()

# ========== Plot 5: Loan Purpose vs Loan Status ==========
sns.countplot(y='loan_purpose', hue='loan_status', data=df)
plt.title('Loan Purpose vs Loan Status')
plt.savefig('../assets/plot05_loan_purpose.png')
plt.clf()

# ========== Plot 6: Loan Type vs Loan Status ==========
sns.countplot(y='loan_type', hue='loan_status', data=df)
plt.title('Loan Type vs Loan Status')
plt.savefig('../assets/plot06_loan_type.png')
plt.clf()

# ========== Plot 7: Credit Worthiness ==========
sns.countplot(y='Credit_Worthiness', hue='loan_status', data=df)
plt.title('Credit Worthiness vs Loan Status')
plt.savefig('../assets/plot07_creditworthiness.png')
plt.clf()

# ========== Plot 8: Credit Type ==========
sns.countplot(x='credit_type', hue='loan_status', data=df)
plt.title('Credit Type vs Loan Status')
plt.xticks(rotation=45)
plt.savefig('../assets/plot08_credit_type.png')
plt.clf()

# ========== Plot 9: Co-applicant Credit Type ==========
sns.countplot(x='co-applicant_credit_type', hue='loan_status', data=df)
plt.title('Co-applicant Credit Type vs Loan Status')
plt.savefig('../assets/plot09_coapp_credit_type.png')
plt.clf()

# ========== Plot 10: Business/Commercial Loans ==========
sns.countplot(x='business_or_commercial', hue='loan_status', data=df)
plt.title('Business/Commercial Loans vs Loan Status')
plt.savefig('../assets/plot10_business.png')
plt.clf()

# ========== Plot 11: Lump Sum Payment Option ==========
sns.countplot(x='lump_sum_payment', hue='loan_status', data=df)
plt.title('Lump Sum Payment vs Loan Status')
plt.savefig('../assets/plot11_lumpsum.png')
plt.clf()

# ========== Plot 12: Interest-Only Loans ==========
sns.countplot(x='interest_only', hue='loan_status', data=df)
plt.title('Interest-Only Loans vs Loan Status')
plt.savefig('../assets/plot12_interest_only.png')
plt.clf()

# ========== Plot 13: Neg Amortization ==========
sns.countplot(x='Neg_ammortization', hue='loan_status', data=df)
plt.title('Negative Amortization vs Loan Status')
plt.savefig('../assets/plot13_neg_amortization.png')
plt.clf()

# ========== Plot 14: Occupancy Type ==========
sns.countplot(x='occupancy_type', hue='loan_status', data=df)
plt.title('Occupancy Type vs Loan Status')
plt.savefig('../assets/plot14_occupancy.png')
plt.clf()

# ========== Plot 15: Region ==========
sns.countplot(y='Region', hue='loan_status', data=df)
plt.title('Loan Status by Region')
plt.savefig('../assets/plot15_region.png')
plt.clf()

# ========== Plot 16: Construction Type ==========
sns.countplot(y='construction_type', hue='loan_status', data=df)
plt.title('Construction Type vs Loan Status')
plt.savefig('../assets/plot16_construction.png')
plt.clf()

# ========== Plot 17: Submission of Application ==========
sns.countplot(x='submission_of_application', hue='loan_status', data=df)
plt.title('Submission Type vs Loan Status')
plt.savefig('../assets/plot17_submission.png')
plt.clf()

# ========== Plot 18: Property Value Boxplot ==========
sns.boxplot(x='loan_status', y='property_value', data=df)
plt.title('Property Value vs Loan Status')
plt.savefig('../assets/plot18_property_value.png')
plt.clf()

# ========== Plot 19: LTV Boxplot ==========
sns.boxplot(x='loan_status', y='LTV', data=df)
plt.title('Loan-to-Value Ratio vs Loan Status')
plt.savefig('../assets/plot19_ltv.png')
plt.clf()

# ========== Plot 20: Loan Amount Histogram ==========
sns.histplot(df['loan_amount'], bins=30, kde=True)
plt.title('Loan Amount Distribution')
plt.savefig('../assets/plot20_loan_amount_hist.png')
plt.clf()

# ========== Plot 21: Rate of Interest Boxplot ==========
sns.boxplot(x='loan_status', y='rate_of_interest', data=df)
plt.title('Interest Rate vs Loan Status')
plt.savefig('../assets/plot21_interest_rate.png')
plt.clf()

# ========== Plot 22: Upfront Charges Histogram ==========
sns.histplot(df['Upfront_charges'], bins=30, kde=True)
plt.title('Upfront Charges Distribution')
plt.savefig('../assets/plot22_upfront_charges.png')
plt.clf()

# ========== Plot 23: Term Boxplot ==========
sns.boxplot(x='loan_status', y='term', data=df)
plt.title('Loan Term vs Loan Status')
plt.savefig('../assets/plot23_term.png')
plt.clf()

# ========== Plot 24: Income Histogram ==========
sns.histplot(df['income'], bins=30, kde=True)
plt.title('Income Distribution')
plt.savefig('../assets/plot24_income_hist.png')
plt.clf()

# ========== Plot 25: Correlation Heatmap ==========
df_encoded = pd.get_dummies(df.select_dtypes(include='object'), drop_first=True)
df_combined = pd.concat([df.select_dtypes(include='number'), df_encoded], axis=1)
corr = df_combined.corr()

sns.heatmap(corr, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.savefig('../assets/plot25_correlation.png')
plt.clf()

# ========== Done ==========
print("✅ EDA complete. All plots saved to /assets/")
