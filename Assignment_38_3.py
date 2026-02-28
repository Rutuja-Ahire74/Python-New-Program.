# Using pandas functions, calculate and display:
## Average StudyHours
## Average Attendance
## Maximum Previous Score
## Minimum SleepHours

import pandas as pd

df = pd.read_csv("student_performance_ml.csv")

average_study_hours = df["StudyHours"].mean()
print("Average Study Hours: ",average_study_hours)

average_attendance = df["Attendance"].mean()
print("Average Attendance: ",average_attendance)

maximum_previous_score = df["PreviousScore"].max()
print("Maximum Previous Score: ",maximum_previous_score)

minimum_sleepHrs = df["SleepHours"].min()
print("Minimum Sleep Hours: ", minimum_sleepHrs)