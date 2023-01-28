#zip(*ieratbles0) aggregate elements from two or more iterables (list, tuple, string, etc.). creates a zip object with paired elements stored as tuples for each element in the zip object

first_name = ["Bilbo", "Frodo", "Gandalf"] #list
last_name = ("Baggins", "Baggins", "theGrey") #tuple

full_name= zip(first_name, last_name) #zip object, will take the first element from each iterable and pair them together, then the second element, etc.

for i in full_name: #loop through the zip object, each element is a tuple with the paired elements from the iterables
    print(i)


print(type(full_name))
