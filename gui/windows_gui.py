#gui - graphical user interface

#windows - serves as a container to hold or contain these widgets

#widgets = GUI elements: buttons, textboxes, images

from tkinter import *
#module included in python

window = Tk() #instantiate an instance of a window
window.geometry("420x420")
window.title("GUI Program")
#making an icon for the window
# icon= PhotoImage(file='kebab.jpg')
# window.iconphoto(True, icon)


window.config(background="red")

window.mainloop() #place window on computer screen, listen for events