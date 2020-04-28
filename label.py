from tkinter import *
from tkinter import ttk

root = Tk()
label = ttk.Label(root,text = 'Hello tkinter now i am coming to know about you.. you are very interesting')
label.pack()
label.config(wraplength = 300)
label.config(justify = CENTER)
label.config(foreground = 'green',background = 'white')
label.config(font = ('Courier',30,'bold'))
img1 = PhotoImage(file = "C://Users/HP/Desktop/tenor.gif")
label.config(image = img1)
label.config(compound = 'text')
label.config(compound = 'center')
#label.config(compound = 'left')
#label.config(compound = 'right')
label.img = img1
label.config(compound = label.img)
