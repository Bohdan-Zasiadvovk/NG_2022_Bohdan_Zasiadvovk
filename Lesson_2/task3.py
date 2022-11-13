size = int(input("Input size: "))
while size != 0:
    for step in range(size, 0, -1):
        print(step, end=" ")
    print()
    size -= 1
