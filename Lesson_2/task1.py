def out(dictionary):  # out dict
    for key, value in dictionary.items():
        print(f"{key}: {value}")


dictionaryLetters = dict()
inputString = input().lower()

for letter in inputString:
    if letter.isalpha():
        dictionaryLetters[letter] = dictionaryLetters.get(letter, 0) + 1

print("""Choose action:
1 - Counting letters
2 - Sorting by alphabet
3 - Sorting by quantity""")
action = int(input(">>>"))

if action == 1:
    out(dictionaryLetters)
elif action == 2:
    dictionaryLetters = dict(sorted(dictionaryLetters.items(), key=lambda x: x[0]))
    out(dictionaryLetters)
elif action == 3:
    dictionaryLetters = dict(sorted(dictionaryLetters.items(), key=lambda x: x[1], reverse=True))
    out(dictionaryLetters)