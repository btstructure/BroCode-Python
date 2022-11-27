
text = "This text has been overwritten by the write_files_in_python.py script."
#the w indicates to write to the file
with open("text1.txt", 'w') as file:
    file.write(text)

#a indicates to append to the file
with open("text1.txt", 'a') as file:
    file.write(text)