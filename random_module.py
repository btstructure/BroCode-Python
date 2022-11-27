#how to generate random pseudo numbers, must import random
import random

#will generate a random number in the range given, only integers
x = random.randint(1,6)
print(x)

#will generate a number between 0 and 1
y = random.random()
print(x)

#will choose a random element from a list
myList = ['rock', 'paper', 'scissors']
z = random.choice(myList)
print(z)

#will shuffle a list
cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9","Jack", "Queen", "King", "Ace"]
random.shuffle(cards)
print(cards)

