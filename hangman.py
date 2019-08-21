import random

with open("countries.txt") as file:
    data = file.readlines()
    #print(data)
    dictionary = {}
    for line in data:
        items = line.strip(" ").split(' | ')
        key = items[0]
        values = items[1]
        dictionary[key] = values
key = random.choice(list(dictionary.keys()))
print("Jaka jest stolica", key)
values = dictionary.get(key)
print(values)
#def randomChoice():


HANGMEN = (
'''
----------
|       |
|
|
|
|
|
|
|
|
--------------
''',
'''
----------
|       |
|       0
|
|
|
|
|
|
--------------
''',
'''
----------
|       |
|       0
|      -+-
|
|
|
|
|
--------------
''',
'''
----------
|       |
|       0
|     /-+-/
|
|
|
|
|
--------------
''',
'''
----------
|       |
|       0
|     /-+-/
|       |
|
|
|
|
--------------
''',
'''
----------
|       |
|       0
|     /-+-/
|       |
|       |
|
|
|
--------------
''',
'''
----------
|       |
|       0
|     /-+-/
|       |
|       |
|      |
|      |
|
--------------
''',
'''
----------
|       |
|       0
|     /-+-/
|       |
|       |
|      | |
|      | |
|
--------------
'''
)

MAX_WRONG = len(HANGMEN) -1
so_far = "-" * len(values)
wrong = 0

used = []

while wrong < MAX_WRONG and so_far != values:
    print(HANGMEN[wrong])
    print("\nWykorzystałeś już następujące litery:\n", used)
    print("\nNa razie zagadkowe słowo wygląda tak:\n", so_far)
    guess = input("Wprowadz litere: ")
    guess = guess.lower()
    while guess in used:
        print("Już wykorzystałeś literę", guess)
        guess = input("Wprowadź literę: ")
        guess = guess.lower()
    used.append(guess)

    if guess in values:
        print("Tak, ta litera występuje w słowie")
        new = ""
        for i in range(len(values)-1):
            if guess == values[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print("\nNiestety,", guess, "nie występuje w zagadkowym słowie.")
        wrong += 1

if wrong == MAX_WRONG:
    print(HANGMEN[wrong])
    print("\nZostałeś powieszony!")
    print("\nZagadkowe słowo to", values)
else:
    print("\nOdgadłeś!")
    print("\nZagadkowe słowo to", values)
    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
