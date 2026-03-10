number1  = int(input ("enter the 1st number : "))
number2 = int(input ("enter the 2nd number : "))

operator = input ("choose the operator +, * , / , -  =  ")
try:

    if operator == "+" :
        print(number1 + number2)

    elif operator  == "*":
        print(number1 * number2)

    elif operator  == "*":
        print(number1 * number2)


    else:
        print(number1 / number2)

except ZeroDivisionError :
    print("can not be divided by zero")
