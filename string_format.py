#str.format() - optional method that gives users more control when displaying output

animal = "cow"
item = "moon"


print("The " + animal + " jumped over the " + item)
#the order of the arguments matter
print("The {} jumped over the {}".format(animal, item))
print("The {} jumped over the {}".format("cow","jump"))

print("The {1} jumped over the {0}".format(animal, item)) #positional arugment, the first argument (animal) is the 0th position/index, the second argument (item) is the 1st position/index
print("The {animal} jumped over the {item}".format(animal = "sheep", item="fence")) #keyword argument


text = "The {} ran under the door."
print(text.format("mouse"))

#to add padding to the string use the colon and the number of spaces you want to pad, {:#}
name = "Bilbo"
print("Hello, {:10}. It is a pleasure to meet you!".format(name)) #10 spaces

#formatting with numbers
pi = 3.14159
print("Pi is equal to {:.2f}".format(pi)) #.2f means 2 decimal places, it will round it too

number = 1000
print("The number is {:,}".format(number)) #adds commas to the number
print("The number is {:b}".format(number)) #converts the number to binary
print("The numebr is {:x}".format(number)) #converts the number to hexidecimal
print("The number is {:o}".format(number)) #converts the number to octal
print("The number is {:e}".format(number)) #converts the number to scientific notation