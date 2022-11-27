#exception - events detected during execution that interrupt the normal flow of a program


#if you divide by zero, you get a ZeroDivisionError, which is an exception
# numerator = int(input("Enter a number to divide: "))
# denominator= int(input("Enter a number to divide by: "))
# result = numerator/denominator
# print(result)

#how to handle exceptions so they don't disrupt the flow of a code
try: 
    numerator = int(input("Enter a number to divide: "))
    denominator= int(input("Enter a number to divide by: "))
    result = numerator/denominator
#this will catch any exception that occurs in the try block, just having an Exception is not good practice
#it is better to catch specific exceptions
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Only enter numbers!")
except Exception:
    print("You can't do that")
else: 
    print(result)
#finally will always run, regardless of whether an exception occurs or not
finally:
    print("This will always run")