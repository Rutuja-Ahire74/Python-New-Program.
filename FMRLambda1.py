
from functools import reduce
#def CheckEven(No):
 #   return (No % 2 == 0)

CheckEven = lambda No: (No % 2 == 0)


#def Increment(No):
 #   return(No + 1)
 
Increment = lambda No :(No + 1)

#def Add(a,b):
 #   return a+b
 
Add = lambda a , b :a + b


def main():
    Data = [11,10,15,20,22,27,30]
    
    print("Actual Data is :",Data)
    
    FData = list(map(CheckEven, Data))
    print("Data After filter",FData)
    
    
    MData = map = (Increment,FData)
    print("Data After Filter :",MData) 
    
    RData = reduce(Add,MData)
    print ("Data after reduce ",RData)
    

if __name__ == "__main__":
    main()