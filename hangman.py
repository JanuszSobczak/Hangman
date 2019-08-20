import random

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

WORD = ("rower", "skuter", "auto", "narty", "tramwaj")

word = random.choice(WORD)

so_far = "-" * len(word)

wrong = 0

used = []

while wrong < MAX_WRONG and so_far != word:
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

    if guess in word:
        print("Tak, ta litera występuje w słowie")
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
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
else:
    print("\nOdgadłeś!")
    print("\nZagadkowe słowo to", word)
    input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
