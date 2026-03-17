# Write a Python program, to calculate the Euclidean distance between two points before and after
# applying feature scaling and explain the difference in results.

from sklearn.preprocessing import StandardScaler
import math

def main():
    P1 = [25,30000]
    P2 = [35,80000]

    # Euclidean distance before scaling
    Eud_before = math.sqrt((P1[0]-P2[0])**2 + (P1[1]-P2[1])**2)

    print("Distance before scaling : ",Eud_before)

    # Dataset for scaling
    data = [[25,30000],
            [30,40000],
            [35,80000]]
    
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)

    scaled_P1 = scaled_data[0]
    scaled_P2 = scaled_data[2]

    Eud_after = math.sqrt((scaled_P1[0]-scaled_P2[0]**2) + (scaled_P1[1]-scaled_P2[1])**2)

    print("Distance after scaling : ",Eud_after)

if __name__ == "__main__":
    main()