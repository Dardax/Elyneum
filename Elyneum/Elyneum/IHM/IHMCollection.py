from tkinter import *
from tkinter import ttk
from FicheDePerso import FicheDePerso

class Collection(object):
    """description of class"""

    def __init__(self,parent):
        self.parent = parent
        self.mainFrame = Frame(parent,highlightbackground="black",highlightthickness=1,height=655,width=1366)
        self.canvas = Canvas(self.mainFrame,height=655,width=1346)
        self.collection = Frame(self.canvas)
        self.scrollbar = Scrollbar(self.mainFrame,command=self.canvas.yview)
        self.canvas.configure(yscrollcommand= self.scrollbar.set)

        self.scrollbar.pack(side="right",fill="y")
        self.canvas.pack(side="bottom")

        self.collection.pack()
        self.canvas.create_window((0,0),window=self.collection,anchor='nw')
        self.canvas.bind("<Configure>",self.myfunction)
        
        
    def place(self, **kwargs):
        self.mainFrame.place(kwargs)

    def place_forget(self):
        self.mainFrame.place_forget()

    def pack(self):
        self.mainFrame.pack()

    def grid(self,**kwargs):
        self.mainFrame.grid(kwargs)
        
    def grid_forget(self):
        self.mainFrame.pack_forget()
    
    def myfunction(self,event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"),height=655,width=1346)

    def updatePerso(self,persos):
        for i in range(len(persos)):
            j=(int)(i/6)
            i=(int)(i-(6*j))
            
            FicheDePerso(self.collection,persos[i]).grid(row=j,column=i,padx=2,pady=2)
            