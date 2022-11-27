#nested function calls - function calls inside other function calls, innermost function calls are resolved first, returned value is used as argument for the next outer function

#num = input("Enter a whole positive number: " )
#num = float(num)
#num = abs(num)
#num = round(num)
#print(num)

#this function is similar to the one above, it starts with the intermost function continues through the functions previous for it until it gets to the end
print(round(abs(float(input("Enter a whole positive number: ")))))