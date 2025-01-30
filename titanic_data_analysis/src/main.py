import gender_survival
import class_survival
import age_group_survival

def main():
    while True:
        print("\n📊 Titanic Survival Analysis Menu:")
        print("1️⃣ - Gender-Based Survival")
        print("2️⃣ - Class-Based Survival")
        print("3️⃣ - Age Group Survival")
        print("4️⃣ - Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            gender_survival.plot_gender_survival()
        elif choice == "2":
            class_survival.plot_class_survival()
        elif choice == "3":
            age_group_survival.plot_age_group_survival()
        elif choice == "4":
            print("Exiting the program. Goodbye! 👋")
            break
        else:
            print("Invalid choice, please enter a number between 1-4.")


main()