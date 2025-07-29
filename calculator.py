def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "incorrect value,b not be zero"
    return a/b

def calculator():
    print("simple calculator")
    while True:
     a=float(input("enter the number:"))
     b=float(input("enter the second number:"))
     inp=input("choose the operator:+,-,*,/")
     if inp=='+':
        print("result:",add(a,b))
     elif inp=='-':
        print("result:",subtract(a,b))
     elif inp=='*':
        print("result:",multiply(a,b))
     elif inp=='/':
        print("result:",divide(a,b))
     else:
        print("invalid operator")
calculator()