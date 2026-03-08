# Implement Simple Linear Regression manually without using any ML library.
## Dataset ##
# X = [1,2,3,4,5]
# Y = [3,4,2,4,5]
# Tasks
## Calculate
### 1. Mean of X(Xbar)
### 2. Mean of Y(Ybar)
### 3. Slope(m)
### 4. Intercept(c)
# Expected Output Example
## Mean of X = 3
## Mean of Y = 3.6
## Slope (m) = 0.4
## Intercept (c) = 2.4
## Regression Equation:
## Y = 0.4X + 2.4
## Predicted Y for X = 6 : 4.8

import numpy as np

def MarvellousPredictor():
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]

    print("Values of Independent Variables : X - ",X)
    print("Values of Dependent Variables : Y - ",Y)

    mean_x = np.mean(X)
    mean_y = np.mean(Y)

    print("Mean of X :", mean_x)
    print("Mean of Y :", mean_y)

    n = len(X)

    numerator = 0
    denominator = 0

    for i in range(n):
        numerator = numerator + ((X[i] - mean_x) * (Y[i] - mean_y))
        denominator = denominator + ((X[i] - mean_x) ** 2)

    m = numerator / denominator
    print("Slope (m) : ",m)

    C = mean_y - (m * mean_x)
    print("Intercept (c) : ",C)

    print("Regression Equation :")
    print(f"Y = {m}X + {C}")

    x = 6
    Y_pred = (m * x) + C

    print(f"Predicted Y for X = 6 : {Y_pred:.2f}")

def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()