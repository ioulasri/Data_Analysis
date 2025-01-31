import gender_survival
import class_survival
import age_group_survival
import fare_survival
import os
import time

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("\n📊 Titanic Survival Analysis Menu:")
    print("🔹 1️⃣ - 👨‍🦰👩 Gender-Based Survival")
    print("🔹 2️⃣ - 🏷️🎩 Class-Based Survival")
    print("🔹 3️⃣ - 👶🧑‍🦳 Age Group Survival")
    print("🔹 4️⃣ - 💰💵 Fare Category Survival")
    print("🔹 5️⃣ - 👨‍👩‍👧‍👦 Family Size & Survival")
    print("🔹 6️⃣ - 🌍🛳️ Embarkation Port & Survival")
    print("🔹 7️⃣ - 📊 Feature Correlation Heatmap")
    print("🔹 8️⃣ - 🎲 Random Passenger Survival Prediction")
    print("❌ 9️⃣ - 🔴 Quit")

    choice = input("👉 Enter your choice (1-9): ")

    if choice == "9":
        print("👋 Exiting the program. Have a great day! 🚀")
        break
    elif choice == "1":
        print("🔍 Running Gender-Based Survival Analysis...")
        gender_survival.plot_gender_survival()
    elif choice == "2":
        print("🔍 Running Class-Based Survival Analysis...")
        class_survival.plot_class_survival()
    elif choice == "3":
        print("🔍 Running Age Group Survival Analysis...")
        age_group_survival.plot_age_group_survival()
    elif choice == "4":
        print("🔍 Running Fare Category Survival Analysis...")
        fare_survival.plot_fare_survival()
    elif choice == "5":
        print("🔍 Running Family Size & Survival Analysis...")
        print("Coming soon...")
        time.sleep(3)
    elif choice == "6":
        print("🔍 Running Embarkation Port & Survival Analysis...")
        print("Coming soon...")
        time.sleep(3)
    elif choice == "7":
        print("🔍 Running Feature Correlation Heatmap...")
        print("Coming soon...")
        time.sleep(3)
    elif choice == "8":
        print("🔍 Running Random Passenger Survival Prediction...")
        print("Coming soon...")
        time.sleep(3)
    else:
        print("⚠️ Invalid choice! Please enter a number between 1-9.")
        time.sleep(1)
