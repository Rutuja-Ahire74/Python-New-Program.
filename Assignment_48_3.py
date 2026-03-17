# Write a Python program using StandardScaler to perform feature scaling on the following dataset:
# [[25,20000],
#  [30,40000],
#  [35,80000]]
# Print the scaled dataset.

from sklearn.preprocessing import StandardScaler

def main():

    data = [[25,20000],
            [30,40000],
            [35,80000]]
    
    scaler = StandardScaler()

    scaled_data = scaler.fit_transform(data)

    print("Original Data :")
    print(data)

    print("Scaled Data :")
    print(scaled_data)

if __name__ == "__main__":
    main()