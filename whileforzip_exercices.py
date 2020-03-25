while True:
    stuff = input("String to capitalize [type q to quit]: ")
    if stuff == 'q':
        break
    print(stuff.capitalize())

while True:
    value = input("Integer, please [type q to quit]: ")
    if value == 'q': # quit
        break
    number = int(value)
    if number % 2 == 0: #an even number
        print("an even number...")
        continue
    print(number, "squared is", number * number)

accusation = {'room': 'ballroom', 'weapon': 'lead pipe', 'person': 'Col. Mustard'}
for card in accusation: # or, for card in accusation.keys():
    print(card)

for value in accusation.values():
    print(value)

for item in accusation.items():
    print(item)

for card, contents in accusation.items():
    print( 'Card', card, 'has the contents', contents)

cheeses = []
for cheese in cheeses:
    print('This shop has some lovely', cheese)
    break
else: # this is an example of check break, basically when the for loop didn't find any items at all!!
    print('This is not much of a cheese shop, is it?')


days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ": drink", drink, "- eat", fruit, "- enjoy", dessert)

for x in range(0, 3):
    print(x)

for x in range(2, -1, -1):
    print(x)
