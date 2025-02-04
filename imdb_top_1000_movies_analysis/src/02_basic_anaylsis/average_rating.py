import pandas as pd

df = pd.read_csv("../data/movies.csv")
average_rating = df["IMDB_Rating"].mean()
print("The average rating of all movies is: ", round(average_rating, 2))