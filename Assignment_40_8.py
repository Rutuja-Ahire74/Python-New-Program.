# Decision Tree Visualization
# Use:
## from sklearn.tree import plot_tree
## Visualize the trained decision tree.
### Which feature appears at the root node?
### Why do you think that feature was selected first?

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree

def main():
    df = pd.read_csv("student_performance_ml.csv")

    X = df[["StudyHours", "Attendance", "PreviousScore"]]
    Y = df["FinalResult"]

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier()
    model.fit(X_train, Y_train)

    plt.figure(figsize=(6,5))
    plot_tree(model, feature_names=X.columns, filled=True)

    plt.title("Decision Tree Visualization")
    plt.show()

if __name__ == "__main__":
    main()