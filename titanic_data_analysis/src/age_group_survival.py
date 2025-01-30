import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("../Cleaned_titanic_data.csv")


df["age_group"] = pd.cut(df["age"], bins=[0, 12, 25, 50, 100], labels=["Child", "Young Adult", "Middle-aged", "Senior"])


survival_data = df.groupby(["survived", "age_group"], observed=True).size()


survivor_age = survival_data.xs(1, level="survived")
non_survivor_age = survival_data.xs(0, level="survived")


categorical_data = {
    "Child": [survivor_age.loc["Child"], non_survivor_age.loc["Child"]],
    "Young Adult": [survivor_age.loc["Young Adult"], non_survivor_age.loc["Young Adult"]],
    "Middle-aged": [survivor_age.loc["Middle-aged"], non_survivor_age.loc["Middle-aged"]],
    "Senior": [survivor_age.loc["Senior"], non_survivor_age.loc["Senior"]]
}


survival_rate = {
    "Child": categorical_data["Child"][0] / (categorical_data["Child"][0] + categorical_data["Child"][1]),
    "Young Adult": categorical_data["Young Adult"][0] / (categorical_data["Young Adult"][0] + categorical_data["Young Adult"][1]),
    "Middle-aged": categorical_data["Middle-aged"][0] / (categorical_data["Middle-aged"][0] + categorical_data["Middle-aged"][1]),
    "Senior": categorical_data["Senior"][0] / (categorical_data["Senior"][0] + categorical_data["Senior"][1])
}


a_data = {
    "Child": [survival_rate["Child"] * 100, 100 - survival_rate["Child"] * 100],
    "Young Adult": [survival_rate["Young Adult"] * 100, 100 - survival_rate["Young Adult"] * 100],
    "Middle-aged": [survival_rate["Middle-aged"] * 100, 100 - survival_rate["Middle-aged"] * 100],
    "Senior": [survival_rate["Senior"] * 100, 100 - survival_rate["Senior"] * 100]
}


data = {
    "Age Group": ["Child", "Child", "Young Adult", "Young Adult", "Middle-aged", "Middle-aged", "Senior", "Senior"],
    "Rate Type": ["Survived", "Did Not Survive", "Survived", "Did Not Survive", "Survived", "Did Not Survive", "Survived", "Did Not Survive"],
    "Percentage": [a_data["Child"][0], a_data["Child"][1], 
                   a_data["Young Adult"][0], a_data["Young Adult"][1], 
                   a_data["Middle-aged"][0], a_data["Middle-aged"][1], 
                   a_data["Senior"][0], a_data["Senior"][1]]
}


sns.set_theme(style="whitegrid")

df_visual = pd.DataFrame(data)

plt.figure(figsize=(10, 6))
sns.barplot(x="Age Group", y="Percentage", hue="Rate Type", data=df_visual, palette={"Survived": "green", "Did Not Survive": "red"})

plt.xlabel("Age Group")
plt.ylabel("Percentage (%)")
plt.title("Survival vs Death Rates by Age Group on Titanic")

plt.show()
