
from Transceiver import Transceiver
from Personnage import Personnage
from Combat import Combat
from Elyneum import Partie
from Collection import Collection
from PyQt5.QtCore import *

transceiver = Transceiver("Algarn")
transceiver.read_modele("C:\Application\Elyneum\Elyneum\Systeme\Algarn\Modele.xml")

perso = Personnage("","","","","","","","","","0","Testes1","","","")
perso1 = Personnage("","","","","","","","","","2","Testes2","","","")
perso2 = Personnage("","","","","","","","","","1","Testes3","","","")



arme = {"nom": "lepoulet",
        "degat":"1d5",
        "modificateur":"+5",
        "effet":"deviens rouge",
        "Description":"desc"}

armure = {"nom": "lepoulet",
        "armure":"15",
        "effet":"deviens rouge",
        "Description":"desc"}

competance = {
    "nom" : "accrobatie",
    "Description" : "fait des sauts"
    }
sort = {
    "nom" : "boule de feu",
    "cout":"3",
    "Description" : "fait des boom"
    }
objet={
    "nom" : "corde",
    "Description" : "3m"
    }
perso.addComp(competance)
perso.addSpell(sort)
perso.addEquip(arme)
perso.addInvent(objet)
transceiver.sauver_personnage(perso)
transceiver.sauver_personnage(perso1)
transceiver.sauver_personnage(perso2)

transceiver.sauver_arme(arme)
arme["nom"] = "2eme"
transceiver.sauver_arme(arme)

transceiver.sauver_armure(armure)
transceiver.sauver_competance(competance)
transceiver.sauver_sort(sort)
transceiver.sauver_objet(objet)

partie = Partie("aLELJD")
combat1 = Combat()
combat1.addPlayer(perso)
combat1.addPlayer(perso1)
combat1.addMonster(perso1)
combat1.addMonster(perso2)
combat1.rename("plouf")
partie.addCombat(combat1)

combat1 = ""
combat2 = Combat([],[])
combat2.addPlayer(perso)
combat2.addMonster(perso1)
combat2.addMonster(perso2)
combat2.rename("plouf2")
combat2.commencer()
partie.addCombat(combat2)

collec = Collection("Algarn")
collec.reload_perso()
collec.reload_armure()
partie.sauvegarder()
partie2 = transceiver.lire_sauvegarde("aLELJD")
partie2.nom = "testeresauv"
partie2.sauvegarder()