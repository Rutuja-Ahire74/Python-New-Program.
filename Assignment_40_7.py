# Train model using:
## random state = 0
## random_state = 10
## random_state = 42
# Compare testing accuracy. Does the result change?

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def TrainModel(parameter):

    df = pd.read_csv("student_performance_ml.csv")

    X = df[["StudyHours", "Attendance", "PreviousScore"]]
    Y = df["FinalResult"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier()
    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)

    accuracy = accuracy_score(Y_test, Y_pred) * 100

    print("Testing Accuracy (random_state =", parameter, ") :", accuracy)

def main():
    TrainModel(0)
    TrainModel(10)
    TrainModel(42)

if __name__ == "__main__":
    main()