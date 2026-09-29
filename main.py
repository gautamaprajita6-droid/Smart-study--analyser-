#Smart study analyser
import numpy as np

print("========================================")
print("     SMART STUDY PRODUCTIVITY ANALYZER")
print("========================================")

name = input("Enter your name: ")
days = int(input("Enter number of days you want to analyze: "))

study_hours = []

for i in range(days):
    hours = float(input(f"Enter study hours for Day {i + 1}: "))
    study_hours.append(hours)

hours_array = np.array(study_hours)

total_hours = np.sum(hours_array)
average_hours = np.mean(hours_array)
maximum_hours = np.max(hours_array)
minimum_hours = np.min(hours_array)

most_productive_day = np.argmax(hours_array) + 1

if average_hours >= 6:
    performance = "Excellent"
elif average_hours >= 4:
    performance = "Good"
elif average_hours >= 2:
    performance = "Average"
else:
    performance = "Needs Improvement"

print("\n========================================")
print("             STUDY ANALYSIS")
print("========================================")

print("Student Name:", name)
print("Total Study Hours:", total_hours)
print("Average Study Hours:", round(average_hours, 2))
print("Maximum Study Hours:", maximum_hours)
print("Minimum Study Hours:", minimum_hours)
print("Most Productive Day:", most_productive_day)
print("Overall Performance:", performance)

print("========================================")