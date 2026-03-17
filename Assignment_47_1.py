# Consider the dataset:
# 4,6,8,10,12
# Perform the following steps:
## Calculate the mean
## Find the deviation of each value from the mean
## Calculate the square of each deviation
## Calculate the variance of the dataset

def main():
    data = [4,6,8,10,12]

    print(data)

    mean = sum(data) / len(data)

    print("Mean of data : ",mean)

    deviations = []
    for value in data:
        deviations.append(value-mean)

    print("Deviation is : ",deviations)

    square_dev = []
    for d in deviations:
        square_dev.append(d*d)

    print("Square of Deviation : ",square_dev)

    variance = sum(square_dev) / len(data)

    print("Variance of dataset : ",variance)

if __name__ == "__main__":
    main()