from tkinter import *
from tkinter import ttk
from FicheDePerso import FicheDePerso
from IHMItem import IHMItem
from IHMAjout import IHMAjout
import time

class Collection(object):
    """description of class"""

    def __init__(self,parent):
        self.parent = parent
        self.perso=[]
        self.arme=[]
        self.armure=[]
        self.objet=[]
        self.sort=[]
        self.competance=[]
        self.actualFrame=None
        self.actualScroll=None

        self.selectFrame = Frame(parent,height=30,width=1366)
        self.selectFrame.columnconfigure(0,weight=1)
        self.selectFrame.columnconfigure(1,weight=1)
        self.selectFrame.columnconfigure(2,weight=1)
        self.selectFrame.columnconfigure(3,weight=1)
        self.selectFrame.columnconfigure(4,weight=1)
        self.selectFrame.columnconfigure(5,weight=1)
        self.bPersonnages = Button(self.selectFrame, text="Personnages", command=self.switchToPerso)
        self.bPersonnages.grid(row=0,column=0)
        self.bArme = Button(self.selectFrame, text="Arme", command=self.switchToArme)
        self.bArme.grid(row=0,column=1)
        self.bArmure = Button(self.selectFrame, text="Armure", command=self.switchToArmure)
        self.bArmure.grid(row=0,column=2)
        self.bObjet = Button(self.selectFrame, text="Objet",command=self.switchToObjet)
        self.bObjet.grid(row=0,column=3)
        self.bSort = Button(self.selectFrame, text="Sort",command=self.switchToSort)
        self.bSort.grid(row=0,column=4)
        self.bCompetance = Button(self.selectFrame, text="Competance",command=self.switchToCompetance)
        self.bCompetance.grid(row=0,column=5)
        self.bCompetance = Button(self.selectFrame, text="Nouveau",command=self.add)
        self.bCompetance.grid(row=0,column=6)
        self.selectFrame.place(x=0,y=50)

        self.mainFrame = Frame(parent,highlightbackground="black",highlightthickness=1,height=655,width=1366)
        

        #Personnage
        self.canvasperso = Canvas(self.mainFrame,height=625,width=1346)
        self.actualFrame=self.canvasperso
        self.collectionperso = Frame(self.canvasperso)
        self.scrollbarperso = Scrollbar(self.mainFrame,command=self.canvasperso.yview)
        self.actualScroll=self.scrollbarperso
        self.canvasperso.configure(yscrollcommand= self.scrollbarperso.set)

        self.scrollbarperso.pack(side="right",fill="y")
        self.canvasperso.pack()
        for i in range(len(self.perso)):
            j=(int)(i/6)
            k=(int)(i-(6*j))
            self.perso[i].grid(row=j,column=k,padx=2,pady=2)
        self.collectionperso.pack()
        self.canvasperso.create_window((0,0),window=self.collectionperso,anchor='nw')
        self.canvasperso.bind("<Configure>",self.myfunctionperso)

        #Arme
        self.canvasarme = Canvas(self.mainFrame,height=625,width=1346)
        self.collectionarme = Frame(self.canvasarme)
        self.scrollbararme = Scrollbar(self.mainFrame,command=self.canvasarme.yview)
        self.canvasarme.configure(yscrollcommand= self.scrollbararme.set)
        for i in range(len(self.arme)):
            j=(int)(i/6)
            k=(int)(i-(6*j))
            self.arme[i].grid(row=j,column=k,padx=2,pady=2)
        self.collectionarme.pack()
        self.canvasarme.create_window((0,0),window=self.collectionarme,anchor='nw')
        self.canvasarme.bind("<Configure>",self.myfunctionarme)

        #Armure
        self.canvasarmure = Canvas(self.mainFrame,height=625,width=1346)
        self.collectionarmure = Frame(self.canvasarmure)
        self.scrollbararmure = Scrollbar(self.mainFrame,command=self.canvasarmure.yview)
        self.canvasarmure.configure(yscrollcommand= self.scrollbararmure.set)
        for i in range(len(self.armure)):
            j=(int)(i/6)
            k=(int)(i-(6*j))
            self.armure[i].grid(row=j,column=k,padx=2,pady=2)
        self.collectionarmure.pack()
        self.canvasarmure.create_window((0,0),window=self.collectionarmure,anchor='nw')
        self.canvasarmure.bind("<Configure>",self.myfunctionarmure)

        #objet
        self.canvasobjet = Canvas(self.mainFrame,height=625,width=1346)
        self.collectionobjet = Frame(self.canvasobjet)
        self.scrollbarobjet = Scrollbar(self.mainFrame,command=self.canvasobjet.yview)
        self.canvasobjet.configure(yscrollcommand= self.scrollbarobjet.set)
        for i in range(len(self.objet)):
            j=(int)(i/6)
            k=(int)(i-(6*j))
            self.objet[i].grid(row=j,column=k,padx=2,pady=2)
        self.collectionobjet.pack()
        self.canvasobjet.create_window((0,0),window=self.collectionobjet,anchor='nw')
        self.canvasobjet.bind("<Configure>",self.myfunctionobjet)

        #sort
        self.canvassort = Canvas(self.mainFrame,height=625,width=1346)
        self.collectionsort = Frame(self.canvassort)
        self.scrollbarsort = Scrollbar(self.mainFrame,command=self.canvassort.yview)
        self.canvassort.configure(yscrollcommand= self.scrollbarsort.set)
        for i in range(len(self.sort)):
            j=(int)(i/6)
            k=(int)(i-(6*j))
            self.sort[i].grid(row=j,column=k,padx=2,pady=2)
        self.collectionsort.pack()
        self.canvassort.create_window((0,0),window=self.collectionsort,anchor='nw')
        self.canvassort.bind("<Configure>",self.myfunctionsort)

        #competance
        self.canvascompetance = Canvas(self.mainFrame,height=625,width=1346)
        self.collectioncompetance = Frame(self.canvascompetance)
        self.scrollbarcompetance = Scrollbar(self.mainFrame,command=self.canvascompetance.yview)
        self.canvascompetance.configure(yscrollcommand= self.scrollbarcompetance.set)
        for i in range(len(self.competance)):
            j=(int)(i/6)
            k=(int)(i-(6*j))
            self.competance[i].grid(row=j,column=k,padx=2,pady=2)
        self.collectioncompetance.pack()
        self.canvascompetance.create_window((0,0),window=self.collectioncompetance,anchor='nw')
        self.canvascompetance.bind("<Configure>",self.myfunctioncompetance)
        
        
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
    
    def myfunctionperso(self,event):
        self.canvasperso.configure(scrollregion=self.canvasperso.bbox("all"),height=625,width=1346)
    
    def myfunctionarme(self,event):
        self.canvasarme.configure(scrollregion=self.canvasarme.bbox("all"),height=625,width=1346)
    
    def myfunctionarmure(self,event):
        self.canvasarmure.configure(scrollregion=self.canvasarmure.bbox("all"),height=625,width=1346)
    
    def myfunctionobjet(self,event):
        self.canvasobjet.configure(scrollregion=self.canvasobjet.bbox("all"),height=625,width=1346)
    
    def myfunctionsort(self,event):
        self.canvassort.configure(scrollregion=self.canvassort.bbox("all"),height=625,width=1346)
    
    def myfunctioncompetance(self,event):
        self.canvascompetance.configure(scrollregion=self.canvascompetance.bbox("all"),height=625,width=1346)

    def clear_frame(self,frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def updatePerso(self,persos):
        self.clear_frame(self.collectionperso)
        self.perso = []
        for i in range(len(persos)):
            self.perso.append(FicheDePerso(self.collectionperso,persos[i]))
        for i in range(len(self.perso)):
            j=(int)(i/6)
            k=(int)(i-(6*j))
            self.perso[i].grid(row=j,column=k,padx=2,pady=2)

    def updateItem(self,items,typeItem):
        
        if typeItem == "ARME":
            self.clear_frame(self.collectionarme)
            self.arme=[]
            for i in range(len(items)):
                self.arme.append(IHMItem(self.collectionarme,items[i]))
            for i in range(len(self.arme)):
                j=(int)(i/6)
                k=(int)(i-(6*j))
                self.arme[i].grid(row=j,column=k,padx=2,pady=2)

        if typeItem == "ARMURE":
            self.clear_frame(self.collectionarmure)
            self.armure=[]
            for i in range(len(items)):
                self.armure.append(IHMItem(self.collectionarmure,items[i]))
            for i in range(len(self.armure)):
                j=(int)(i/6)
                k=(int)(i-(6*j))
                self.armure[i].grid(row=j,column=k,padx=2,pady=2)

        if typeItem == "OBJET":
            self.clear_frame(self.collectionobjet)
            self.objet=[]
            for i in range(len(items)):
                self.objet.append(IHMItem(self.collectionobjet,items[i]))
            for i in range(len(self.objet)):
                j=(int)(i/6)
                k=(int)(i-(6*j))
                self.objet[i].grid(row=j,column=k,padx=2,pady=2)

        if typeItem == "SORT":
            self.clear_frame(self.collectionsort)
            self.sort=[]
            for i in range(len(items)):
                self.sort.append(IHMItem(self.collectionsort,items[i]))
            for i in range(len(self.sort)):
                j=(int)(i/6)
                k=(int)(i-(6*j))
                self.sort[i].grid(row=j,column=k,padx=2,pady=2)

        if typeItem == "COMPETANCE":
            self.clear_frame(self.collectioncompetance)
            self.competance=[]
            for i in range(len(items)):
                self.competance.append(IHMItem(self.collectioncompetance,items[i]))
            for i in range(len(items)):
                j=(int)(i/6)
                k=(int)(i-(6*j))
                self.competance[i].grid(row=j,column=k,padx=2,pady=2)
            
    def switchToPerso(self):
        if self.actualFrame ==self.canvasperso: return
        self.actualFrame.pack_forget()
        self.actualScroll.pack_forget()
        self.canvasperso.pack()
        self.scrollbarperso.pack(side="right",fill="y")
        self.actualFrame = self.canvasperso
        self.actualScroll = self.scrollbarperso

    def switchToArme(self):
        if self.actualFrame ==self.canvasarme: return
        self.actualFrame.pack_forget()
        self.actualScroll.pack_forget()
        self.canvasarme.pack()
        self.scrollbararme.pack(side="right",fill="y")
        self.actualFrame = self.canvasarme
        self.actualScroll =self.scrollbararme

    def switchToArmure(self):
        if self.actualFrame ==self.canvasarmure: return
        self.actualFrame.pack_forget()
        self.actualScroll.pack_forget()
        self.canvasarmure.pack()
        self.scrollbararmure.pack(side="right",fill="y")
        self.actualFrame = self.canvasarmure
        self.actualScroll =self.scrollbararmure

    def switchToObjet(self):
        if self.actualFrame ==self.canvasobjet: return
        self.actualFrame.pack_forget()
        self.actualScroll.pack_forget()
        self.canvasobjet.pack()
        self.scrollbarobjet.pack(side="right",fill="y")
        self.actualFrame = self.canvasobjet
        self.actualScroll =self.scrollbarobjet

    def switchToSort(self):
        if self.actualFrame ==self.canvassort: return
        self.actualFrame.pack_forget()
        self.actualScroll.pack_forget()
        self.canvassort.pack()
        self.scrollbarsort.pack(side="right",fill="y")
        self.actualFrame = self.canvassort
        self.actualScroll =self.scrollbarsort

    def switchToCompetance(self):
        if self.actualFrame ==self.canvascompetance: return
        self.actualFrame.pack_forget()
        self.actualScroll.pack_forget()
        self.canvascompetance.pack()
        self.scrollbarcompetance.pack(side="right",fill="y")
        self.actualFrame = self.canvascompetance
        self.actualScroll =self.scrollbarcompetance

    def add(self):
        if self.actualFrame ==self.canvascompetance: return
        elif self.actualFrame ==self.canvassort: return
        elif self.actualFrame ==self.canvasobjet:
            dicti = {"nom":"nouveau","Description":"nouvelle desc"}    
            self.objet.append(IHMItem(self.collectionobjet,dicti).grid(row=(int)(len(self.objet)/6),column=(int)(len(self.objet)%6),padx=2,pady=2))
            
        elif self.actualFrame ==self.canvasarmure: return
        elif self.actualFrame ==self.canvasarme: return
        elif self.actualFrame ==self.canvasperso: 
            ajout = IHMAjout("PERSONNAGE",self)
        
