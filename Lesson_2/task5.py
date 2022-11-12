listNumber = map(float, input("Input list: ").split(","))

listNumber = sorted(listNumber)

minimal = listNumber[0]
if minimal % 1 == 0:
    minimal = int(minimal)
print("Minimal: ", minimal)
maximal = listNumber[-1]
if maximal % 1 == 0:
    maximal = int(maximal)
print("Maximal: ", maximal)
summa = sum(listNumber[1:-1])
if summa % 1 == 0:
    summa = int(summa)
print("Summa: ", summa)