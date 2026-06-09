def main():
    Ans = 0
    try:
        print("Inside try")
        print("Enter first number:")
        No1 = int(input())
    
        print("Enter Second number:")
        No2 = int(input())

        Ans = No1 / No2 
        
    except ZeroDivisionError as zobj:
        print("Inside except :",zobj)
        
    except ValueError as vobj:
        print("Inside except:",vobj)  
        
    except Exception as eobj:   #Genric Except block
        print("Inside except:",eobj)  
        
    finally:
        print("inside finally:")
    
    print("Division is :",Ans)

    
if __name__ == "__main__":
    main()