from tkinter import *
import os
from threading import Thread

class Launcher(object):
    """description of class"""
    def __init__(self):
        self.window= Tk()
        self.window.title("Launcher")
        self.window.geometry("500x500")
        self.bBouton = Button(self.window,command = self.lancer,text="Elyneum")
        self.bBouton.pack(expand=True)
        self.window.mainloop()
        
    def lancer(self):
        Demarrer().start()
        self.window.destroy()

class Demarrer(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        os.system("C:\Application\Elyneum\Elyneum\IHM\MainPage.py")
Launcher()