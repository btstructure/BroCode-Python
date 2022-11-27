#nested loops -> the "inner loop" will finish all of it's iterations before finishing one iteration of the "outer loop"

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

#conventional to use j during a inner for loop as the index
for i in range(rows):
    for j in range(columns):
        print(symbol, end="") #the end prevents the print statement from moving to the next line
    print()