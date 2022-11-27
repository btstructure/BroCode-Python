# tuple = collection which is ordered and unchangeable, used to group together related data

student = ("Bilbo", 99, "male")

#can count how many times a value appears
print(student.count("Bilbo"))

#locates where the index of the value
print(student.index("Bilbo"))

#will iterate once in our tuple of student
for x in student:
    print(x)


if "Bilbo" in student:
    print("Bilbo is present")