# Use value_counts() to analyze the distribution of FinalResult.
# calculate the percentage of Pass and Fail students.
# Is the dataset balanced? Justify your answer.

import pandas as pd

df = pd.read_csv("student_performance_ml.csv")

result =df["FinalResult"].value_counts()

print("Distribution of FinalResult:")
print(result)

result_prcnt = df["FinalResult"].value_counts(normalize=True) * 100

print("\nPercentage Distribution:")
print(result_prcnt)
