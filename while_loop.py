#while loop =  a statement that will execute it's block of code as long as its condition remains true

#an infinite loop happens with the absence of a functional exit

#while 1==1:
    #print("Help! I am stuck in a loop")
name = ""
#will keep running until the length of the name input is larger than 0
while len(name) == 0:
    name = input("What is your name?: ")

#the exit
print("Hello " + name)

#using not

name1 = None
while not name:
    name = input("Enter your name: ")
print("Hello "+ name)