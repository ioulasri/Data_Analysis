import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def plot_gender_survival():
    df = pd.read_csv("../Cleaned_titanic_data.csv")

    survival_data = df.groupby(["survived", "sex"]).size()

    X = survival_data.loc[(0, "female")]
    Y = survival_data.loc[(1, "female")]
    A = survival_data.loc[(0, "male")]
    B = survival_data.loc[(1, "male")]

    male_survival_rate = round(B * 100 / (A + B), 2)

    male_death_rate = round(100 - male_survival_rate, 2)

    female_survival_rate = round(Y * 100 / (X + Y), 2)

    female_death_rate = round(100 - female_survival_rate, 2)

    print(f"Male survival rate: {male_survival_rate}%")
    print(f"Female survival rate: {female_survival_rate}%")

    print(f"Male death rate: {male_death_rate}%")
    print(f"Female death rate: {female_death_rate}%")

    data = {
        "Gender": ["Male", "Male", "Female", "Female"],
        "Rate Type": ["Survived", "Did Not Survive", "Survived", "Did Not Survive"],
        "Percentage": [male_survival_rate, male_death_rate, female_survival_rate, female_death_rate],
    }

    df_visual = pd.DataFrame(data)

    plt.figure(figsize=(8, 5))

    sns.barplot(x="Gender", y="Percentage", hue="Rate Type", data=df_visual, palette={"Survived": "green", "Did Not Survive": "red"})

    plt.xlabel("Gender")

    plt.ylabel("Percentage (%)")

    plt.title("Survival vs Death Rates by Gender on Titanic")

    plt.show()

