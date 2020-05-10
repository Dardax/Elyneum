from tkinter import *
from tkinter import ttk
from FicheDePerso import FicheDePerso

class Combat(object):
    """description of class"""


    def __init__(self,parent):
            self.parent = parent
            self.mainFrame = Frame(self.parent,highlightbackground="black",highlightthickness=1,height=655,width=1366)
            self.listcombats=Frame(self.mainFrame,highlightbackground="black",highlightthickness=1,height=655,width=100)
            self.buttoncbt1 = Button(self.listcombats, text="combat1")
            self.buttoncbt1.pack()
            self.buttoncbt2 = Button(self.listcombats, text="combat2")
            self.buttoncbt2.pack(expand=True)
            self.listcombats.place(x=0,y=0)

            self.combatframe = Frame(self.mainFrame,highlightbackground="black",highlightthickness=1,height=655,width=1266)

            self.oposants=Frame(self.combatframe,height=255,width=1266)
            #self.labelopo = FicheDePerso(self.oposants)
            #self.labelopo.place(x=0,y=0)
            self.oposants.place(x=0,y=0)
            self.labelcbt = Label(self.combatframe,text="Label du combat")
            self.labelcbt.place(x=0,y=250)
            self.joueurs=Frame(self.combatframe,height=255,width=1266)
            #self.labeljrs = FicheDePerso(self.joueurs)
            #self.labeljrs.place(x=0,y=0)
            #self.labeljrs2 = FicheDePerso(self.joueurs)
            #self.labeljrs2.place(x=220,y=0)
            self.joueurs.place(x=0,y=270)
            self.actionframe=Frame(self.combatframe,highlightbackground="black",highlightthickness=1,height=195,width=1266)
            self.buttonact1 = Button(self.actionframe, text="action 1")
            self.buttonact1.pack()
            self.actionframe.place(x=0,y=520)
            self.combatframe.place(x=100,y=0)
            
    def place(self, **kwargs):
        self.mainFrame.place(kwargs)

    def place_forget(self):
        self.mainFrame.place_forget()

    def pack(self):
        self.mainFrame.pack()

    def grid(self,**kwargs):
        self.mainFrame.grid(kwargs)

    def grid_forget(self):
        self.mainFrame.grid_forget()