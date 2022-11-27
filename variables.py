
#strings - series of character, single or double qoutes
first_name = "Bilbo"
last_name = "Baggins"
introduction = "Hell, my name is " + first_name + " " + last_name + "."

#integers - whole numbers
age = 21

age += 1

#print("Hello " + first_name + last_name)

print(type(first_name))
print(type(age))
print(age)

#when using a string concatenation with a string literal, a different data type will give a type error, and must use type casting 
#print(introduction + " I am " + age + " years old")
print(introduction + " I am " + str(age) + " years old")


#float - floating point number, a decimal

height =  160.3 
print(height)
print(type(height))
myAge = " I am " + str(age) + " years old."

print(introduction + myAge + " I am " + str(height) + "cm tall!" )


#boolean - true or false datatype
human = False
print(type(human))
print("Are you a human?: " + str(human))