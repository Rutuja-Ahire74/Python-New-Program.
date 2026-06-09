import gc

class Demo:
    #class Veriable
    No1= 10
    No2=11
    def __init__(self): #Constructor
        print("Inside Constructer")
        
    def __del__(self): #Destructor
        print("Inside Destructor")
        
print(Demo.No1)
print(Demo.No2)
 
    
    