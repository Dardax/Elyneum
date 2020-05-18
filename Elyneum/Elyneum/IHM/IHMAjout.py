from tkinter import *
from tkinter import ttk
from Personnage import Personnage
from Presenter import queue



class IHMAjout(object):
    """description of class"""
    def __init__(self,tag,collection):
 
        self.window= Tk()
        i = 0;
        self.desc=[]
        self.tabcarac=[]
        self.collection=collection
        if tag == "PERSONNAGE":
            modelePers=Personnage(getmodel=True)
            for descri in  modelePers.getDesc().keys():
                Label(self.window,text = descri).grid(row=i,column=0)
                value = StringVar() 
                entree = Entry(self.window, textvariable=value, width=30)
                value.set(modelePers.getDesc()[descri])
                entree.grid(row=i,column=1)
                i =i+1
                self.desc.append(entree)

            for car in  modelePers.getCar():
                Label(self.window,text = car["nom_long"]).grid(row=i,column=0)
                value = StringVar() 
                entree = Entry(self.window, textvariable=value, width=30)
                value.set(car["valeur"])
                entree.grid(row=i,column=1)
                i =i+1
                self.tabcarac.append(entree)
            
            
            listcompetance = []
            for item in collection.competance:
                listcompetance.append(item.item["nom"])

            self.listeCombo = ttk.Combobox(self.window, values=listcompetance)
            self.listeCombo.grid(row=i+1,column=0)
            self.btnAddComp = Button(self.window, text="ajouter", command=self.ajouterComp)
            self.btnAddComp.grid(row=i+1,column=1)
            self.listCompPers=[]
            self.frameComp = Frame(self.window)
            self.frameComp.grid(row=i+2,column=0,columnspan=2)
            listsort = []
            for item in collection.sort:
                listsort.append(item.item["nom"])

            self.listeComboSort = ttk.Combobox(self.window, values=listsort)
            self.listeComboSort.grid(row=i+3,column=0)
            self.btnAddSort = Button(self.window, text="ajouter", command=self.ajouterSort)
            self.btnAddSort.grid(row=i+3,column=1)
            self.listSortPers=[]
            self.frameSort = Frame(self.window)
            self.frameSort.grid(row=i+4,column=0,columnspan=2)
            self.btn = Button(self.window,text="Sauver",command=self.sauver)
            self.btn.grid(row=i+5,column=0)
            self.window.mainloop()
            

    def ajouterComp(self):
        if not (self.listeCombo.get() in self.listCompPers):
            self.listCompPers.append(self.listeCombo.get())
            self.updateListComp()
    
    def updateListComp(self):
        self.clear_frame(self.frameComp)
        for newWidget in self.listCompPers:
            Label(self.frameComp,text=newWidget).pack()

    def ajouterSort(self):
        if not (self.listeComboSort.get() in self.listSortPers):
            self.listSortPers.append(self.listeComboSort.get())
            self.updateListSort()
    
    def updateListSort(self):
        self.clear_frame(self.frameSort)
        for newWidget in self.listSortPers:
            Label(self.frameSort,text=newWidget).pack()

    def clear_frame(self,frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def sauver(self):
        strTabCar = []
        for entry in self.tabcarac:
            strTabCar.append( entry.get())
        strTabDesc = []
        for entry in self.desc:
            strTabDesc.append( entry.get())
            
        self.newPers=Personnage(*strTabCar, *strTabDesc, False)
        for sort in self.listSortPers:
            for sortilege in self.collection.sort:
                if sort == sortilege.item["nom"]:
                    self.newPers.addSpell(sortilege.item)
        for comp in self.listCompPers:
            for competance in self.collection.competance:
                if comp == competance.item["nom"]:
                    self.newPers.addComp(competance.item)

        queue.append(("SAVE_PERSO",self.newPers))
        self.window.destroy()

    def pack(self):
        self.window.pack()

    def grid(self,**kwargs):
        self.window.grid(kwargs)

    def place(self,**kwargs):
        self.window.place(kwargs)
