# Train model with:
## max_depth = None
# Calculate:
## Training accuracy
## Testing accuracy
# If training accuracy is 100% but testing accuracy is lower, explain why this happens.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def main():
    df = pd.read_csv("student_performance_ml.csv")

    X = df[["StudyHours", "Attendance", "PreviousScore"]]
    Y = df["FinalResult"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier(max_depth=None)
    model.fit(X_train, Y_train)

    Y_train_pred = model.predict(X_train)
    Y_test_pred = model.predict(X_test)

    train_accuracy = accuracy_score(Y_train, Y_train_pred) * 100

    test_accuracy = accuracy_score(Y_test, Y_test_pred) * 100

    print("Training Accuracy : ", train_accuracy)
    print("Testing Accuracy : ", test_accuracy)

if __name__ == "__main__":
    main()