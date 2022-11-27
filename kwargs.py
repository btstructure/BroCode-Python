# **kwargs =  paraemeter that will pack all arguments into a dictionary, useful so that a function can accept a varying amount of keyword arguments
# unlike args which is a tuple, kwargs is a dictionary

def hello(first, last):
    #f string is a new way to format strings in python 
    print(f"Hello {first} {last}")

#this will return an error because there is no middle name
# hello(first="Bilbo", middle="Freeman", last="Baggins")

def hello2(**entire_name):
    print(f"Hello {entire_name['first']} {entire_name['last']}")

hello2(first = "Bilbo", last = "Baggins")

def hello3(**kwargs):
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")

hello3(title = "Sir", first = "Bilbo", middle="Freeman", last = "Baggins")