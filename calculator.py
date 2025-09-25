print("          ========Calculation========")
print("               Addition(+)")
print("               Subtraction(-)")
print("               Multiplication(*)")
print("               Dvision(/)")
def cal(a,b,c):
    if choice=='+':
        return a+b
    elif choice=='-':
        return a-b
    elif choice=='*':
        return a*b
    elif choice=='/':
        if b==0:
            print("divisible by 0 error")
        else:
            return a/b
    elif choice=='%':
        return a%b
    else:
        print("invalid")
a=int(input("Enter the first number= "))
b=int(input("Enter the second number= "))
choice=input("Enter the choice(+,-,*,/,%):")
result = cal(a,b,choice)
print("Result",result)           