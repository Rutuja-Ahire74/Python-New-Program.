def CheckEven(No):
    return (No % 2 == 0)


def Increment(No):
    return(No + 1)





def main():
    Data = [11,10,15,20,22,27,30]
    print("Actual Data is :",Data)
    
    FData = list(map(CheckEven, Data))
    print("Data After filter",FData)
    
    
    MData = map = (Increment,MData)
    print("Data After Filter :",MData) 
    
    

if __name__ == "__main__":
    main()