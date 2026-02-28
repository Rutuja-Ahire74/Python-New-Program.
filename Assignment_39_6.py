# Train three Decision Tree models with:
## max_depth = 1
## max_depth = 3
## max_depth = None
# Compare their testing accuracies and write your observations.

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv("student_performance_ml.csv")

X = df[["StudyHours", "Attendance", "PreviousScore"]]
Y = df["FinalResult"]

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42)

model1 = DecisionTreeClassifier(max_depth=1)
model1.fit(X_train, Y_train)
acc1 = model1.score(X_test, Y_test)
print("Testing Accuracy (max_depth=1): {:.2f}%".format(acc1 * 100))

model2 = DecisionTreeClassifier(max_depth=3)
model2.fit(X_train, Y_train)
acc2 = model2.score(X_test, Y_test)
print("Testing Accuracy (max_depth=3): {:.2f}%".format(acc2 * 100))

model3 = DecisionTreeClassifier(max_depth=None)
model3.fit(X_train, Y_train)
acc3 = model3.score(X_test, Y_test)
print("Testing Accuracy (max_depth=None): {:.2f}%".format(acc3 * 100))