print("Welcome to calculator!")

firstNumber, secondNumber = float(input("Enter first number (a): ")), float(input("Enter second number (b): "))
print("""Functional: 
1  -  a + b
2  -  a - b
3  -  a * b
4  -  a / b (classical)
5  -  a / b (integer)
6  -  a^b
7  -  remainder of a / b
8  -  root of pover b for a""")
operator = int(input("Choose operation: "))

if operator == 1:
    result = firstNumber + secondNumber
elif operator == 2:
    result = firstNumber - secondNumber
elif operator == 3:
    result = firstNumber * secondNumber
elif operator == 4:
    result = firstNumber / secondNumber
elif operator == 5:
    result = firstNumber // secondNumber
elif operator == 6:
    result = firstNumber ** secondNumber
elif operator == 7:
    result = firstNumber % secondNumber
elif operator == 8:
    result = firstNumber ** (1 / secondNumber)
else:
    print("Unknown operation: ")

if result % 1 == 0:
    result = round(result)
print("\nResult:", result)
