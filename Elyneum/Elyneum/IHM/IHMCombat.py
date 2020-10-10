from tkinter import *
from tkinter import ttk
from FicheDePerso import FicheDePerso
from Presenter import queue
from IHMPersoCbt import FicheDePersoCbt

class Combat(object):
    """description of class"""


    def __init__(self,parent, partie):
        self.partie = partie
        self.parent = parent
        self.mainFrame = Frame(self.parent,highlightbackground="black",highlightthickness=1,height=655,width=1366)
        self.listcombats=Frame(self.mainFrame,highlightbackground="black",highlightthickness=1,height=655,width=100)
        self.btnAddCbt = Button(self.listcombats, text="+", command=self.chooseName)
        self.btnAddCbt.pack()
            
        self.listcombats.place(x=0,y=0)

        self.combatframe = Frame(self.mainFrame,highlightbackground="black",highlightthickness=1,height=655,width=1266)

        self.oposants=Frame(self.combatframe,height=255,width=1266)
        self.oposants.place(x=0,y=0)
        Button(self.oposants, text="+", command= self.addMonster).pack(fill=X, side=LEFT)
        self.nomcbt = StringVar()
        self.nomcbt.set("Label du combat")
        self.labelcbt = Label(self.combatframe,textvariable=self.nomcbt)
        self.labelcbt.place(x=0,y=250)
        self.joueurs=Frame(self.combatframe,height=255,width=1266)
        self.joueurs.place(x=0,y=270)
        Button(self.joueurs, text="+", command= self.addPlayer).pack(fill=X, side=LEFT)
        self.actionframe=Frame(self.combatframe,highlightbackground="black",highlightthickness=1,height=195,width=1266)
        self.buttonact1 = Button(self.actionframe, text="action 1")
        self.buttonact1.pack()
        self.buttonact2 = Button(self.actionframe, text="action 2")
        self.buttonact2.pack()
        self.buttonact3 = Button(self.actionframe, text="action 3")
        self.buttonact3.pack()
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

    def chooseName(self):
        self.window= Tk()
        self.window.title("Nouveau Combat")
        self.window.geometry("400x200")
        self.window.rowconfigure(0,weight = 1)
        self.window.rowconfigure(1,weight = 1)
        self.window.columnconfigure(0,weight=1)
        self.window.columnconfigure(1,weight=1)
        Label(self.window,text = "nom :").grid(row=0,column=0)
        self.value = StringVar()
        self.entree = Entry(self.window, textvariable=self.value, width=30)
        self.entree.grid(row=0,column=1)
        Button(self.window, text="Valider", command=self.addCbt).grid(row=1, column=0)
        self.window.mainloop()

    def addCbt(self):
        queue.append(("ADD_CBT",self.entree.get()))
        self.window.destroy()
    
    def updateCbtList(self, lstCbt):

        for widget in self.listcombats.winfo_children():
            if widget.cget("text") != "+":
                widget.destroy()
        for cbt in lstCbt:
            nom = cbt.nom
            btn =  Button(self.listcombats, text=cbt.nom,command = lambda nom = cbt.nom: self.switchCbt(nom)).pack()

    def switchCbt(self,cbtName):
        queue.append(("SWITCH_CBT",cbtName))
        self.nomcbt.set(cbtName)
        print("switch to "+cbtName)

    def loadCbt(self, cbt):
        for widget in self.joueurs.winfo_children():
            
            if not isinstance(widget, Button):
                widget.destroy()
        print("Loading " + cbt.nom)
        print(cbt)
        for player in cbt.joueur:
            print("\tJoueur : " + player.desc["nom"])
            FicheDePersoCbt(self.joueurs,player).pack()

        for monster in cbt.monstre:
            print("\tMonstre : " + monster.desc["nom"])
            FicheDePersoCbt(self.joueurs,monster).pack()
        return

    def addPlayer(self):
        self.window= Tk()
        self.window.title("Nouveau Combat")
        self.window.geometry("400x200")
        self.window.rowconfigure(0,weight = 1)
        self.window.rowconfigure(1,weight = 1)
        self.window.columnconfigure(0,weight=1)
        self.window.columnconfigure(1,weight=1)
        Label(self.window,text = "Choix :").grid(row=0,column=0)
        listCar = []
        for item in self.partie.collectionFrame.perso:
            listCar.append(item.nomPersonnage.cget("text"))

        self.listeCombo = ttk.Combobox(self.window, values=listCar)
        self.listeCombo.grid(row=1,column=0)
        self.btnAddComp = Button(self.window, text="ajouter", command=self.addCar)
        self.btnAddComp.grid(row=1,column=1)
        self.window.mainloop()
        print("Nouveau player")

    def addCar(self):
        queue.append(("ADD_CHAR_TO_CBT",self.listeCombo.get()))
        self.window.destroy()

    def addMonster(self):
        print("Nouveau Monster")