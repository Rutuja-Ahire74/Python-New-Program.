# Write a Python program that classifies a new data point using the K-Nearest Neighbours Algorithm.
# The algorithm should be implemented manually without using any machine learning library.
# The program should:
## Calculate Euclidean distance
## Sort distances
## Select K nearest neighbors
## Predict the class based on majority voting
## Dataset ##
# Point |   X   |    Y   |    Label     |
# A     |   1   |    2   |    Red       |
# B     |   2   |    3   |    Red       |
# C     |   3   |    1   |    Blue      |
# D     |   6   |    5   |    Blue      |
## Tasks ##
### 1. Accept X and Y coordinates of a new point from the user.
### 2. Compute Euclidean distance from all dataset points.
### 3. Sort the distances.
### 4. Select K = 3 nearest neighbors.
### 5. Predict the class label.

import math

def EucDistance(P1,P2):
    Ans = math.sqrt((P1['X'] - P2['X']) ** 2 + (P1['Y'] - P2['Y']) ** 2)
    return Ans

def AcceptPoint():
    X = int(input("Enter X coordnate : "))
    Y = int(input("Enter Y coordnate : "))
    return {'X' : X, 'Y' : Y}

def DisplayNeighbors(nearest):
    print("Nearest Neighbors :")
    for n in nearest:
        print(n['Point'], "- Distance:", round(n['Distance'],2))

def PredictClass(nearest):
    votes = {}

    for n in nearest:
        label = n['Label']
        votes[label] = votes.get(label,0) + 1

    pred = max(votes, key=votes.get)
    return pred

def KNNClassifier():
    data = [
        {'Point':'A', 'X':1, 'Y':2, 'Label':'Red'},
        {'Point':'B', 'X':2, 'Y':3, 'Label':'Red'},
        {'Point':'C', 'X':3, 'Y':1, 'Label':'Blue'},
        {'Point':'D', 'X':6, 'Y':5, 'Label':'Blue'},
    ]

    new_point = AcceptPoint()

    for d in data:
        d['Distance'] = EucDistance(d,new_point)

    sorted_data = sorted(data, key=lambda item: item['Distance'])

    k = 3
    nearest = sorted_data[:k]

    DisplayNeighbors(nearest)

    pred = PredictClass(nearest)

    print("Predicted Class: ",pred)

def main():
    KNNClassifier()

if __name__ == "__main__":
    main()