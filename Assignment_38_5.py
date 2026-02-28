# Based on the dataset values, analyze whether:
## Higher StudyHours increase the chance of passing.
## Higher Attendance improves FinalResult.
## Write your observations in 4-5 lines.

import pandas as pd

df = pd.read_csv("student_performance_ml.csv")

result = df.groupby("FinalResult")[["StudyHours","Attendance"]].mean()

print(result)
