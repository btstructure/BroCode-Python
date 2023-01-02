#lambda function - function written in one line using the lambda keyword
#are anonymous functions, they don't have a name
#accepts any number of arguments, but only has one expression
#syntax: lambda arguments: expression

def double(x):
    return x * 2
print(double(5))

#lambda function
double = lambda x: x * 2
print(double(5))

#lambda function with multiple arguments
def add(x, y):
    return x + y
print(add(5, 7))
add = lambda x, y: x + y
print(add(5, 7))

#lambda function checking if a number is even
even = lambda x: x % 2 == 0
print(even(5))
print(even(6))