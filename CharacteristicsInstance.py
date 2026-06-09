import gc

class Demo:
    #class Veriable
    No1= 10
    No2=11
    def __init__(self): #Constructor
        #Instance veriable
        self.A=101
        self.B=201
        
        
        print("Inside Constructer")
        
    def __del__(self): #Destructor
        print("Inside Destructor")
        
print(Demo.No1)
print(Demo.No2)

obj = Demo

print(obj.A)
print(obj.B)
 
    
    