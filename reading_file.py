# with open('test.txt') as file:
#     print(file.read())

#will return if the file is closed or not: true or false
# print(file.closed)

try: 
    with open('test.tx') as file:
        print(file.read())
except FileNotFoundError:
    print("That file does not exist")