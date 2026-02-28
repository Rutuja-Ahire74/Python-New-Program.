# Calculate:
## Training accuracy
## Testing accuracy
# Compare both and comment whether the model is overfitting or underfitting.

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv("student_performance_ml.csv")

X = df[["StudyHours", "Attendance", "PreviousScore"]]
Y = df["FinalResult"]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

model = DecisionTreeClassifier()
model.fit(X_train, Y_train)

train_accuracy = model.score(X_train, Y_train)

test_accuracy = model.score(X_test, Y_test)

print("Training accuracy: {:.2f}%".format(train_accuracy * 100))
print("Testing accuracy: {:.2f}%".format(test_accuracy * 100))

### Result ### 
# Training accuracy: 100.00%
# Testing accuracy: 83.33%
# The training accuracy is 100% while the testing accuracy is 83.33%.
# Since there is a significant difference between them, the model is overfitting.