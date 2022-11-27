# list = used to store multiple items in a single variable
#to create a list surround with square brackets, []

#each food in the list is a element, if we wish to access one we will use a index
food = ["pizza", "hamburger","kebab", "french fries"]

print(food)
print(food[2])

#a few useful functions of list

#removes the element from the list
food.remove("hamburger")
#removes the last element in the list
food.pop()
#inserts the element in the index, (index, element)
food.insert(0, "tacos")

#append adds a element to the end of the element
food.append("ice cream")

#sorts alphabetically
food.sort()

#clears the elements in the list
#food.clear()

for x in food:
    print(x)


