#reduce() - apply a function to an iterable and reduce it to a single cumulative value
#performs function on first two elements and repeats process until only one element remains
#reduce(function, iterable)

import functools 

#using reduce()
letters = ["h", "e", "l", "l", "o"]
#repeats until only one element remains


#for the first two elements we would like to combine them into a single string
word = functools.reduce(lambda x, y: x + y, letters)
#x = h, y = e -> x + y = he -> x = he, y = l -> x + y = hel and so on
print(word)

#using a for loop
word = ""
for letter in letters:
    word += letter
print(word)

factorial = [6, 5, 4, 3, 2, 1]
#repeats until only one element remains
result = functools.reduce(lambda x, y: x * y, factorial)
print(result)