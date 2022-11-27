#*args - parameter that will pack all arguments into a tuple, useful so that a function can accept a varying amount of arguments

#in this function only two arguments can be passed, so you can't add more than two values

# def add(num1,num2):
#     sum = num1 + num2
#     return sum

#the asterik is what makes the packing/tuple, arg just means argument

def add(*nums):
    sum = 0
    #iterate for every item in the tuple
    for i in nums:
        sum += i
    return sum

print(add(1,3,5,6))
print(add(1,3,5,6,9,15))

#tuples are immutable, so you can't change the values in the tuple

def add2(*stuff):
    sum = 0
    #a list can be changeable, so we can change the values in the list
    stuff = list(stuff)
    #at index 0, the value is 0
    stuff[0] = 0
    for i in stuff:
        sum += i
    return sum

print(add2(1,3,5,6))
