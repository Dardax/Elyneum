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

        self.selectFrame = Frame(self.parent,height=30,width=1366)
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
        self.bCompetance = Button(self.selectFrame, text="Competence",command=self.switchToCompetance)
        self.bCompetance.grid(row=0,column=5)
        self.bCompetance = Button(self.selectFrame, text="Nouveau",command=self.add)
        self.bCompetance.grid(row=0,column=6)
        self.selectFrame.place(x=0,y=50)

        self.mainFrame = Frame(self.parent,highlightbackground="black",highlightthickness=1,height=655,width=1366)
        
        self.canvas = Canvas(self.mainFrame,height=625,width=1346)
        self.actualFrame=""
        self.collection = Frame(self.canvas)
        self.scrollbar = Scrollbar(self.mainFrame,command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.scrollbar.pack(side="right",fill="y")
        self.collection.pack()

        self.canvas.pack(side="bottom")
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
        self.mainFrame.grid_forget()
    
    def myfunction(self,event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"),height=625,width=1346)
   
    def refresh_frame(self):
        oldFrame = self.actualFrame
        self.actualFrame = ""
        self.clear_frame(self.collection)
        if oldFrame=="PERSO":
            self.switchToPerso()
        elif oldFrame=="ARME":
            self.switchToArme()
        elif oldFrame=="ARMURE":
            self.switchToArmure()
        elif oldFrame=="SORT":
            self.switchToSort()
        elif oldFrame=="COMPETANCE":
            self.switchToCompetance()
        elif oldFrame=="OBJET":
            self.switchToObjet()

    def clear_frame(self,frame):
        for widget in frame.winfo_children():
            widget.grid_forget()

    def updatePerso(self,persos):
        self.perso = []
        for i in range(len(persos)):
            self.perso.append(FicheDePerso(self.collection,persos[i]))
        
    def updateItem(self,items,typeItem):
        if typeItem == "ARME":
            self.arme=[]
            for i in range(len(items)):
                self.arme.append(IHMItem(self.collection,items[i],typeItem))
            

        if typeItem == "ARMURE":
            self.armure=[]
            for i in range(len(items)):
                self.armure.append(IHMItem(self.collection,items[i],typeItem))
            

        if typeItem == "OBJET":
            self.objet=[]
            for i in range(len(items)):
                self.objet.append(IHMItem(self.collection,items[i],typeItem))
            
        if typeItem == "SORT":
            self.sort=[]
            for i in range(len(items)):
                self.sort.append(IHMItem(self.collection,items[i],typeItem))

        if typeItem == "COMPETANCE":
            self.competance=[]
            for i in range(len(items)):
                self.competance.append(IHMItem(self.collection,items[i],typeItem))
            
    def switchToPerso(self):
        if self.actualFrame =="PERSO": return
        self.clear_frame(self.collection)
        for i in range(len(self.perso)):
            j=(int)(i/6)
            k=(int)(i-(6*j))
            if isinstance(self.perso[i],FicheDePerso):
                self.perso[i].grid(row=j,column=k,padx=2,pady=2)
        self.actualFrame = "PERSO"

    def switchToArme(self):
        if self.actualFrame =="ARME": return
        self.clear_frame(self.collection)
        for i in range(len(self.arme)):
            j=(int)(i/6)
            k=(int)(i-(6*j))
            if isinstance(self.arme[i], IHMItem):
                self.arme[i].grid(row=j,column=k,padx=2,pady=2)
        self.actualFrame = "ARME"     
        

    def switchToArmure(self):
        if self.actualFrame =="ARMURE": return
        self.clear_frame(self.collection)
        for i in range(len(self.armure)):
            j=(int)(i/6)
            k=(int)(i-(6*j))
            self.armure[i].grid(row=j,column=k,padx=2,pady=2)
        self.actualFrame = "ARMURE"

    def switchToObjet(self):
        if self.actualFrame =="OBJET": return
        self.clear_frame(self.collection)
        for i in range(len(self.objet)):
            j=(int)(i/6)
            k=(int)(i-(6*j))
            self.objet[i].grid(row=j,column=k,padx=2,pady=2)
        self.actualFrame = "OBJET"

    def switchToSort(self):
        if self.actualFrame =="SORT": return
        self.clear_frame(self.collection)
        for i in range(len(self.sort)):
            j=(int)(i/6)
            k=(int)(i-(6*j))
            self.sort[i].grid(row=j,column=k,padx=2,pady=2)
        self.actualFrame = "SORT"

    def switchToCompetance(self):
        if self.actualFrame =="COMPETANCE": return
        self.clear_frame(self.collection)
        for i in range(len(self.competance)):
            j=(int)(i/6)
            k=(int)(i-(6*j))
            self.competance[i].grid(row=j,column=k,padx=2,pady=2)
        self.actualFrame = "COMPETANCE"


    def add(self):
        ajout = IHMAjout(self.actualFrame,self)
        #if self.actualFrame =="COMPETANCE": return
        #elif self.actualFrame =="SORT": 
            
        #elif self.actualFrame =="OBJET":
        #    dicti = {"nom":"nouveau","Description":"nouvelle desc"}    
        #    self.objet.append(IHMItem(self.collection,dicti).grid(row=(int)(len(self.objet)/6),column=(int)(len(self.objet)%6),padx=2,pady=2))
            
        #elif self.actualFrame =="ARMURE": return
        #elif self.actualFrame =="ARME": return
        #elif self.actualFrame =="PERSO": 
        #    ajout = IHMAjout("PERSONNAGE",self)
        
