import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("../../imdb_top_1000.csv")

# Drop unnecessary columns
df = df.drop(["Poster_Link", "Certificate", "Meta_score"], axis=1)

df["Gross"] = df["Gross"].replace(",", "", regex=True)
df["Gross"] = pd.to_numeric(df["Gross"], errors="coerce")
df["Runtime"] = df["Runtime"].str.extract("(\d+)").astype(float)

sample_before = df[df["Gross"].isnull()].head(1)

# Separate rows with and without missing values
df_train = df[df["Gross"].notnull()].copy()
df_missing = df[df["Gross"].isnull()].copy()

features = ["No_of_Votes", "Runtime", "IMDB_Rating"]

df_train = df_train.dropna(subset=features)
df_missing = df_missing.dropna(subset=features)

X_train, X_test, y_train, y_test = train_test_split(df_train[features], df_train["Gross"], test_size=0.2, random_state=42)

model = RandomForestRegressor()
model.fit(X_train, y_train)

df_missing.loc[:, "Gross"] = model.predict(df_missing[features])

# Merge back into original DataFrame
df.loc[df["Gross"].isnull(), "Gross"] = df_missing["Gross"]

# Final check
print(df.isnull().sum())
print(df.shape)

sample_after = df[df.index == sample_before.index[0]]

cleaned_data = df.to_csv("movies.csv")