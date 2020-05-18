import Transceiver
import Personnage
import os

class Collection:
    """description of class"""
    def __init__(self, systeme):
        self.personnages = []
        self.armes = []
        self.armures = []
        self.sorts =[]
        self.competances = []
        self.objets = []
        self.systeme = systeme
        self.transceiver = Transceiver.Transceiver(systeme)

    def sauver_personnage(self,personnage):
        self.transceiver.sauver_personnage(personnage)

    def reload_perso(self):
        self.personnages=[]
        path = "C:\Application\Elyneum\Elyneum\Systeme\\"+self.systeme+"\Collection\Personnage"
        for element in os.listdir(path):
            desc, cara, competances, sorts, equip, inv = self.transceiver.lire_personnage(path+"\\"+element)
            perso = Personnage.Personnage(*cara,*desc)
            for comp in competances:
                for com in self.competances:
                    if com["nom"]==comp:
                        perso.addComp(com)
            for sor in sorts:
                for s in self.sorts:
                    if s["nom"]==sor:
                        perso.addSpell(s)
            for equi in equip:
                for arme in self.armes:
                    if arme["nom"]==equi:
                        perso.addEquip(arme)
                for armure in self.armures:
                    if armure["nom"]==equi:
                        perso.addEquip(armure)
            for objet_n in inv:
                for obj in self.objets:
                    if obj["nom"]==objet_n:
                        perso.addInvent(obj)
            self.personnages.append(perso)

    def reload_armure(self):
        path = "C:\Application\Elyneum\Elyneum\Systeme\\"+self.systeme+"\Collection\Armures.xml"
        self.armures = self.transceiver.lire_armure()

    def reload_arme(self):
        path = "C:\Application\Elyneum\Elyneum\Systeme\\"+self.systeme+"\Collection\Armes.xml"
        self.armes = self.transceiver.lire_arme()

    def reload_sort(self):
        path = "C:\Application\Elyneum\Elyneum\Systeme\\"+self.systeme+"\Collection\Sorts.xml"
        self.sorts = self.transceiver.lire_sort()

    def reload_competances(self):
        path = "C:\Application\Elyneum\Elyneum\Systeme\\"+self.systeme+"\Collection\Competances.xml"
        self.competances = self.transceiver.lire_competance()
    
    def reload_objet(self):
        path = "C:\Application\Elyneum\Elyneum\Systeme\\"+self.systeme+"\Collection\Objets.xml"
        self.objets = self.transceiver.lire_objet()

