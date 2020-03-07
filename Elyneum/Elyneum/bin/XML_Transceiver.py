# encoding: utf-8
import xml.etree.ElementTree as ET
import os.path as op
import Roll

ENTETE = "# encoding: utf-8\nimport roll from Roll.py\n\nclass Personnage(object):\n\t"


class XML_Transceiver(object):
    """Transceiver appelé depuis le managaer de transceiver pour utiliser des fichiers XML"""

    def __init__(self):
        pass


    def read_modele(self, path):
        """Methode de lecture du modele en vue de créer Personnage.py"""
       
        def add_carac(carac):
            isfirst = True;
            line_number =0
            nom_var = carac.attrib["nom_long"]
            print(nom_var)
            nom_var=nom_var.replace("é","e")
            nom_var=nom_var.replace("è","e")
            nom_var=nom_var.replace("ê","e")
            nom_var=nom_var.replace("ù","u")
            nom_var=nom_var.replace("à","a")
            nom_var=nom_var.replace(" ","_")
            nom_var="m"+nom_var
            tab_carac.append(nom_var)
            line = "\n\t" + nom_var + " = {"
            for name in carac.attrib.keys():
                if not isfirst: line =line +","
                isfirst = False
                line_number = line_number + 1
                line =line +"\n\t\t\""+ name + "\" : \"" + carac.attrib[name] + "\""
            text = carac.text
            if text == None: text=""
            line = line +"\n\t\t\"valeur\" : \""+text+"\""
            line = line + "\n\t}"
            return line
            

        tab_carac = []
        if not op.isfile(path):
           print("Fichier inexistant")
           return False
     
        tree = ET.parse(path)
        root = tree.getroot()
        personnage = root.find("Personnage")
        carac_princ = personnage.find("Carac_Principal")
        carac_secon = personnage.find("Carac_Secondaire")
        competance = personnage.find("Competance")
        sort = personnage.find("Sort")
       
        
        fichier  = open("Personnage.py","w", encoding='utf-8')
        line = ENTETE
        for car in carac_princ:
            ret = add_carac(car)
            line = line + ret
        for car in carac_secon:
            ret = add_carac(car)
            line = line + ret
        line=line +"\n\ttab_carac = ["
        isfirst = True
        for car in tab_carac:
            if not isfirst: line =line +", "
            isfirst = False
            line = line + car
        line = line +"]"
        line = line + "\n\tcompetances = []"
        line = line + "\n\tsorts = []"
        line = line + "\n\tequipements = []"
        line = line + "\n\tinventaire = []"
        
        line = line + "\n\tdef __init__(self, "
        isfirst = True
        for car in tab_carac:
            if not isfirst: line =line +", "
            isfirst = False
            line = line + car[1:]
        line = line +"):"
        for car in tab_carac:
            line = line + "\n\n\t\tif " + car[1:] +" ==\"\" : \n\t\t\t"+ car + "[\"valeur\"] = Roll(self, "+car+"[\"valeur\"])"
            line = line + "\n\t\telse:\n\t\t\t" + car + "[\"valeur\"] = " + car[1:]
   
        line = line + "\n\n\tdef modifier_value(self,nom_long,value):\n\t\tfor carac in tab_carac:\n\t\t\tif carac[\"nom_long\"]==nom_long:\
 carac[\"valeur\"] = value"

        line = line + "\n\n\tdef getCar(self): \n\t\treturn tab_carac"
        line = line + "\n\n\tdef addSpell(self, sort): \n\t\tsorts.append(sort)"
        line = line + "\n\n\tdef getSpell(self): \n\t\treturn sorts"
        line = line + "\n\n\tdef addComp(self, comp): \n\t\tcompetances.append(comp)"
        line = line + "\n\n\tdef getComp(self): \n\t\treturn competances"
        line = line + "\n\n\tdef addEquip(self, equi): \n\t\tequipements.append(equip)"
        line = line + "\n\n\tdef getEquip(self): \n\t\treturn equipements"
        line = line + "\n\n\tdef addInvent(self, invent): \n\t\tinventaire.append(invent)"
        line = line + "\n\n\tdef getinvent(self): \n\t\treturn inventaire"
        
        fichier.write(line)
        fichier.close()
        

object = XML_Transceiver()
object.read_modele("C:/Application/Elyneum/Elyneum/Systeme/Algarne/Modele.xml")