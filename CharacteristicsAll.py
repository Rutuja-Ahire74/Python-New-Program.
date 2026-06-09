class Demo:
    No = 10
    
    
    def __init__(self,A,B):
        self.value1=A 
        self.value2=B
 
print("Class variable:",Demo.No)     
  
obj1 = Demo(11,21)
obj2 = Demo(51,101)

print("Instance veriable of Obj1:",obj1.value1,obj1.value2)
print("Instance veriable of Obj1:",obj2.value1,obj2.value2)


        
 
    
    