size = int(input("Input size: "))
while size != 0:
    for i in range(size, 0, -1):
        print(i, end=" ")
    print()
    size -= 1
