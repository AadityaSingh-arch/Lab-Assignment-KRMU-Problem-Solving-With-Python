# Daily Calorie Tracker
# Author: Your Name
# Date: YYYY-MM-DD
# Project: Daily Calorie Tracker CLI

# --- Task 1: Welcome Message ---
print("===================================")
print(" Welcome to the Daily Calorie Tracker ")
print("===================================")
print("This program helps you log meals, track calories,")
print("and check if you are within your daily limit.\n")

# --- Task 2: Input & Data Collection ---
meals = []       # to store meal names
calories = []    # to store calorie values

num_meals = int(input("How many meals do you want to log today? "))

for i in range(num_meals):
    meal = input("Enter the name of meal " + str(i+1) + ": ")
    cal = int(input("Enter calories for " + meal + ": "))
    meals.append(meal)
    calories.append(cal)

# --- Task 3: Calculations ---
total_calories = sum(calories)
average_calories = total_calories / len(calories)

daily_limit = int(input("\nEnter your daily calorie limit: "))

# --- Task 4: Limit Warning ---
if total_calories > daily_limit:
    status = "WARNING: You exceeded your daily limit!"
else:
    status = "Good job! You are within your daily limit."

# --- Task 5: Neatly Formatted Output ---
print("\nYour Calorie Report")
print("---------------------------")
print("Meal\t\tCalories")
print("---------------------------")
for i in range(len(meals)):
    print(meals[i], "\t\t", calories[i])
print("---------------------------")
print("Total:\t\t", total_calories)
print("Average:\t", round(average_calories, 2))
print(status)
print("---------------------------")

# --- Task 6: Bonus (Save to File) ---
choice = input("\nDo you want to save this report to a file? (yes/no): ")

if choice.lower() == "yes":
    file = open("calorie_log.txt", "a")   # open in append mode
    file.write("Calorie Report\n")
    file.write("---------------------------\n")
    file.write("Meal\tCalories\n")
    for i in range(len(meals)):
        file.write(meals[i] + "\t" + str(calories[i]) + "\n")
    file.write("---------------------------\n")
    file.write("Total:\t" + str(total_calories) + "\n")
    file.write("Average:\t" + str(round(average_calories, 2)) + "\n")
    file.write(status + "\n\n")
    file.close()
    print("Report saved to 'calorie_log.txt'")
