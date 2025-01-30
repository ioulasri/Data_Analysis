import pandas as pd

import matplotlib.pyplot as plt

import numpy as np

import seaborn as sns

def plot_class_survival():
	df = pd.read_csv("../Cleaned_titanic_data.csv")

	survival_data = df.groupby(["survived", "pclass"]).size()

	X = survival_data.loc[(1, 1)]
	Y = survival_data.loc[(1, 2)]
	Z = survival_data.loc[(1, 3)]

	A = survival_data.loc[(0, 1)]
	B = survival_data.loc[(0, 2)]
	C = survival_data.loc[(0, 3)]

	fclass_survival_rate = round(X * 100 / (X + A), 2)
	sclass_survival_rate = round(Y * 100 / (Y + B), 2)
	tclass_survival_rate = round(Z * 100 / (Z + C), 2)

	fclass_death_rate = round(100 - fclass_survival_rate, 2)
	sclass_death_rate = round(100 - sclass_survival_rate, 2)
	tclass_death_rate = round(100 - tclass_survival_rate, 2)

	print(f"1st class survival rate: {fclass_survival_rate}%")
	print(f"2nd class survival rate: {sclass_survival_rate}%")
	print(f"3rd class survival rate: {tclass_survival_rate}%")

	print(f"1st class death rate: {fclass_death_rate}%")
	print(f"2nd class death rate: {sclass_death_rate}%")
	print(f"3rd class death rate: {tclass_death_rate}%")

	data = {
		"Class": ["1st class", "1st class", "2nd class", "2nd class", "3rd class", "3rd class"],
		"Rate Type": ["Survived", "Did Not Survive", "Survived", "Did Not Survive", "Survived", "Did Not Survive"],
		"Percentage": [fclass_survival_rate, fclass_death_rate, sclass_survival_rate, sclass_death_rate, tclass_survival_rate, tclass_death_rate]
	}

	sns.set_theme(style="whitegrid")

	df_visual = pd.DataFrame(data)

	plt.figure(figsize=(10, 6))

	sns.barplot(x="Class", y="Percentage", hue="Rate Type", data=df_visual, palette={"Survived": "green", "Did Not Survive": "red"})

	plt.xlabel("Class")
	plt.ylabel("Percentage (%)")
	plt.title("Survival vs Death Rates by Class on Titanic")


	plt.show()