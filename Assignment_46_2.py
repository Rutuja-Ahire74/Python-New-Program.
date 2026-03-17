# Write a Python program using LinearRegression to train a regression model.
# Your program should:
### Train the regression model
### Print the coefficient
### Print the intercept

from sklearn.linear_model import LinearRegression

def main():

    X = [[1],[2],[3],[4],[5]]
    Y = [50,55,60,65,70]

    model = LinearRegression()
    model.fit(X, Y)

    print("Coefficient is : ",model.coef_[0])
    print("Intercept : ",model.intercept_)

if __name__ == "__main__":
    main()