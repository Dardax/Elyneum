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

    def sauver_sort(self,sort):
        self.transceiver.sauver_sort(sort)
    
    def sauver_arme(self,sort):
        self.transceiver.sauver_arme(sort)
    
    def sauver_armure(self,sort):
        self.transceiver.sauver_armure(sort)
    
    def sauver_objet(self,sort):
        self.transceiver.sauver_objet(sort)
    
    def sauver_competance(self,sort):
        self.transceiver.sauver_competance(sort)

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

    def supprimer_personnage(self, nom):
        for pers in self.personnages:
            if pers.desc["nom"] == nom :
                self.personnages.remove(pers)
                self.transceiver.supprimer_personnage(nom)
                return

    def supprimer_armure(self, nom):
        for arm in self.armures:
            if arm["nom"] == nom:
                self.transceiver.supprimer_armure(nom)
                self.armures.remove(arm)
                return

    def supprimer_arme(self, nom):
        for arm in self.armes:
            if arm["nom"] == nom:
                self.transceiver.supprimer_arme(nom)
                self.armes.remove(arm)
                return

    def supprimer_competence(self, nom):
        for arm in self.competences:
            if arm["nom"] == nom:
                self.transceiver.supprimer_competence(nom)
                self.competences.remove(arm)
                return

    def supprimer_sort(self, nom):
        for arm in self.sorts:
            if arm["nom"] == nom:
                self.transceiver.supprimer_sort(nom)
                self.sorts.remove(arm)
                return

    def supprimer_objet(self, nom):
        for arm in self.objets:
            if arm["nom"] == nom:
                self.transceiver.supprimer_objet(nom)
                self.objets.remove(arm)
                return



