import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_fare_survival():
    df = pd.read_csv("../Cleaned_titanic_data.csv")
    df["fare_category"] = pd.cut(df["fare"], bins=[0, 10, 50, 600], labels=["Low", "Medium", "High"])
    survival_data = df.groupby(["survived", "fare_category"], observed=True).size()

    survivor_age = survival_data.xs(1, level="survived")
    non_survivor_age = survival_data.xs(0, level="survived")

    categorical_data = {
        "Low": [survivor_age.loc["Low"], non_survivor_age.loc["Low"]],
        "Medium": [survivor_age.loc["Medium"], non_survivor_age.loc["Medium"]],
        "High": [survivor_age.loc["High"], non_survivor_age.loc["High"]]
    }

    survival_rate = {
        "Low": categorical_data["Low"][0] / (categorical_data["Low"][0] + categorical_data["Low"][1]),
        "Medium": categorical_data["Medium"][0] / (categorical_data["Medium"][0] + categorical_data["Medium"][1]),
        "High": categorical_data["High"][0] / (categorical_data["High"][0] + categorical_data["High"][1])
    }

    a_data = {
        "Low": [survival_rate["Low"] * 100, 100 - survival_rate["Low"] * 100],
        "Medium": [survival_rate["Medium"] * 100, 100 - survival_rate["Medium"] * 100],
        "High": [survival_rate["High"] * 100, 100 - survival_rate["High"] * 100]
    }

    data = {
        "Fare category": ["Low", "Low", "Medium", "Medium", "High", "High"],
        "Rate Type": ["Survived", "Did Not Survive", "Survived", "Did Not Survive", "Survived", "Did Not Survive"],
        "Percentage": [a_data["Low"][0], a_data["Low"][1], 
                    a_data["Medium"][0], a_data["Medium"][1], 
                    a_data["High"][0], a_data["High"][1]]
    }

    sns.set_theme(style="whitegrid")

    df_visual = pd.DataFrame(data)

    plt.figure(figsize=(8, 5))
    sns.barplot(x="Fare category", y="Percentage", hue="Rate Type", data=df_visual, palette={"Survived": "green", "Did Not Survive": "red"})

    plt.xlabel("Fare Category")
    plt.ylabel("Percentage (%)")
    plt.title("Survival vs Death Rates by Fare price category on Titanic")

    plt.show()