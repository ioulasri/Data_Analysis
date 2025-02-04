import pandas as pd

df = pd.read_csv("../data/movies.csv")

# Function to calculate the average rating of all movies
def average_rating():
    avg_rating = df["IMDB_Rating"].mean()
    print(f"\nThe average IMDB rating of all movies is: {round(avg_rating, 2)}")

# Function to convert minutes to hours and minutes format
def minutes_to_hours(time):
    hours = time // 60  # Corrected hours calculation
    mins = time % 60
    return f"{hours}h and {mins}m"

# Function to get the longest runtime
def longest_runtime():
    max_runtime = df["Runtime"].max()
    print(f"\nThe longest runtime in this dataset is: {minutes_to_hours(max_runtime)}")

# Function to get the most common genre
def most_common_genre():
    genre_column = df["Genre"]
    most_common = genre_column.value_counts().idxmax()
    print(f"\nThe most common genre in this dataset is: {most_common}")

while True:
    print("\nSelect an option:")
    print("1 - Average IMDB rating of all movies")
    print("2 - Longest runtime in the dataset")
    print("3 - Most common genre in the dataset")
    print("0 - Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        average_rating()
    elif choice == "2":
        longest_runtime()
    elif choice == "3":
        most_common_genre()
    elif choice == "0":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 0.")
