# Suppose a dataset has the following values:
# 6,7,8,9,10,11,12
# The mean is 9 and standard deviation is 2.
## Calculate the scaled values for the following numbers using standard scaling.
### 6
### 9
### 12

def main():

    mean = 9
    std = 2

    values = [6,9,12]

    for x in values:
        scaled = (x - mean) / std
        print("Value :",x, "Scaled Value :",scaled)

if __name__ == "__main__":
    main()