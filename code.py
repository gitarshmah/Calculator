import sys

def addition(a:float, b:float) -> float:
    return a + b


def subtraction(a:float, b:float) -> float:
    return a - b


def multiplication(a:float, b:float) -> float:
    return a * b

def division(a:float, b:float) -> float:
    return a/b


print("\n-----------------Menu------------------------\n1 - Addition\n2 - Subtraction\n3 - Multiplication\n4 - Division\n")

operation = int(input("Enter the operation number above: "))

if operation not in list(range(1, 5)): sys.exit("Incorrect Operation Number") 
num1 = float(input("Enter the first input: "))
num2 = float(input("Enter the second input: "))


if operation == 1:
    print("Result: ", addition(num1, num2))
elif operation == 2:
    print("Result: ", subtraction(num1, num2))
elif operation == 3:
    print("Result: ", multiplication(num1, num2))
elif operation == 4:
    print("Result: ", division(num1, num2))



