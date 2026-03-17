# Write a Python program that calculates the variance and standard deviation of the dataset:
# [6,7,8,9,10,11,12]
# Display both results

def main():
    data = [6,7,8,9,10,11,12]

    mean = sum(data) / len(data)

    sum_variance = 0
    for value in data:
        sum_variance = sum_variance + (value - mean) ** 2

    variance = sum_variance / len(data)

    std = variance ** 0.5

    print(data)
    print("Variance of data : ",variance)
    print("Standard Deviation of data : ",std)

if __name__ == "__main__":
    main()