#set -> collection which is unordered, unindexed. No duplicate values

#to create a set, you must surround it with curly braces
utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup"}

#useful methods for sets

#adds a value to the set
utensils.add("napkin")

#removes a value from the set
utensils.remove("fork")


#add one set to another, all the elements in the dishes set will be added to the utensils
#utensils.update(dishes)


#with union you can join two sets to make a new one
#dinner_table = utensils.union(dishes)


#you can compare the values of two sets with difference
#print(dishes.difference(utensils))


#sets are different from lists because they are unordered and unindexed, when printing it will print in a different order
#a set is faster than a list
#a set doesn't have duplicate values, when printing it will only show once
for x in utensils: 
    print(x)

# for x in dinner_table:
#     print(x)



# ---------------------------------------------------------------------------------------------------------------------------------------------

utensils1 = {"fork", "spoon", "knife", "knife", "knife"}

#clears the set
utensils.clear()

for x in utensils1: 
    print(x)

#utensils2 = {"fork", "spoon", "knife"}
#dishes1 = {"bowl", "plate", "cup", "fork"}

#print(utensils2.intersection(dishes1))