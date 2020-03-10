import Personnage
import XML_Transceiver
import Combat
import Collection

perso = Personnage.Personnage("","","","","","","","","","","Testes1","","","")
perso1 = Personnage.Personnage("","","","","","","","","","","Testes2","","","")
perso2 = Personnage.Personnage("","","","","","","","","","","Testes3","","","")

transceiver = XML_Transceiver.XML_Transceiver("Algarn")
perso.addComp(("Accrobatie", "tu vol"))
perso.addSpell(("FireBall", "Lance une boule de feu"))
perso.addEquip(("Epée","quicoupe"))
perso.addInvent(("Corde","Pour se pendre"))
transceiver.sauver_personnage(perso)
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
    "nom" : "accrobatie",
    "cout":"3",
    "Description" : "fait des sauts"
    }
objet={
    "nom" : "corde",
    "Description" : "3m"
    }

transceiver.sauver_arme(arme)
arme["nom"] = "2eme"
transceiver.sauver_arme(arme)

transceiver.sauver_armure(armure)
transceiver.sauver_competance(competance)
transceiver.sauver_sort(sort)
transceiver.sauver_objet(objet)

combat = Combat.Combat()
combat.addMonster(perso)
combat.addMonster(perso1)
combat.addMonster(perso2)
combat.commencer()
collec = Collection.Collection("Algarn")
collec.reload_perso()
collec.reload_armure()