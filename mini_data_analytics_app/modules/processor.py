
import pandas as pd
import numpy as np

def clean_data(df):
    df = df.copy()
    df['Purchase_Amount'] = pd.to_numeric(df['Purchase_Amount'], errors='coerce')
    if 'Age' in df.columns:
        df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
        median_age = int(df['Age'].median(skipna=True))
        df['Age'] = df['Age'].fillna(median_age)
    df = df.dropna(subset=['Purchase_Amount'])
    df['Purchase_Date'] = pd.to_datetime(df['Purchase_Date'], errors='coerce')
    return df

def categorize_spenders(df):
    df = df.copy()
    q1 = df['Purchase_Amount'].quantile(0.33)
    q2 = df['Purchase_Amount'].quantile(0.66)
    def tier(a):
        if a <= q1: return 'Low'
        if a <= q2: return 'Medium'
        return 'High'
    df['Spender_Tier'] = df['Purchase_Amount'].apply(tier)
    return df

def mean_purchase_by_category(df):
    return df.groupby('Product_Category')['Purchase_Amount'].mean().reset_index()

class CustomerAnalysis:
    def __init__(self, df):
        self.df = df.copy()
    def total_sales(self):
        return self.df['Purchase_Amount'].sum()
    def sales_by_category(self):
        return self.df.groupby('Product_Category')['Purchase_Amount'].sum().reset_index()
    def age_distribution(self):
        return self.df['Age'].describe()
