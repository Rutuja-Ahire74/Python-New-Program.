# 1. Write a Python program to load the file student_performance_ml.csv using pandas.
## Display:
### First 5 records
### Last 5 records
### Total number of rows and columns
### List of column names
### Data types of each column
import pandas as pd

df = pd.read_csv("student_performance_ml.csv")

print("First 5 Records:")
print(df.head())

print("\nLast 5 Records:")
print(df.tail())

print("\nTotal Rows and Columns:")
print(df.shape)

print("Column Names:")
print(df.columns.tolist())

print("\nData types of each column:")
print(df.dtypes)

