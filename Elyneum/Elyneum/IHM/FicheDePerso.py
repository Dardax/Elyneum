from tkinter import *
from tkinter import ttk

class FicheDePerso(object):
    """Objet de base pour l'IHM des fiches de perso"""
    def __init__(self, parent,perso):

        self.window= Frame(parent,highlightbackground="black",highlightthickness=1,height=250,width=200)
        
        self.nomPersonnage = Label(self.window,text = perso.desc["nom"])
        self.nomPersonnage.place(x=0,y=0)

        #Frame des caracteristiques
        self.frame = ttk.Frame(self.window)        

        #Caracteristique principal
        labelFor = Label(self.frame,text="FOR :")
        labelFor.grid(row=0,column=0)
        self.LabelvalueFor = Label(self.frame,text=perso.force["valeur"])
        self.LabelvalueFor.grid(row=0,column=1)

        labelDex = Label(self.frame,text="DEX :")
        labelDex.grid(row=1,column=0)
        self.LabelvalueDex = Label(self.frame,text =perso.agilite["valeur"])
        self.LabelvalueDex.grid(row=1,column=1)

        labelInt = Label(self.frame,text="INT :")
        labelInt.grid(row=2,column=0)
        self.LabelvalueInt = Label(self.frame,text=perso.intelligence["valeur"])
        self.LabelvalueInt.grid(row=2,column=1)

        labelCha = Label(self.frame,text="CHA :")
        labelCha.grid(row=3,column=0)
        self.LabelvalueCha = Label(self.frame,text=perso.charisme["valeur"])
        self.LabelvalueCha.grid(row=3,column=1)

        labelPer = Label(self.frame,text="PER :")
        labelPer.grid(row=4,column=0)
        self.LabelvaluePer = Label(self.frame,text=perso.perseption["valeur"])
        self.LabelvaluePer.grid(row=4,column=1)
        
        #Caracteristique secondaire
        labelVie = Label(self.frame,text="HP :")
        labelVie.grid(row=0,column=3)
        self.labelvalueVie = Label(self.frame,text=perso.point_de_vie["valeur"])
        self.labelvalueVie.grid(row=0,column=4)

        labelMana = Label(self.frame,text="MP :")
        labelMana.grid(row=1,column=3)
        self.labelvalueMana = Label(self.frame,text=perso.point_de_mana["valeur"])
        self.labelvalueMana.grid(row=1,column=4)

        labelEsq = Label(self.frame,text="ESQ :")
        labelEsq.grid(row=2,column=3)
        self.LabelvalueEsq = Label(self.frame,text=perso.esquive["valeur"])
        self.LabelvalueEsq.grid(row=2,column=4)

        labelPar = Label(self.frame,text="PAR :")
        labelPar.grid(row=3,column=3)
        self.LabelvaluePar = Label(self.frame,text=perso.parade["valeur"])
        self.LabelvaluePar.grid(row=3,column=4)

        labelArm = Label(self.frame,text="ARM :")
        labelArm.grid(row=4,column=3)
        self.LabelvalueArm = Label(self.frame,text=perso.armure["valeur"])
        self.LabelvalueArm.grid(row=4,column=4)
        #Fin de la frame de caracteristique
        self.frame.place(x=0,y=20)
        self.frame2 =Frame(self.window)
        #Sort et Comp
        labelComp = Label(self.frame2,text="Competances :",justify ="left")
        labelComp.grid(row=0,column=0)
        for i in range(len(perso.competances)):
            self.labelvalueComp=Label(self.frame2,text=perso.competances[i]["nom"])
            self.labelvalueComp.grid(row=i+1,column=0)

        labelSort = Label(self.frame2,text="Sorts:")
        labelSort.grid(row=0, column=1)
        for i in range(len(perso.sorts)):
            self.labelvalueSort = Label(self.frame2,text=perso.sorts[i]["nom"])
            self.labelvalueSort.grid(row=1+i,column=1)
        self.frame2.place(x=0,y=130)

    def pack(self):
        self.window.pack()

    def grid(self,**kwargs):
        self.window.grid(kwargs)

    def place(self,**kwargs):
        self.window.place(kwargs)

    
