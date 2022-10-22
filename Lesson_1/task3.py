print("Welcome to time converter!")
time = int(input("Enter time is seconds: "))
days = time // (24 * 60 * 60)
time %= (24 * 60 * 60)
hours = time // (60 * 60)
time %= 60 * 60
minutes = time // 60
seconds = time % 60

print(days, hours, minutes, seconds, sep=":")
