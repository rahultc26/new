from tkinter import *
from tkinter import ttk

class HelloApp:
    
    def __init__(self,master):
        self.label = ttk.Label(master,text = "Gadag,Gajendragada")
        self.label.grid(row = 0,column = 0,columnspan = 1)

        ttk.Button(master,text='gadag',
                   command=self.gadag_hello).grid(row = 1,column = 0)
        ttk.Button(master,text='gajendragad',
                   command=self.gada_hello).grid(row = 2,column = 0)

    def gadag_hello(self):
            self.label.config(text = 'Hello,Gadag')

    def gada_hello(self):
            self.label.config(text = 'Hello,Gajendragada')

def main():
    root = Tk()
    app = HelloApp(root)
    root.mainloop()

if __name__ == "__main__":main()
        
