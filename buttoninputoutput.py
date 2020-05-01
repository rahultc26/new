from tkinter import *
from tkinter import ttk

root = Tk()
button = ttk.Button(text = 'clickMe')
button.pack()
def click():
    print("clicked")
button.config(command = click)
button.state(['disabled'])
button.instate(['disabled'])
logo = PhotoImage(file = 'C:\\Users\\HP\\Desktop\\tenor.gif')
button.config(image = logo)
button.config(image = logo,compound = CENTER)
sample = logo.subsample(5,5)
button.config(image = sample)
