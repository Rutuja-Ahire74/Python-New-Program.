# 1. After training the Decision Tree model, use:
## model.feature_importances_
### Display importance score of each feature.
### Which feature contributes the most in predicting FinalResult?
### Which feature contributes the least?

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

def main():
    df = pd.read_csv("student_performance_ml.csv")

    X = df[["StudyHours", "Attendance", "PreviousScore"]]
    Y = df["FinalResult"]

    X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier()
    model.fit(X_train, Y_train)

    importances = model.feature_importances_

    feature_df = pd.DataFrame({
        "Feature" : X.columns,
        "Importance" : importances
    }).sort_values(by="Importance", ascending=False)

    print("Feature Importance Score:")
    print(feature_df)

    print("Most Important Feature : ",feature_df.iloc[0]["Feature"])
    print("Least Important Feature : ",feature_df.iloc[-1]["Feature"])

if __name__ == "__main__":
    main()