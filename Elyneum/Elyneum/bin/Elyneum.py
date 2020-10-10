
from Transceiver import Transceiver
from Combat import Combat
from Collection import Collection
from Personnage import Personnage

class Partie(object):
    
    def __init__(self, nom=""):
        self.collection= Collection("Algarn")
        self.transceiver = Transceiver("Algarn")
        self.nom = nom
        self.actualCbt = None
        self.listCbts = []

    def sauvegarder(self):
        self.transceiver.sauvegarder(self)

    def create_combat(self,nom):
        cbt = Combat()
        cbt.rename(nom)
        self.listCbts.append(cbt)

    def addCombat(self,combat):
        self.listCbts.append(combat)

    def getNom(self):
        return self.nom

    def getCombats(self):
        return self.listCbts

    def setActualCbt(self, cbtName):
        for cbt in self.listCbts:
            if cbt.nom == cbtName:
                self.actualCbt = cbt
                print("set actual cbt : " + cbt.nom)

    def addCharToCbt(self, charName):
        if self.actualCbt != None :
            for perso in self.collection.personnages:
                if perso.desc["nom"] == charName:
                    self.actualCbt.addPlayer(perso)
                    print("Ajouter " + charName + " into " + self.actualCbt.nom)
                    return
