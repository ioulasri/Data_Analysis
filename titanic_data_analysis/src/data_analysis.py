import pandas as pd

# Surival Rate Overview

df = pd.read_csv("../Cleaned_titanic_data.csv")

survival_data = df.groupby(["survived", "sex"]).size()

X = survival_data.loc[(0, "female")] # Did Not Survived
Y = survival_data.loc[(1, "female")] # Survived

A = survival_data.loc[(0, "male")] # Did Not Survived
B = survival_data.loc[(1, "male")] # Survived

print(f"Females who did not survive: {X}")
print(f"Females who survived: {Y}")
print()
print(f"Males who did not survive: {A}")
print(f"Males who survived: {B}")

male_survival_rate = round(B * 100 / (A + B), 2)
male_death_rate = round(100 - male_survival_rate, 2)

female_survival_rate = round(Y * 100 / (X + Y), 2)
female_death_rate = round(100 - female_survival_rate, 2)

print(f"Males survival rate is: {male_survival_rate}%")
print(f"Males Death rate is: {male_death_rate}%")
print()
print(f"Females survival rate is: {female_survival_rate}%")
print(f"Females Death rate is: {female_death_rate}%")