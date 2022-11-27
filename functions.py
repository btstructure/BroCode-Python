#function - a bloack of code which is executed only when it is called, functions are useful to prevent repeating code and do a specific task whenever it is invoked


#functions always end with parenthesis
def hello():
    print("hello!")


hello()

#name is a parameter 
def greeting(name):
    print("good morning " + name)

#Bilbo is a argument that is being passed into the function
greeting("Bilbo")

#you can also pass varaibles
def formal_greeting(name):
    print ("good morning " + name)

formal_name = "Baggins"

formal_greeting(formal_name)

#you can pass more than one argument into a function

def client_information(first_name, last_name, age, location):
    print("My name is " + first_name + " " + last_name)
    print("I am " + str(age) + " years old")
    print("I live in " + location )

#the number of arguments must match the number of parameters 
client_information("Bilbo", "Baggins", 100, "The Shire")