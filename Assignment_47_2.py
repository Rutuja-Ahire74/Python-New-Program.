# Consider the dataset:
# 5,7,9,11,13
# Perform the following calculations step by step:
## Calculate the mean
## Calculate the variance
## Calculate the standard deviation

def main():
    data = [5,7,9,11,13]

    print(data)

    mean = sum(data) / len(data)
    print("Mean is : ",mean)

    sum_variance = 0
    for value in data:
        sum_variance = sum_variance + (value - mean) ** 2

    variance = sum_variance / len(data)
    print("Variance is : ",variance)

    std = variance ** 0.5
    print("Standard Deviation is : ",std)

if __name__ == "__main__":
    main()