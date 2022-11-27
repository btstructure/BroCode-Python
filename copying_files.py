#copyfile() = copies the contents of a file
#copy() = copies the file and its permissions
#copy2() = copies the file, its permissions, and its metadata

import shutil

shutil.copyfile('text1.txt', 'copy.txt') #copies the contents of text1.txt to copy.txt