# %%
import pandas as pd

# %%
df = pd.read_csv("C:/Users/venka/Downloads/loan_default.csv")

# %%
df

# %%
df['age'].unique()

# %%
df.isnull().sum()

# %%
df["loan_limit"].unique()

# %%
df["loan_limit"]=df["loan_limit"].fillna("blank")

# %%
df["loan_limit"].head(50)

# %%
df["loan_limit"].unique()

# %%
df["loan_limit"].isnull().sum()

# %%
df['loan_purpose'].unique()

# %%
df['loan_purpose'].value_counts()

# %%
df['loan_purpose']=df['loan_purpose'].fillna('not mentioned')

# %%
df['loan_purpose'].unique()

# %%
df['rate_of_interest'] = df['rate_of_interest'].fillna(df['rate_of_interest'].median())
df['Interest_rate_spread'] = df['Interest_rate_spread'].fillna(df['Interest_rate_spread'].median())

# %%
df['Upfront_charges'] = df['Upfront_charges'].fillna(0)

# %%
df['income'] = df['income'].fillna(df['income'].median())


# %%
df['property_value'] = df.groupby('Region')['property_value'].transform(lambda x: x.fillna(x.median()))

# %%
df.dropna(subset=['term', 'Neg_ammortization'], inplace=True)

# %%
df['LTV'] = df['LTV'].fillna(df['LTV'].median())
df['dtir1'] = df['dtir1'].fillna(df['dtir1'].median())


# %%
df['age'] = df['age'].fillna("Unknown")
df['submission_of_application'] = df['submission_of_application'].fillna("Unknown")

# %%
df.dropna(subset=['approv_in_adv'], inplace=True)


# %%
df.isnull().sum()

# %%
df.to_csv("C:/Users/venka/Downloads/loan_defaults_newcln.csv", index=False)


