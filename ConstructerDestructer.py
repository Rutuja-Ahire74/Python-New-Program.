import gc

class Demo:
    def __init__(self): #Constructor
        print("Inside Constructer")
        
    def __del__(self): #Destructor
        print("Inside Destructor")
 #Allocate       
obj = Demo()

#Dealocate
del obj
 
gc.collect()

print("End of Application")

    
    