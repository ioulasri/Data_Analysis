import pandas as pd

import matplotlib.pyplot as plt

import numpy as np

import seaborn as sns


def plot_gender_survival():
    # Load the cleaned dataset

    df = pd.read_csv("../Cleaned_titanic_data.csv")



    # Group by survived and sex

    survival_data = df.groupby(["survived", "sex"]).size()



    # Extract survival counts

    X = survival_data.loc[(0, "female")]  # Females who did not survive

    Y = survival_data.loc[(1, "female")]  # Females who survived

    A = survival_data.loc[(0, "male")]    # Males who did not survive

    B = survival_data.loc[(1, "male")]    # Males who survived



    # Calculate survival rates

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



    # Create a bar plot using seaborn

    plt.figure(figsize=(8, 5))

    sns.barplot(x="Gender", y="Percentage", hue="Rate Type", data=df_visual, palette={"Survived": "green", "Did Not Survive": "red"})



    # Labels and title

    plt.xlabel("Gender")

    plt.ylabel("Percentage (%)")

    plt.title("Survival vs Death Rates by Gender on Titanic")



    # Show the plot
    plt.show()

