# index operator [] = gives access to a sequence's element (str, list, tuples)

name = "bro Code"

#if the first letter(index[0]) is lower case, capitalize it

# if(name[0].islower()):
#     name = name.capitalize()

#print(name)


#checks the range from index 0 to 3
first_name = name[0:3].upper() #or [:3]
last_name = name[4:].lower()
print(first_name + " " + last_name)

