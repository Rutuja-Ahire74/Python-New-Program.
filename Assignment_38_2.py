#2. Write a program to:
## Display total number of students in the dataset
## Count how many students Passed (FinalResult=1)
## Count how many students Failed (Final Result=0)

import pandas as pd

df = pd.read_csv("student_performance_ml.csv")

total_students = df.shape[0]
print("Total Number of Students: ", total_students)

passed_students = (df["FinalResult"] == 1).sum()
print("Number of Students Passed: ", passed_students)

failed_students = (df["FinalResult"] == 0).sum()
print("Number of Students Failed: ", failed_students)