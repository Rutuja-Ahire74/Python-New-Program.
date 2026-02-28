# Use the trained model to predict results for X_test.
# Display predicted values along with actual values.

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv("student_performance_ml.csv")

X = df[["StudyHours", "Attendance", "PreviousScore"]]
y = df["FinalResult"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = DecisionTreeClassifier()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

result = pd.DataFrame({
    "Actual" : y_test.values,
    "Predicted" : y_pred
})

print(result)