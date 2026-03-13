# ------------------------------------------ #
## -------- Play Predictor Dataset -------- #
# ------------------------------------------ #


import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def GetData():
    Border = "-"*40

    data = pd.read_csv("PlayPredictor.csv")

    print(Border)
    print("Dataset loaded successfully")
    print(Border)
    print(data)

    return data

def AnalyzeData(data):
    Border = "-"*40

    if 'Unnamed: 0' in data.columns:
        data.drop(columns=['Unnamed: 0'], inplace=True)

    print(Border)
    print("Dataset after removal of unwanted column")
    print(Border)
    print(data)

    Encoder = LabelEncoder()

    data['Whether'] = Encoder.fit_transform(data['Whether'])
    data['Temperature'] = Encoder.fit_transform(data['Temperature'])
    data['Play'] = Encoder.fit_transform(data['Play'])

    print(Border)
    print("Dataset after Encoding")
    print(Border)
    print(data)

    X = data[['Whether','Temperature']]
    Y = data['Play']

    return X, Y

def TrainModel(X, Y):
    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(X,Y)
    return model

def TestModel(model):
    Whether = int(input("Enter Weather Value: "))
    Temperature = int(input("Enter Temperature Value: "))

    test_data = pd.DataFrame([[Whether,Temperature]], columns=['Whether', 'Temperature'])

    result = model.predict(test_data)

    if (result[0] == 1):
        print("Play = Yes")
    else:
        print("Play = No")

def CheckAccuracy(X,Y):
    Border = "-"*40

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.5, random_state=42)

    print(Border)
    print("Accuracy for different values of K")
    print(Border)

    for k in [1,3,5]:
        model = KNeighborsClassifier(n_neighbors=k)

        model.fit(X_train, Y_train)

        Y_pred = model.predict(X_test)

        accuracy = accuracy_score(Y_test, Y_pred)

        print(f"Accuracy with K = {k} is {accuracy*100}")


def main():
    data = GetData()
    X, Y = AnalyzeData(data)
    model = TrainModel(X,Y)
    TestModel(model)
    CheckAccuracy(X,Y)

if __name__ == "__main__":
    main()