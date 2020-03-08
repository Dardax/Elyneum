import Personnage
import XML_Transceiver

perso = Personnage.Personnage("","","","","","","","","","","Testes","","","")
transceiver = XML_Transceiver.XML_Transceiver()
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

transceiver.sauver_arme(arme,"Algarn")
transceiver.sauver_armure(armure,"Algarn")