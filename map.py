#map() function applies a function to each item in an iterable (list, tuple etc.) and returns a list of the results.
#map(function, iterable)

#online store with a list of tuples in usd dollars, convert to euro (curerntly 0.94)

store = [("shirt", 10.00), ("pants", 30.00), ("shoes", 20.00)]

to_euros = lambda data: (data[0], data[1] * 0.94)

#creates a new list with the results of the function
#to_euros is the function, store is the iterable
store_euros = list(map(to_euros, store))

#prints the new list
for i in store_euros:
    print(i)