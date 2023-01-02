#sort() used for lists or with iterables
#sorts the list in ascending order
#does not return any value


students = ['John', 'Alex', 'Jack', 'Henry', 'Zoe']

students.sort()

#will sort the list in descending order
# students.sort(reverse=True)

for i in students:
    print(i)

#doesn't work with tuples, but uses sorted() function
cats = ("Persian", "Siamese", "Tabby", "Munchkin")

sorted_cats = sorted(cats)

for i in sorted_cats:
    print(i)


#a list of tuples, how to sort by the second element of the tuple

students_info = [('John', 'A',20), ('Alex', 'C', 19), ('Jack', 'F', 21), ('Henry','B', 18), ('Zoe', 'C', 20)]

#sort by the second element of the tuple, used lambda function
students_info.sort(key=lambda x: x[1])
#grade = lambda grade: grade[1]
#students_info.sort(key=grade)

for i in students_info:
    print(i)