import pandas as pd


df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv")

# 1- check for missing value to clean the data

# missing_values_count = df.isnull().sum()
# print(f"Missing values for each column: \n{missing_values_count}")

print(f"data before cleaning had: {df.shape}")

# 1-1 Fixing the age missing data by replacing NULL with the median age

age_median = df["age"].median()

df["age"] = df["age"].fillna(age_median)

# 1-2 Fixing the categorical missing data with the most common data for the given column

df["embark_town"] = df["embark_town"].fillna(df["embark_town"].mode()[0])
df["embarked"] = df["embarked"].fillna(df["embarked"].mode()[0])

# 1-3 Removing the deck category for having so many missing data

df.drop(columns=["deck"], inplace=True)

# Check if there is any more missing data

# missing_values_count = df.isnull().sum()
# print(f"Missing values for each column: \n{missing_values_count}")

print(f"data after cleaning has: {df.shape}")

df.to_csv("Cleaned_titanic_data.csv")