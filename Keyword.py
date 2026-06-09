def EmployeeInfo(Name ,Age,Salary,City):
    print("name= ",Name)
    print("age= ",Age)
    print("Salary= ",Salary)
    print("City= ",City)
    
    
    
    
    
def main():
    #Positional
    #EmployeeInfo("Rahul",28,20000,"Pune") #Correct
    #EmployeeInfo(26,"Rohit","Pune",3000.50) #Wrong
    
    
    #This is a Keyword Argument
    EmployeeInfo(Age=26,Name="Rohit",City="Pune",Salary=3000.50) #Correct




if __name__ == "__main__":
    main()
