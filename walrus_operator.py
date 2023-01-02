#walrus operator := 

#new to python 3.8
# assignment expression :=, assigns values to variables as part of a larger expression

# happy = True
# print(happy)

# print(happy := True)


# foods = list()
# while True:
#     food = input("What food do you like?: ")
#     if food == "quit":
#             break
#     foods.append(food)   

# print(foods)

#using walrus operator for the same thing as above
foods = list()
while food := input("What food do you like?: ") != "quit":
    foods.append(food)

print(foods)