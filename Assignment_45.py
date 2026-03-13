# ------------------------------------------ #
## -------- Wine Predictor Dataset --------- #
# ------------------------------------------ #

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

def main():
    df = pd.read_csv("WinePredictor.csv")

    print(df.shape)

    if 'Unnamed: 0' in df.columns:
        df.drop(columns=['Unnamed: 0'], inplace=True)

    print(df.shape)

    X = df.drop("Class")
    Y = df["Class"]

    print("Independent variables: ",X.shape)
    print("Dependent variables: ",Y.shape)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.fit_transform(X_test)

    model = KNeighborsClassifier(n_neighbors=3)

    model.fit(X_train_scaled, Y_train)

    Y_pred = model.predict(X_test_scaled)

    accuracy = accuracy_score(Y_test, Y_pred)

    print("Accuracy of model is : ",accuracy*100)

if __name__ == "__main__":
    main()