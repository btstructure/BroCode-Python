#Loop Control Statements = change a loops execution from its normal sequence

#break = used to termine the loop entirely
#continue =  skips to the next iteration of the loop
#pass = does nothing, acts as a placeholder

#will keep asking name until a name is entered and the length is greater than or equal to 3
while True:
    name = input("Enter your name?: ")
    if name != "" and len(name) >= 3:
        break

phone_number = "123-456-7890"
for i in phone_number:
    if i == "-":
        continue
    print(i, end="") #the end prevents the print statement from moving to the next line

#acts as a placeholder and will skip over 13
for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i,",", end="")