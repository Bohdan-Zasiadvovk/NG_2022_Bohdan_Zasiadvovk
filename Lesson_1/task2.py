print("Welcome to calculator!")
flag = True
while flag:
    a, b = float(input("Enter first number (a): ")), float(input("Enter second number (b): "))
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
        result = a + b
    elif operator == 2:
        result = a - b
    elif operator == 3:
        result = a * b
    elif operator == 4:
        result = a / b
    elif operator == 5:
        result = a // b
    elif operator == 6:
        result = a ** b
    elif operator == 7:
        result = a % b
    elif operator == 8:
        result = a ** (1 / b)
    else:
        print("Unknown operation: ")

        continue
    if result % 1 == 0:
        result = round(result)
    print("\nResult:", result)

    print("""\nDo you want continue?
1 - Yes
0 - Exit""")
    tmp = int(input(">>> "))
    if tmp in [1, 0]:
        flag = bool(tmp)
    else:
        print("Unknown answer!")
        flag = False
    print("Bye!")