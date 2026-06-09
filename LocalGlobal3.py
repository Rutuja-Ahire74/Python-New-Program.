No = 11 #Global - data defination

def Fun(): #Local
    No = 21
    print("Value of No from Fun is :",No) 
    No= No + 1
    print("Value of No from Fun is :",No) 
    
print("Value of No is :",No) #11
Fun()
print("Value of No is :",No) #11