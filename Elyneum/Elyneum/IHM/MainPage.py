from tkinter import *
from tkinter import ttk
from IHMCollection import Collection
from IHMCombat import Combat
from Presenter import Presenter,queue

class MainPage(object):
    """description of class"""

    def __init__(self):

        self.presenter=Presenter(self.callback)
        
        self.window= Tk()
        self.window.title("Titre")
        self.window.geometry("1920x600")
        self.window.rowconfigure(0,weight = 1)
        self.window.rowconfigure(1,weight = 9)
        self.window.columnconfigure(0,weight=1)
        self.collectionFrame = Collection(self.window)
        self.combatFrame = Combat(self.window)
        self.actualFrame = self.combatFrame

        self.listOption=Frame(self.window,highlightbackground="black",highlightthickness=1,height=50,width=1920)
        self.listOption.rowconfigure(0,weight = 1)
        self.listOption.columnconfigure(0,weight=1)
        self.buttonOpt1 = Button(self.listOption, text="Combat",command =self.switchToCombat)
        self.buttonOpt1.grid(row=0,column=0)
        self.buttonOpt2 = Button(self.listOption, text="Collection",command =self.switchToCollection)
        self.buttonOpt2.grid(row=0,column=1)
        self.listOption.place(x=0,y=0)

        self.actualFrame.place(x=0,y=50)
        
        self.presenter.start()
        queue.append("LOAD_COLLECTION")
        
        self.window.mainloop()
        queue.insert(0,"END")
        

    def switchToCollection(self):
        if self.actualFrame ==self.collectionFrame: return
        self.actualFrame.place_forget()
        self.collectionFrame.place(x=0,y=50)
        self.actualFrame = self.collectionFrame

    def switchToCombat(self):
        if self.actualFrame ==self.combatFrame: return
        self.actualFrame.place_forget()
        self.combatFrame.place(x=0,y=50)
        self.actualFrame = self.combatFrame
    
    def callback(self,com,retour):
        if com=="READ_COL_PERSOS":
            self.collectionFrame.updatePerso(retour)
        elif com=="READ_COL_ARMES": pass
        elif com=="READ_COL_ARMURES": pass
        elif com=="READ_COL_OBJETS":pass
        elif com=="READ_COL_COMPETANCES": pass
        elif com=="READ_COL_SORTS": pass
    

MainPage()