import pandas as pd

# Load dataset
df = pd.read_csv("../data/movies.csv")

# Movies count over the years
year_data = df["Released_Year"].value_counts().sort_index()

def movies_count():
    print("\n0-1 Number of movies released each year from dataset:\n")
    for year, value in year_data.items():
        print(f"Year: {year}, Count: {value}")

# Year with the most movies released
def max_released():
    print("\n0-2 Year with most released movies:\n")
    year = year_data.idxmax()
    movies_count = year_data.max()
    print(f"{movies_count} movies released in {year}")

# Average rating for each year
rating_year = df.groupby("Released_Year")["IMDB_Rating"].mean()

def average_ratings():
    print("\n0-3 Average IMDB Rating per Year:\n")
    for year, avg_rating in rating_year.items():
        print(f"Year: {year}, Average IMDB Rating: {avg_rating:.2f}")

while True:
    print("\nSelect an option:")
    print("1 - Number of movies released each year")
    print("2 - Year with the most movies released")
    print("3 - Average IMDB rating per year")
    print("0 - Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        movies_count()
    elif choice == "2":
        max_released()
    elif choice == "3":
        average_ratings()
    elif choice == "0":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 0.")
