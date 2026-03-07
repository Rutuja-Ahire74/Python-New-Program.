# Write a single structured Python program that performs:
# 1. Dataset loading
# 2. Data analysis
# 3. Visuaization
# 4. Train-test split
# 5. Model training
# 6. Prediction
# 7. Accuracy calculation
# 8. Confusion matrix generation
# 9. Final conclusion
# Your code should include proper comments explaining each step.

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix,classification_report, ConfusionMatrixDisplay

Border = "-" * 60

####################################################################
# Step 1 : Load the Dataset
####################################################################

print(Border)
print("Step 1 : Load the Dataset")
print(Border)

df = pd.read_csv("student_performance_ml.csv")

print("Dataset loaded successfully...")
print("Initial entries from dataset:")
print(df.head())

####################################################################
# Step 2 : Data Analysis
####################################################################

print(Border)
print("Step 2 : Data Analysis")
print(Border)

print("Dataset Shape :",df.shape)
print("Missing Values :")
print(df.isnull().sum())

print("Class Distribution :")
print(df["FinalResult"].value_counts())

print("Statistical Report of Dataset :")
print(df.describe())

####################################################################
# Step 3 : Decide Independent & Dependent Variables
####################################################################

print(Border)
print("Step 3 : Decide Independent & Dependent Variables")
print(Border)

X = df[["StudyHours", "Attendance", "PreviousScore"]]
Y = df["FinalResult"]

print("X shape :",X.shape)
print("Y shape :",Y.shape)

####################################################################
# Step 4 : Visualization of Dataset
####################################################################

print(Border)
print("Step 4 : Visualization of Dataset")
print(Border)

plt.figure(figsize=(6,5))

for result in df["FinalResult"].unique():
    temp = df[df["FinalResult"] == result]
    plt.scatter(temp["StudyHours"], temp["PreviousScore"], label=result)

plt.title("Study Hours vs Previous Score")

plt.xlabel("Study Hours")
plt.ylabel("Previous Score")

plt.legend()
plt.grid(True)
plt.show()

####################################################################
# Step 5 : Train-Test Split
####################################################################

print(Border)
print("Step 5 : Train-Test Split")
print(Border)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

print("Training shape :", X_train.shape)
print("Testing shape :",X_test.shape)


