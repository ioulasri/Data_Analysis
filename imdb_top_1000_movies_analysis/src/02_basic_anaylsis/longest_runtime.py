import pandas as pd

df = pd.read_csv("../data/movies.csv")

def minutes_to_hours(time):
    hours = time % 60
    time -= hours * 60
    mins = time % 60
    return f"{round(hours)}h and {round(mins)}m"

runtime_column = df["Runtime"]

print("The longest runtime in this dataset is:", minutes_to_hours(runtime_column.max()))