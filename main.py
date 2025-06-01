"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jakub Rubes
email: rubes.jakub@email.cz
"""
TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]
line = '-' * 40
numbersCount = 0
titleCount = 0
upperCount = 0
lowerCount = 0
totalValue = 0
letterCount = dict()
##############  Prihlaseni uzivatele ##############
users = {'bob':'123', 'ann':'pass123', 'mike':'password123', 'liz':'pass123'}
inputUser = input('username:')
inputPassword = input('password:')
print(line)
if inputUser in users and inputPassword == users[inputUser]:
    print(f'Welcome to the app, {inputUser}')
else:
    print('unregistered user, terminating the program..')
    exit()
#################  Vyber textu ####################
print('We have 3 texts to be analyzed.')
print(line)
inputNumber = input('Enter a number btw. 1 and 3 to select: ')
if inputNumber not in ['1', '2', '3']:
    print('Invalid number, terminating the program..')
    exit()
print(line)
text = TEXTS[int(inputNumber) - 1]
##############  Celkovy pocet slov  ###############
wordsCount = len(text.split())
#################  Prace s textem #################
for words in text.split():
    if words.isdigit():
        numbersCount += 1
        totalValue += int(words)
    elif words.istitle():
        titleCount += 1 
    elif words.isupper():
        upperCount += 1
    else words.islower():
        lowerCount += 1
print(f'There are {wordsCount} words in the selected text.')
print(f'There are {titleCount} titlecase words.')
print(f'There are {upperCount} uppercase words.')
print(f'There are {lowerCount} lowercase words.')
print(f'There are {numbersCount} numeric strings.')
print(f'The sum of all the numbers {totalValue}')
print(line)
##########  Graficke znazeni delky slov ###########
print('LEN|   OCCURENCES   |NR.')   
print(line)
for length in text.split():
    for letter in length:
        if not letter.isalnum():
            length = length.replace(letter, '')
    wordLength = len(length) 
    letterCount[wordLength] = letterCount.get(wordLength, 0) + 1
for i in range(len(letterCount) + 1):
    if i in letterCount:
        print(f'{i:>3}|{"*" * letterCount[i]:<22}|{letterCount[i]:<2}')
