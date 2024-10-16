num1=int(input("enter a number:"))
def calculate(num1):
    op=input("enter an operation:+,-,*,/")
    num2=int(input("enter another number"))
    if op== '+':
        res=num1+num2
    elif op=='-':
        res=num1-num2
    elif op=='*':
        res=num1*num2
    elif op=='/':
        res=num1/num2
    print(f"your result is:{res}")
    choice=input("enter 'y' to continue with result, 'n' for new calculation and 'x' to exit")
    if choice=='y':
        num1=res
        calculate(num1)
    elif choice=='n':
        num1=int(input("enter a number:"))
        calculate(num1)
calculate(num1)
