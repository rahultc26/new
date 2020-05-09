from tkinter import *
>>> from tkinter import ttk
>>> root  =Tk
>>> root  =Tk()
>>> entry = ttk.Entry(root,width=20)
>>> entry.pack()
>>> entry = ttk.Entry(root,width=50)
>>> entry.pack()
>>> entry.get()
'Enter your crush name'
>>> entry.delete(0,4)
>>> entry.delete(0,2)
>>> entry.insert(0,'enter ')
>>> entry.delete(0,END)
>>> entry.insert(0,"enter your password")
>>> entry.config(show = '*')
>>> entry.get()
 entry.state(['disabled'])
>>> entry.instate(['disabled'])
True
>>> entry.state(['readonly'])
('!readonly',)
>>> entry.state(['readonly'])
