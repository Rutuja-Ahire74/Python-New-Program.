# Use the trained model to predict result for a student with:
## StudyHours = 6
## Attendance = 85
## PreviousScore = 66

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv("student_performance_ml.csv")

X = df[["StudyHours", "Attendance", "PreviousScore"]]
Y = df["FinalResult"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier()
model.fit(X_train, Y_train)

# Data = [[6, 85, 66]]
Data = pd.DataFrame({
    "StudyHours": [6],
    "Attendance": [85],
    "PreviousScore":[66]})

pred = model.predict(Data)

if pred[0] == 1:
    print("Predicted Result : Pass")
else:
    print("Predicted Result : Fail")