#scope -  the region that a variable is recognized. A variable is only available from inside the region it is created. A global and locally scoped versions of a variable can be created


name = "Bilbo" #global scope(available inside and outside the function)

def display_name():
    name="Frodo" #local scope(available only inside this funciton, so it can't be called outside the function)
    print(name)

display_name()
print(name)

#Python Rule
#L - local
#E - enclosed
#G - global
#B - built in