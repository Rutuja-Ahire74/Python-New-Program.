# A regression model is given as:
# Salary = 12 * Experience + 25
# Calculate the predicted salary.
# Show all calculations.

def main():
    experience = [2,5,7]

    for exp in experience:
        salary = 12 * exp + 25
        print("Experience is", exp, "years and Predicted Salary is",salary)


if __name__ == "__main__":
    main()