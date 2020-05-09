from tkinter import *
from tkinter import ttk
root = Tk()
checkbutton = ttk.Checkbutton(root,text = 'image')
checkbutton.pack()
spam = StringVar()
spam.set('spam')
spam.get()
#checkbutton.config(variable =spam,onvalue = 'spam spam',offvalue='boom spam')
root = Tk()
>>> spam = StringVar()
>>> spam.set('spam')
>>> spam.get()
'spam'
>>> checkbutton = ttk.Checkbutton(text = 'spam')
>>> checkbutton.pack()
>>> checkbutton.config(variable= spam,onvalue='spamplss',offvalue='boom value')
>>> spam.get()
'boom value'
>>> spam.get()
'spamplss'
>>> breakfast = StringVar()
>>> ttk.Radiobutton(root,text= 'eggs',variable=breakfast,value = 'eggs').pack()
>>> ttk.Radiobutton(root,text= 'sause',variable=breakfast,value = 'eggs').pack()
>>> ttk.Radiobutton(root,text= 'sause',variable=breakfast,value = 'sause').pack()
>>> ttk.Radiobutton(root,text= 'omlet',variable=breakfast,value = 'omlet').pack()
>>> breakfast.get()
'eggs'
>>> breakfast.get()
'omlet'
>>> breakfast.get()
'sause'
>>> checkbutton.config(textvariable = breakfast)
>>> 
