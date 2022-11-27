#keyword arguments =  arguments preceded by an identifier when we pass them to a function. The order of the arugment doesn't matter unlike positional arguments. 
# Python knows the name of the arguments that our function receives


def hello(first, middle, last):
    print("Hello " + first + " " + middle + " "+last)

#positional arguments - the order of the arguments matter, the code will run how its ordered

hello("Bilbo","M","Baggins")

#key word arguments
hello(last="Baggins", first="Frodo", middle="Wood")