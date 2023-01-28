# if __name__ == "__main__":

# why
# Module can be run as a standalone porgram or imported into another program

# python interpreter sets the special variable __name__ to the string "__main__", then python will execute the code in the module
if __name__ == '__main__': #check if the module is being run as a standalone program or imported into another program
    print("Running this module correctly")
else:
    print("Importing this module incorrectly")

