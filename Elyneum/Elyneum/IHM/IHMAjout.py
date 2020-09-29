from tkinter import *
from tkinter import ttk
from Personnage import Personnage
from Presenter import queue



class IHMAjout(object):
    """description of class"""
    def __init__(self,tag,collection):
 
        self.window= Tk()
        self.i = 0;
        self.desc=[]
        self.tabcarac=[]
        self.dico ={}
        self.keyEntree=[]
        self.valueEntree=[]
        self.collection=collection
        modelePers=Personnage(getmodel=True)
        if tag == "PERSO":
            for descri in  modelePers.getDesc().keys():
                Label(self.window,text = descri).grid(row=self.i,column=0)
                value = StringVar() 
                value.set(modelePers.getDesc()[descri])
                entree = Entry(self.window, textvariable=value, width=30)
                entree.grid(row=self.i,column=1)
                self.i =self.i+1
                self.desc.append(entree)

            for car in  modelePers.getCar():
                Label(self.window,text = car["nom_long"]).grid(row=self.i,column=0)
                value = StringVar() 
                entree = Entry(self.window, textvariable=value, width=30)
                value.set(car["valeur"])
                entree.grid(row=self.i,column=1)
                self.i =self.i+1
                self.tabcarac.append(entree)
            
            
            listcompetance = []
            for item in collection.competance:
                listcompetance.append(item.item["nom"])

            self.listeCombo = ttk.Combobox(self.window, values=listcompetance)
            self.listeCombo.grid(row=self.i+1,column=0)
            self.btnAddComp = Button(self.window, text="ajouter", command=self.ajouterComp)
            self.btnAddComp.grid(row=self.i+1,column=1)
            self.listCompPers=[]
            self.frameComp = Frame(self.window)
            self.frameComp.grid(row=self.i+2,column=0,columnspan=2)
            listsort = []
            for item in collection.sort:
                listsort.append(item.item["nom"])

            self.listeComboSort = ttk.Combobox(self.window, values=listsort)
            self.listeComboSort.grid(row=self.i+3,column=0)
            self.btnAddSort = Button(self.window, text="ajouter", command=self.ajouterSort)
            self.btnAddSort.grid(row=self.i+3,column=1)
            self.listSortPers=[]
            self.frameSort = Frame(self.window)
            self.frameSort.grid(row=self.i+4,column=0,columnspan=2)
            self.btn = Button(self.window,text="Sauver",command=self.sauver)
            self.btn.grid(row=self.i+5,column=0)
            

        elif tag == "SORT":
            self.dico ={}
            if len(self.collection.sort) != 0:
                for attrib in self.collection.sort[0].item:
                    Label(self.window,text = attrib).grid(row=self.i,column=0)
                    value = StringVar() 
                    entree = Entry(self.window, textvariable=value, width=30)
                    entree.grid(row=self.i,column=1)
                    self.dico[attrib] = entree
                    self.i =self.i+1
            else:
                
                Label(self.window,text = "nom").grid(row=self.i,column=0)
                value = StringVar() 
                entree = Entry(self.window, textvariable=value, width=30)
                entree.grid(row=self.i,column=1)
                self.dico["nom"] = entree
                self.i =self.i+1
                Label(self.window,text = "Description").grid(row=self.i,column=0)
                value = StringVar() 
                entree = Entry(self.window, textvariable=value, width=30)
                entree.grid(row=self.i,column=1)
                self.dico["Description"] = entree
                self.i =self.i+1
                Button(self.window,text="+",command=self.addLine).grid(row=0,column=2)
            self.btn = Button(self.window,text="Sauver",command=self.sauverSort)
            self.btn.grid(row=self.i+1,column=0)

        elif tag == "ARME":
            self.dico ={}
            if len(self.collection.arme) != 0:
                for attrib in self.collection.arme[0].item:
                    Label(self.window,text = attrib).grid(row=self.i,column=0)
                    value = StringVar() 
                    entree = Entry(self.window, textvariable=value, width=30)
                    entree.grid(row=self.i,column=1)
                    self.dico[attrib] = entree
                    self.i =self.i+1
            else:
                
                Label(self.window,text = "nom").grid(row=self.i,column=0)
                value = StringVar() 
                entree = Entry(self.window, textvariable=value, width=30)
                entree.grid(row=self.i,column=1)
                self.dico["nom"] = entree
                self.i =self.i+1
                Label(self.window,text = "Description").grid(row=self.i,column=0)
                value = StringVar() 
                entree = Entry(self.window, textvariable=value, width=30)
                entree.grid(row=self.i,column=1)
                self.dico["Description"] = entree
                self.i =self.i+1
                Button(self.window,text="+",command=self.addLine).grid(row=0,column=2)
            self.btn = Button(self.window,text="Sauver",command=self.sauverArme)
            self.btn.grid(row=self.i+1,column=0)

        elif tag == "ARMURE":
            self.dico ={}
            if len(self.collection.armure) != 0:
                for attrib in self.collection.armure[0].item:
                    Label(self.window,text = attrib).grid(row=self.i,column=0)
                    value = StringVar() 
                    entree = Entry(self.window, textvariable=value, width=30)
                    entree.grid(row=self.i,column=1)
                    self.dico[attrib] = entree
                    self.i =self.i+1
            else:
                
                Label(self.window,text = "nom").grid(row=self.i,column=0)
                value = StringVar() 
                entree = Entry(self.window, textvariable=value, width=30)
                entree.grid(row=self.i,column=1)
                self.dico["nom"] = entree
                self.i =self.i+1
                Label(self.window,text = "Description").grid(row=self.i,column=0)
                value = StringVar() 
                entree = Entry(self.window, textvariable=value, width=30)
                entree.grid(row=self.i,column=1)
                self.dico["Description"] = entree
                self.i =self.i+1
                Button(self.window,text="+",command=self.addLine).grid(row=0,column=2)
            self.btn = Button(self.window,text="Sauver",command=self.sauverArmure)
            self.btn.grid(row=self.i+1,column=0)

        elif tag == "OBJET":
            self.dico ={}
            if len(self.collection.objet) != 0:
                for attrib in self.collection.objet[0].item:
                    Label(self.window,text = attrib).grid(row=self.i,column=0)
                    value = StringVar() 
                    entree = Entry(self.window, textvariable=value, width=30)
                    entree.grid(row=self.i,column=1)
                    self.dico[attrib] = entree
                    self.i =self.i+1
            else:
                
                Label(self.window,text = "nom").grid(row=self.i,column=0)
                value = StringVar() 
                entree = Entry(self.window, textvariable=value, width=30)
                entree.grid(row=self.i,column=1)
                self.dico["nom"] = entree
                self.i =self.i+1
                Label(self.window,text = "Description").grid(row=self.i,column=0)
                value = StringVar() 
                entree = Entry(self.window, textvariable=value, width=30)
                entree.grid(row=self.i,column=1)
                self.dico["Description"] = entree
                self.i =self.i+1
                Button(self.window,text="+",command=self.addLine).grid(row=0,column=2)
            self.btn = Button(self.window,text="Sauver",command=self.sauverObjet)
            self.btn.grid(row=self.i+1,column=0)

        elif tag == "COMPETANCE":
            self.dico ={}
            if len(self.collection.competance) != 0:
                for attrib in self.collection.competance[0].item:
                    Label(self.window,text = attrib).grid(row=self.i,column=0)
                    value = StringVar() 
                    entree = Entry(self.window, textvariable=value, width=30)
                    entree.grid(row=self.i,column=1)
                    self.dico[attrib] = entree
                    self.i =self.i+1
            else:
                
                Label(self.window,text = "nom").grid(row=self.i,column=0)
                value = StringVar() 
                entree = Entry(self.window, textvariable=value, width=30)
                entree.grid(row=self.i,column=1)
                self.dico["nom"] = entree
                self.i =self.i+1
                Label(self.window,text = "Description").grid(row=self.i,column=0)
                value = StringVar() 
                entree = Entry(self.window, textvariable=value, width=30)
                entree.grid(row=self.i,column=1)
                self.dico["Description"] = entree
                self.i =self.i+1
                Button(self.window,text="+",command=self.addLine).grid(row=0,column=2)
            self.btn = Button(self.window,text="Sauver",command=self.sauverComp)
            self.btn.grid(row=self.i+1,column=0)
        self.window.mainloop()

    def addLine(self):
        value1 = StringVar() 
        entree1 = Entry(self.window, textvariable=value1, width=30)
        entree1.grid(row=self.i,column=0)
        value = StringVar() 
        entree = Entry(self.window, textvariable=value, width=30)
        entree.grid(row=self.i,column=1)
        self.keyEntree.append(entree1)
        self.valueEntree.append(entree)
        self.i =self.i+1
        self.btn.grid_forget()
        self.btn.grid(row=self.i,column=0)

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
            widget.pack_forget()

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

    def sauverSort(self):
        i=0
        for entree in self.keyEntree:
            self.dico[entree.get()]=self.valueEntree[i]
            i =i+1
        for keys in self.dico.keys():
            self.dico[keys]=self.dico[keys].get()
        descr = self.dico["Description"]
        self.dico.pop("Description")
        self.dico["Description"]=descr
        queue.append(("SAVE_SORT",self.dico))
        self.window.destroy()

    def sauverObjet(self):
        i=0
        for entree in self.keyEntree:
            self.dico[entree.get()]=self.valueEntree[i]
            i =i+1
        for keys in self.dico.keys():
            self.dico[keys]=self.dico[keys].get()
        descr = self.dico["Description"]
        self.dico.pop("Description")
        self.dico["Description"]=descr
        queue.append(("SAVE_OBJET",self.dico))
        self.window.destroy()

    def sauverComp(self):
        i=0
        for entree in self.keyEntree:
            self.dico[entree.get()]=self.valueEntree[i]
            i =i+1
        for keys in self.dico.keys():
            self.dico[keys]=self.dico[keys].get()
        descr = self.dico["Description"]
        self.dico.pop("Description")
        self.dico["Description"]=descr
        queue.append(("SAVE_COMPETANCE",self.dico))
        self.window.destroy()

    def sauverArmure(self):
        i=0
        for entree in self.keyEntree:
            self.dico[entree.get()]=self.valueEntree[i]
            i =i+1
        for keys in self.dico.keys():
            self.dico[keys]=self.dico[keys].get()
        descr = self.dico["Description"]
        self.dico.pop("Description")
        self.dico["Description"]=descr
        queue.append(("SAVE_ARMURE",self.dico))
        self.window.destroy()

    def sauverArme(self):
        i=0
        for entree in self.keyEntree:
            self.dico[entree.get()]=self.valueEntree[i]
            i =i+1
        for keys in self.dico.keys():
            self.dico[keys]=self.dico[keys].get()
        descr = self.dico["Description"]
        self.dico.pop("Description")
        self.dico["Description"]=descr
        queue.append(("SAVE_ARME",self.dico))
        self.window.destroy()

    def pack(self):
        self.window.pack()

    def grid(self,**kwargs):
        self.window.grid(kwargs)
        
    def grid_forget(self):
        self.window.pack_forget()

    def place(self,**kwargs):
        self.window.place(kwargs)
