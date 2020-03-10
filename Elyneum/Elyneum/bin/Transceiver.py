import XML_Transceiver

class Transceiver(object):
    """description of class"""
    def __init__(self, systeme):
        self.transceiver = XML_Transceiver.XML_Transceiver(systeme)
        

    def read_modele(self, path):
        self.transceiver.read_modele(path)
       
    def lire_personnage(self,path):
        return self.transceiver.lire_personnage(path)
    
    def lire_armure(self):
        return self.transceiver.lire_armure()

    def sauver_personnage(self, personnage):
        self.transceiver.sauver_personnage(personnage)

    def sauver_arme(self,arme):
        self.transceiver.sauver_arme(arme,self.systeme)

    def sauver_armure(self, armure):
        self.transceiver.sauver_armure(armure, self.systeme)

    def sauver_sort(self, armure):
        self.transceiver.sauver_sort(sort, self.systeme)

    def sauver_competance(self, competance):
        self.transceiver.sauver_competance(competance, self.systeme)

    def sauver_objet(self, objet):
        self.transceiver.sauver_objet(objet, self.systeme)