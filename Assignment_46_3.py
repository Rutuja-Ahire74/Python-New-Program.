# Using the regression model created in the previous question, write a Python program to predict marks for 
# 6 study hours and display the predicted value.

from sklearn.linear_model import LinearRegression

def main():

    X = [[1],[2],[3],[4],[5]]
    Y = [50,55,60,65,70]

    model = LinearRegression()
    model.fit(X, Y)

    hours = [[6]]
    prediction = model.predict(hours)

    print("Predicted Marks for 6 study hours : ",prediction[0])

if __name__ == "__main__":
    main()