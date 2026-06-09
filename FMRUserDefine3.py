#Right Code
from functools import reduce

CheckEven = lambda No: (No % 2 == 0)

Increment = lambda No :(No + 1)

Add = lambda a , b :a + b

def filterX(Task , Elements):
    result = list ()
    
    
    for no in Elements:
        Ret = Task (no)
        
        if (Ret == True):
            result.append(no)
            
    return result

def mapx(Task ,Element):
    result = list()
      
      
    for no in Element:
        Ret = Task (no)
        result.append(Ret)
        
    return result



def reduceX(Task, Element ):
    sum = 0 
    
    #[11,21,23,31]
    for no in Element:
        Sum = Task(sum,no)
    return Sum 
        
        
def main():
    Data = [11,10,15,20,22,27,30]
    
    print("Actual Data is :",Data)
    
    FData = list(filter (CheckEven,Data))
    print("Data After filter",FData)
    
    
    MData = mapx(Increment,FData)
    print("Data After Filter :",MData) 
    
    RData = reduceX(Add,MData)
    print ("Data after reduce ",RData)
    

if __name__ == "__main__":
    main()