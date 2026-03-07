# Create a new DataFrame with details of 5 new students.
# Use the trained model to predict their result. Display predictiions clearly.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def main():
    df = pd.read_csv("student_performance_ml.csv")

    X = df[["StudyHours", "Attendance", "PreviousScore"]]
    Y = df["FinalResult"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier()
    model.fit(X_train, Y_train)

    new_students = pd.DataFrame({
        "StudyHours" : [6,3,8,4,7],
        "Attendance" : [85,60,95,70,90],
        "PreviousScore" : [66,50,88,55,62]
    })

    prediction = model.predict(new_students)

    result = new_students.copy()
    result["PredictedResult"] = prediction

    print("----- Display Predictions ------")
    print(result)

if __name__ == "__main__":
    main()