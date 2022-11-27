# if statements = a block of code that will execute if it's condition is true
#in python put a semi-colon at the end of the condition

# set a prompt asking a question
age = int(input("How old are you?: "))

#use age as the condition that will run the block of code if it is met
#a double equal is the comparison and a single is the assignment operator
if age == 100:
    print("You are a century old!")
elif age >= 18:
    print("You are an adult!")
elif age < 0:
    print("You haven't been born yet!")
else: 
    print("You are a child!")