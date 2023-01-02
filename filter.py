#filter() - creates a collection of elements from an iterable for which a function returns true

#filter(function, iterable)

friensd = [("Rudolf", 25), ("Adam", 30), ("Anne", 17), ("Bob", 22), ("Jen", 16)]

#function to check if the age is >= 18
age = lambda data: data[1] >= 18

#will filter through the list and return a list of tuples with the age >= 18
drinking_age = list(filter(age, friensd))

for i in drinking_age:
    print(i)