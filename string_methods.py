name = "Bilbo Baggins"
low_name = "frodo baggins"
high_name = "Gandalf"
number = "123"

#length of name

print(len(name))

#finds the first index of where the character is

print(name.find("o"))

#capitalizes the first letter in the string

print(low_name.capitalize())

#uppercases the entire string

print(low_name.upper())

#lowercases the entire string

print(high_name.lower())

#will return true/false if the string is a digit

print(name.isdigit())
print(number.isdigit())

#will return true/false if the string is letters, theere can be no space in the string
print(name.isalpha())
print(number.isalpha())
print(high_name.isalpha())

#count how many characters within the string

print(name.count("g"))

#replaces the character with a new character

print(name.replace("a", "u"))