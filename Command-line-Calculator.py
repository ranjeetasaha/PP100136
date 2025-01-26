import math

num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))
operator = input("Enter the operation you wish to perform (+,-,*,/,^,sqrt) : ")

try:
    if operator =='+':
        result=num1 + num2
        print("            " , num1 , operator , num2 , "=" , result)
    elif operator == '-':
        result=num1 - num2
        print("            " , num1 , operator , num2 , "=" , result)
    elif operator == '*':
        result=num1 * num2
        print("            " , num1 , operator , num2 , "=" , result)
    elif operator == '/':
        result=num1 / num2
        print("            " , num1 , operator , num2 , "=" , result)
    elif operator == '^':
        num1 = int(num1)
        num2 = int(num2)
        result = pow(num1 , num2)
        print("            " , num1 , operator , num2 , "=" , result)
    elif operator =='sqrt':
        result = math.sqrt(num1)
        print("            square root of " , num1 , "=" , result)
    else:
        print("         You entered invalid operator!!!")

except ZeroDivisionError as dbz:
    print("         Any value can't divided by zero.")