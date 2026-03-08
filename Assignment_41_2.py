# The value of K plays an important role in the KNN algorithm.
# Write a Python that demonstrates how prediction changes when K changes.
## Dataset ##
# Use the same dataset as Assignment 1.
## Tasks ##
## Predict the class of the same new point using:
### K = 1
### K = 3
### K = 5

import math

def EucDistance(P1,P2):
    Ans = math.sqrt((P1['X'] - P2['X']) ** 2 + (P1['Y'] - P2['Y']) ** 2)
    return Ans

def PredictClass(data, new_point, k):
    for d in data:
        d['Distance'] = EucDistance(d, new_point)

    sorted_data = sorted(data, key=lambda item: item['Distance'])

    nearest = sorted_data[:k]

    votes = {}
    for n in nearest:
        label = n['Label']
        votes[label] = votes.get(label,0) + 1

    pred = max(votes, key=votes.get)

    return pred

def main():
    data = [
        {'Point':'A', 'X':1, 'Y':2, 'Label':'Red'},
        {'Point':'B', 'X':2, 'Y':3, 'Label':'Red'},
        {'Point':'C', 'X':3, 'Y':1, 'Label':'Blue'},
        {'Point':'D', 'X':6, 'Y':5, 'Label':'Blue'},
    ]

    new_point = {'X':2,'Y':2}

    print("Prediction Results")

    for k in [1,3,5]:
        pred = PredictClass(data.copy(), new_point, k)
        print("K =",k,"->",pred)

if __name__ == "__main__":
    main()