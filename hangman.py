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

with open("countries.txt") as file:
    data = file.readlines()
    #print(data)
    dictionary = {}
    for line in data:
        items = line.strip().split(' | ')
        key = items[0]
        values = items[1]
        dictionary[key] = values
key = random.choice(list(dictionary.keys()))
print("What is the capital of: ", key.upper())
values = dictionary.get(key)
values = values.upper()

#print(values)
#def randomChoice():


MAX_WRONG = len(HANGMEN) -1
so_far = ""
for i in values:
    if i == " ":
        so_far = so_far + " "
    else:
        so_far = so_far + "-"


wrong = 0

used = []

while wrong < MAX_WRONG and so_far != values:
    print(HANGMEN[wrong])
    print("\nYou've already used the letter: \n", used)
    print("\nFor now, the mysterious word looks like this: \n", so_far)
    guess = input("Enter the letter: ")
    #guess = guess.lower()
    guess = guess.upper()
    while guess in used:
        print("You have already used this letter", guess)
        guess = input("Enter the letter: ")
        #guess = guess.lower()
        guess = guess.upper()
    used.append(guess)

    if guess in values:
        print("Yes, this letter appears in the word")
        new = ""
        for i in range(len(values)):
            if guess == values[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print("\nUnfortunately,", guess, "this letter doesn't appear in this word.")
        wrong += 1

if wrong == MAX_WRONG:
    print(HANGMEN[wrong])
    print("\nYou have been hanged!")
    print("\nThe mysterious word is", values)
else:
    print('\nCONGRATULATION!!!')
    print('''
       0  
     /-+-/
       |
       |
      | |
      | |
----------
|       |
|       
|    
|       
|       
|     
|      
|
--------------
'''  
)
    print("\nThe mysterious word is", values)
    input("\n\nTo end the program, press Enter.")
