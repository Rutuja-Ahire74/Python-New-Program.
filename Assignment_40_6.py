# Identify students where:
# Y_test != Y_pred
## Display those rows.
## How many students were misclassified?
## What common pattern do you observe?

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def Display(X_test, Y_test, Y_pred):

    result = X_test.copy()
    result["ActualResult"] = Y_test.values
    result["PredictedResult"] = Y_pred

    rows = result[result["ActualResult"] != result["PredictedResult"]]

    print("Misclassified Students :")
    print(rows)

    print("Total Misclassified Students : ", len(rows))

def main():
    df = pd.read_csv("student_performance_ml.csv")

    X = df[["StudyHours", "Attendance", "PreviousScore"]]
    Y = df["FinalResult"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier()
    model.fit(X_train, Y_train)

    Y_pred = model.predict(X_test)

    Display(X_test, Y_test, Y_pred)

if __name__ == "__main__":
    main()