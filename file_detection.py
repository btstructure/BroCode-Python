#basic file detection

import os

path = "C:\\Users\\User\\Desktop\\test.txt"

if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("That is a file")
else:
    print("That location does not exist")