class Demo:
    No = 10
    
    
    def __init__(self,A,B):
        self.value1=A 
        self.value2=B
        
    def fun(self):
        print("Inside Instance method fun",self.value1,self.value2)
     
    @classmethod   
    def sun(cls):
        print("Inside class method sun",cls.No)
        
Demo.sun()
print("class veriable No",Demo.No)

obj = Demo(11,21)

obj.fun()
print("Instance Veribale :",obj.value1,obj.value2)
