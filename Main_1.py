def Multiplication(Value1 , value2):
    ans = 0
    ans = Value1 * value2
    return ans


def main():
    No1 = 0
    No2 = 0
    result = 0


    No1 = int(input("Enter First Number:"))
    No2 = int(input("Enter Second Number:"))

    result = Multiplication (No1,No2)
    print("Multiplication is :",result)
    
main()



