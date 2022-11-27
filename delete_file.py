import os

try: 
    os.remove("copy.txt")
    print("The file has been deleted.")
except FileNotFoundError:
    print("That file does not exist.")
except PermissionError:
    print("You do not have permission to delete that file.")
else:
    print("The file has been deleted.")

#go back to copying_files.py and run the script again to see the difference