#list comprehension - a way to create a list with less syntax
#can mimic certain lambda functions and is easier to read
#list = [expression for item in iterable, can use if/else statement]

squares = [] #empty list
for x in range(1,11): #for loop
    squares.append(x**2) #define what each loop iteration will do
print(squares)

#using list comprehension
squares_comprehension = [x**2 for x in range(1,8)]
print(squares_comprehension)

#using a lambda function
students = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]

#passed = list(filter(lambda x: x >= 70, students))

passed = [x for x in students if x >= 70]
passed_1 = [x if x >= 70 else "failed" for x in students]

print(passed)