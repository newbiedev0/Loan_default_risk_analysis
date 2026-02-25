# %%
import pandas as pd

# %%
import matplotlib.pyplot as plt

# %%
import numpy as np

# %%
import seaborn as sns

# %%
df=pd.read_csv("C:/Users/venka/Downloads/loan_default.csv")

# %%
df

# %%
df.describe()

# %%
df.columns

# %%
df.dtypes

# %%
df.isnull().sum()

# %%

plt.figure(figsize=(10, 6))
sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap='viridis')
plt.title("Missing Data Heatmap")
plt.show()

# %%
df.dtypes

# %%
cols_to_drop = ['rate_of_interest', 'Interest_rate_spread', 'Upfront_charges']
df = df.drop(columns=cols_to_drop, errors='ignore')

# %%
cat_cols = df.select_dtypes(include=['object']).columns
df[cat_cols] = df[cat_cols].fillna("Not Provided")

# %%
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# %%
df.isnull().sum()

# %%

df['term'] = df['term'].fillna(df['term'].mode()[0])


cols_to_fix = ['property_value', 'income', 'LTV', 'dtir1']

for col in cols_to_fix:
    median_value = df[col].median()
    df[col] = df[col].fillna(median_value)

print(df[cols_to_fix + ['term']].isnull().sum())

# %%
df.isnull().sum()

# %%
df.to_csv("C:/Users/venka/Downloads/loan_dfalt_cln.csv")

# %%
df.columns

# %%



