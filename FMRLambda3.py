
from functools import reduce



def main():
    Data = [11,10,15,20,22,27,30]
    print("Actual Data is :",Data)
    
    FData = list (filter ((lambda No: (No % 2 == 0)),Data))
    print("Data After filter",FData)
    
    
    MData = list (map  ((lambda No :(No + 1)),FData))
    print("Data After Filter :",MData) 
    
    RData = list (reduce(lambda a , b :a + b),MData )
    print ("Data after reduce ",RData)
    

if __name__ == "__main__":
    main()