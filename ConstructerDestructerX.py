import gc

class Demo:
    def __init__(self): #Constructor
        print("Inside Constructer")
        
    def __del__(self): #Destructor
        print("Inside Destructor")
 #Allocate       
obj1 = Demo()
obj2 = Demo()


#use

#Dealocate
del obj1
del obj2
 
gc.collect()

print("End of Application")

    
    