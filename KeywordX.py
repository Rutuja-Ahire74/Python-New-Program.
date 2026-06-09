def EmployeeInfo(Name ,Age,Salary,City):
    print("name= ",Name)
    print("age= ",Age)
    print("Salary= ",Salary)
    print("City= ",City)
    
    
    
    
    
def main():
    
    #This is a Keyword Argument
    EmployeeInfo(Age=26,Name="Rohit",City="Pune",Salary=None) #Correct




if __name__ == "__main__":
    main()
