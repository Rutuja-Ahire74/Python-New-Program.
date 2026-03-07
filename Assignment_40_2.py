# Remove the column SleepHours from the dataset.
## train the model again.
## Compare new accuracy with previous accuracy.
## Does removing this feature affect performance?

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def main():

    print("----- Model with SleepHours -----")
    df = pd.read_csv("student_performance_ml.csv")

    X1 = df.drop("FinalResult", axis=1)
    Y = df["FinalResult"]

    X_train1, X_test1, Y_train1, Y_test1 = train_test_split(X1, Y, test_size=0.2, random_state=42)

    model1 = DecisionTreeClassifier()
    model1.fit(X_train1, Y_train1)

    pred1 = model1.predict(X_test1)
    acc1 = accuracy_score(Y_test1, pred1)

    print("Accuracy with SleepHours : ",acc1)


    print("----- Model without SleepHours -----")
    X2 = df.drop(["SleepHours", "FinalResult"], axis=1)

    X_train2, X_test2, Y_train2, Y_test2 = train_test_split(X2, Y, test_size=0.2, random_state=42)

    model2 = DecisionTreeClassifier()
    model2.fit(X_train2, Y_train2)

    pred2 = model2.predict(X_test2)
    acc2 = accuracy_score(Y_test2, pred2)

    print("Accuracy without SleepHours : ",acc2)

    print("--------- Comparison Result ---------")

    if acc1 == acc2:
        print("Removing SleepHours did not affect performance")
    elif acc2 < acc1:
        print("Removing SleepHours reduced model performance")
    else:
        print("Removing SleepHours improved model performance")

if __name__ == "__main__":
    main()