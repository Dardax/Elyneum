from tkinter import *
import os
from threading import Thread
import XML_Transceiver

class Launcher(object):
    """description of class"""
    def __init__(self):
        self.window= Tk()
        self.window.title("Launcher")
        self.window.geometry("500x500")
        self.bBouton = Button(self.window,command = self.lancer,text="Algarn")
        self.bBouton.pack(expand=True)
        self.window.mainloop()
        
    def lancer(self):
        transceiver = XML_Transceiver.XML_Transceiver("Algarn")
        transceiver.read_modele("C:\Application\Elyneum\Elyneum\Systeme\Algarn\Modele.xml")
        Demarrer().start()
        self.window.destroy()

class Demarrer(Thread):
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        os.system("python C:\Application\Elyneum\Elyneum\IHM\MainPage.py")
Launcher()