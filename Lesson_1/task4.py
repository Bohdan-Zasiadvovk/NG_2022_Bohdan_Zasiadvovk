print("""Hello! Welcome to quadratic equation calculator!
Quadratic equation has the form:
ax^2 + bx + c""")
a, b, c = map(float, input("Enter a, b and c (with space): ").split())

discriminant = b ** 2 - 4 * a * c

if discriminant >= 0:
    x1 = (- b + discriminant ** 0.5) / (2 * a)
    x2 = (- b - discriminant ** 0.5) / (2 * a)
    if x1 % 1 == 0:
        x1 = round(x1)
    if x2 % 1 == 0:
        x2 = round(x2)
    if x1 == x2:
        print("x =", x1)
    else:
        print("x1 =", x1, "x2 =", x2)
else:
    print("No solutions")
print("\nBye!")
