from tkinter import *
from tkinter import ttk

class IHMItem(object):
    """description of class"""
    def __init__(self,parent,item):
        self.parent=parent
        self.item = item
        self.window= Frame(self.parent,highlightbackground="black",highlightthickness=1,height=250,width=200)
        self.i=0
        self.j=0
        for key in item.keys():
            self.nomPersonnage = Label(self.window,text = key)
            self.nomPersonnage.grid(row=self.j,column=0)
            self.nomPersonnage = Label(self.window,text = item[key])
            self.nomPersonnage.grid(row=self.j,column=1)
            self.j = self.j + 1

    def pack(self):
        self.window.pack()

    def grid(self,**kwargs):
        self.window.grid(kwargs)

    def place(self,**kwargs):
        self.window.place(kwargs)
        

