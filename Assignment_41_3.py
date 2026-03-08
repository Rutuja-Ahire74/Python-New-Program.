# Use KNN to predict whether a student passes or fails based on study hours and attendance.
## Dataset ##
# StudyHours |   Attendance   |   Result    |
#   2        |       60       |     Fail    |
#   5        |       80       |     Pass    |
#   6        |       85       |     Pass    |
#   1        |       50       |     Fail    |
# Tasks
## 1. Accept input from user:
##### Study hours
##### Attendance percentage
## 2. Apply KNN algorithm
## 3. Predict whether the student Passes or Fails

import math

def EucDistance(P1,P2):
    Ans = math.sqrt((P1['StudyHours'] - P2['StudyHours']) ** 2 + (P1['Attendance'] - P2['Attendance']) ** 2)
    return Ans

def predictResult(data, new_point, k):
    for d in data:
        d['Distance'] = EucDistance(d, new_point)

    sorted_data = sorted(data, key=lambda item: item['Distance'])

    nearest = sorted_data[:k]

    votes = {}
    for n in nearest:
        label = n['Result']
        votes[label] = votes.get(label,0) + 1

    pred = max(votes, key=votes.get)
    return pred

def main():
    data = [
        {'StudyHours':2, 'Attendance':60, 'Result':'Fail'},
        {'StudyHours':5, 'Attendance':80, 'Result':'Pass'},
        {'StudyHours':6, 'Attendance':85, 'Result':'Pass'},
        {'StudyHours':1, 'Attendance':50, 'Result':'Fail'},
    ]

    std = int(input("Enter Study Hours :"))
    attend = int(input("Enter Attendance :"))

    new_point = {'StudyHours':std, 'Attendance':attend}

    k = 3
    pred = predictResult(data, new_point, k)

    print("Predicted Result :",pred)

if __name__ == "__main__":
    main()