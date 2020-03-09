import XML_Transceiver

class Transceiver(object):
    """description of class"""
    def __init__(self, systeme):
        self.systeme = systeme
        

    def read_modele(self, path):
        XML_Transceiver.read_modele(path)
       
    def lire_personnage(self,path):
        return XML_Transceiver.lire_personnage(path)

    def sauver_personnage(self, personnage):
        XML_Transceiver.sauver_personnage(personnage)
        pass

    def sauver_arme(self,arme):
        XML_Transceiver.sauver_arme(arme,self.systeme)
        pass

    def sauver_armure(self, armure):
        XML_Transceiver.sauver_armure(armure, self.systeme)
        pass