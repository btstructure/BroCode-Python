#label - an area widget that holds text and/or an image within a window
from tkinter import *

window = Tk()

label = Label(window,text="Hello World",font=('Arial', 40, 'bold'))

#fg gives font color
#bg - background color
#padx, pady - makes padding

#pack function - defaults widget to the center
label.pack()

#places where you wish to put the label by coordinates
# label.place(x=0,y=0)

window.mainloop()