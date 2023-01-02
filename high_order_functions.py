#High Order Functions = a function that either
# 1. accepts a function as an argument
# 2. returns a function
#in python functions are first class objects, so they can be assigned to variables, passed into functions, returned from functions, and defined inside other functions

#1. accepts a function as an argument
def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def greet(func):
    text = func("Hello")
    print(text)

greet(loud) #will call the greet function and pass the loud function as an argument, which will then be called inside the greet function
greet(quiet) #will call the greet function and pass the quiet function as an argument, which will then be called inside the greet function

#2. a function that returns a function

#outer function
def divisor(x): #pass 2 as an argument/line 29
    #inner function/nested function
    def divide(y): #pass 10 as an argument/line 31
        return y / x
    return divide

divide_by_2 = divisor(2)

print(divide_by_2(10)) #will print 5