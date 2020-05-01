from tkinter import *
from tkinter import ttk
root = Tk()
month = StringVar()
#combobocx
combobox = ttk.Combobox(root, textvariable = month)
combobox.pack()
combobox.config(values = ('ram','raj','arun','jai','mack','john'))
combobox.get()
#spin box
#since spin box is not from tkinter
year = StringVar()
Spinbox(root,from_=1991,to = 2020,textvariable = year).pack()
