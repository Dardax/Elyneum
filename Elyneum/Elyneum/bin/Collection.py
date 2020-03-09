import Transceiver
import os

class Collection(object):
    """description of class"""
    def __init__(self, systeme):
        self.personnages = []
        self.armes = []
        self.armure = []
        self.sorts =[]
        self.competances = []
        self.objet = []
        self.systeme = systeme
        self.transceiver = Transceiver.Transceiver(systeme)

    def reload_perso(self):
        path = "C:\Application\Elyneum\Elyneum\Systeme\\"+self.systeme+"\Collection\Personnage"
        for element in os.listdir(path):
            desc, cara, competances, sorts, equip, inv = self.transceiver.lire_personnage(path+"\\"+element)
            perso = Personnage(*cara,*desc)
            for comp in competances:
                for com in self.competances:
                    if com["nom"]==comp:
                        perso.addComp(com)
            for sor in sorts:
                for s in self.sorts:
                    if s["nom"]==sor:
                        perso.addSpell(s)
            for equi in equi:
                for arme in self.armes:
                    if arme["nom"]==equi:
                        perso.addEquip(arme)
                for armure in self.armure:
                    if armure["nom"]==equi:
                        perso.addEquip(armure)
            for objet_n in inv:
                for obj in self.objet:
                    if obj["nom"]==objet_n:
                        perso.addInvent(obj)

    def reload_armure(self):
        path = "C:\Application\Elyneum\Elyneum\Systeme\\"+self.systeme+"\Collection\Armures.xml"

    def reload_arme(self):
        pass

    def reload_sort(self):
        pass

    def reload_competances(self):
        pass
    
    def reload_objet(self):
        pass

