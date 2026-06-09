def main():
    
    size = 0
    Value = 0
    
    print("Enter the number of element :")
    size = int(input())
    
   
    
    data = list()
      
print("Enter a element :")     
    
for i in range(size):
    Value = int(input())
    data.append(Value)
    
Sum = 0
   
for i in range (size):
       Sum = Sum + data[i]
       
print("summation is :",Sum)
    
if __name__ == "__main__":
    main()