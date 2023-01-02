def hello():
    print("Hello")

#python will treat everything as an object

#below will print the memory address of the function
print(hello)

#below will print the function, do not use () because you will be calling the function
#hi is a variable that is assigned to the function hello, so you can call the function by calling the variable name
hi = hello
hi()
hello()

