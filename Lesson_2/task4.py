number = int(input("Input number: "))
factorial = 1
for step in range(1, number + 1):
    factorial *= step

print("Factorial: ", factorial)
