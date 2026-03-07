# Without using accuracy_score, manually calculate accuracy:
## Verify whether it matches sklearn accuracy.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def CalculateAccuracy(actual, predicted):
    numerator = 0

    for i in range(len(actual)):
        if actual.iloc[i] == predicted[i]:
            numerator = numerator + 1

    accuracy = (numerator / len(actual)) * 100
    return accuracy

def main():
    df = pd.read_csv("student_performance_ml.csv")

    X = df[["StudyHours", "Attendance", "PreviousScore"]]
    Y = df["FinalResult"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier()
    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)

    manual_accuracy = CalculateAccuracy(Y_test, Y_pred)
    print("Manual Accuracy : ",manual_accuracy)

    sklearn_accuracy = accuracy_score(Y_test, Y_pred) * 100
    print("Sklearn Accuracy : ",sklearn_accuracy)

if __name__ == "__main__":
    main()