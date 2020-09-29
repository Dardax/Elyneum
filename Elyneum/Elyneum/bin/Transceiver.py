import XML_Transceiver

class Transceiver:
    """description of class"""
    def __init__(self, systeme):
        self.transceiver = XML_Transceiver.XML_Transceiver(systeme)
        

    def lire_sauvegarde(self,nom):
        return self.transceiver.lire_sauvegarde(nom) 

    def sauvegarder(self,partie):
        self.transceiver.sauvegarder(partie)

    def read_modele(self, path):
        self.transceiver.read_modele(path)
       
    def lire_personnage(self,path):
        return self.transceiver.lire_personnage(path)
    
    def lire_armure(self):
        return self.transceiver.lire_armure()

    def lire_arme(self):
        return self.transceiver.lire_arme()

    def lire_competance(self):
        return self.transceiver.lire_competance()

    def lire_sort(self):
        return self.transceiver.lire_sort()

    def lire_objet(self):
        return self.transceiver.lire_objet()

    def sauver_personnage(self, personnage):
        self.transceiver.sauver_personnage(personnage)

    def sauver_arme(self,arme):
        self.transceiver.sauver_arme(arme)

    def sauver_armure(self, armure):
        self.transceiver.sauver_armure(armure)

    def sauver_sort(self, sort):
        self.transceiver.sauver_sort(sort)

    def sauver_competance(self, competance):
        self.transceiver.sauver_competance(competance)

    def sauver_objet(self, objet):
        self.transceiver.sauver_objet(objet)

    def supprimer_personnage(self, nom):
        self.transceiver.supprimer_personnage(nom)

    def supprimer_armure(self, nom):
        self.transceiver.supprimer_armure(nom)

    def supprimer_arme(self, nom):
        self.transceiver.supprimer_arme(nom)

    def supprimer_objet(self, nom):
        self.transceiver.supprimer_objet(nom)

    def supprimer_competence(self, nom):
        self.transceiver.supprimer_competence(nom)

    def supprimer_sort(self, nom):
        self.transceiver.supprimer_sort(nom)
