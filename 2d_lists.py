#2D lists = a list of lists

drinks = ["coffee","soda", "tea"]
dinner = ["pizza", "hamburger","kebab", "french fries"]
desserts = ["cake", "ice caream"]

#these lists can be combined to one list
food = [drinks, dinner, desserts]
print(food)

#the first index is dinner, the second pizza which is at index 0 of dinner
print(food[1][0])