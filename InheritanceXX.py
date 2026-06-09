class Parent:
    def __init__(self):
        print("Inside Parent Constructer")
        
        
    def fun(self):
        print("Inside fun method of parent")
        
class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Inside Child Constructer")
       
        
    def fun(self):
        super().fun()
        print("Inside fun method of child")
        
        
cobj = Child()

cobj.fun()





        