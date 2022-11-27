import os

source = "copy.txt"
destination = "C:\\Users\\name\\Desktop\\copy.txt" #change the path to your desktop

try:
    if os.path.exists(destination):
        print("The file already exists.")
    else:
        os.replace(source, destination)
        print("The file has been moved.")
except FileNotFoundError:
    print("The file does not exist.")
    
