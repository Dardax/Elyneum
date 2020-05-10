
from Transceiver import Transceiver
from Combat import Combat
from Collection import Collection
from Personnage import Personnage

class Partie(object):
    
    def __init__(self, nom=""):
        self.collection= Collection("Algarn")
        self.transceiver = Transceiver("Algarn")
        self.nom = nom
        self.combats = []

    def sauvegarder(self):
        self.transceiver.sauvegarder(self)

    def create_combat(self,nom):
        self.combats.append(Combat())
        self.combats[-1].rename(nom)

    def addCombat(self,combat):
        self.combats.append(combat)

    def getNom(self):
        return self.nom

    def getCombats(self):
        return self.combats