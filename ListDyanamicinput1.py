def main():
    
    Size = 0
    Value = 0
    
    print("Enter the number of element :")
    Size = int(input())
    
   
    
    data = list()
      
print("Enter a element :")     
    
for i in range(Size):
    Value = int(input())
    data.append(Value)
    
    print(data)
    
if __name__ == "__main__":
    main()