# Generate confusion matrix using sklearn.
# Display it using ConfusionMatrixDisplay.
## Explain clearly:
#### True Positive
#### True Negative
#### False Positive
#### False Negative

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

df = pd.read_csv("student_performance_ml.csv")

X = df[["StudyHours", "Attendance", "PreviousScore"]]
Y = df["FinalResult"]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

model = DecisionTreeClassifier()
model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)

cm = confusion_matrix(Y_test, Y_pred)

result = ConfusionMatrixDisplay(confusion_matrix=cm)
result.plot()

plt.title("Confusion Matrix")
plt.show()