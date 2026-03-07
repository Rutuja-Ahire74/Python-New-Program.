# Train the model using only:
## StudyHours
## Attendance
# Compare the accuracy with the full-feature model.
# Is the model still performing well?

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def main():
    df = pd.read_csv("student_performance_ml.csv")

    Y = df["FinalResult"]

    print("---------------- Full-feature Model ----------------")

    X_full = df[["StudyHours", "Attendance", "PreviousScore", "SleepHours"]]

    X_train1, X_test1, Y_train1, Y_test1 = train_test_split(X_full, Y, test_size=0.2, random_state=42)

    model1 = DecisionTreeClassifier()
    model1.fit(X_train1, Y_train1)

    pred1 = model1.predict(X_test1)

    acc1 = accuracy_score(Y_test1,pred1)

    print("Accuracy with full-features : ",acc1)

    print("----- Train model using StudyHours & Attendance -----")

    X2 = df[["StudyHours", "Attendance"]]

    X_train2, X_test2, Y_train2, Y_test2 = train_test_split(X2, Y, test_size=0.2, random_state=42)

    model2 = DecisionTreeClassifier()
    model2.fit(X_train2, Y_train2)

    pred2 = model2.predict(X_test2)

    acc2 = accuracy_score(Y_test2, pred2)

    print("Accuracy with StudyHours & Attendance : ",acc2)

    print("----------------- Comparison Result ------------------")

    if acc2 == acc1:
        print("Model performs well with fewer features")
    elif acc2 < acc2:
        print("Performance decreased after removing features")
    else:
        print("Performance improved with fewer features")

if __name__ == "__main__":
    main()