import pandas as pd

df = pd.read_csv("../data/movies.csv")

year_data = df["Released_Year"].value_counts()

# movies count over the years

print("0-1 Number of movies released each year from dataset: ")

for year, value in year_data.items():
    print(f"Year: {year}, Count: {value}")

# Year with the most movies released:

print("0-2 Year with most released movies: ")

year = year_data.index[0]
movies_count = year_data.iloc[0]

print(f"{movies_count} movies released in {year}")