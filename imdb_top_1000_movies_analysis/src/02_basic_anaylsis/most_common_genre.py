import pandas as pd

df = pd.read_csv("../data/movies.csv")

genre_column = df["Genre"]

print("The most commun genre in this dataset is: ", genre_column.value_counts().idxmax())