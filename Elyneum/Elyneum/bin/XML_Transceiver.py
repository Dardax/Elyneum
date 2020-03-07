# encoding: utf-8
import xml.etree.ElementTree as ET
import os.path as op
#import Roll

ENTETE = "# encoding: utf-8\nimport Roll\n\nclass Personnage(object):\n\t"


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
            nom_var=nom_var.replace("é","e")
            nom_var=nom_var.replace("è","e")
            nom_var=nom_var.replace("ê","e")
            nom_var=nom_var.replace("ù","u")
            nom_var=nom_var.replace("à","a")
            nom_var=nom_var.replace(" ","_")
            nom_var="m"+nom_var
            tab_carac.append(nom_var)
            line = "\n\t\tself." + nom_var + " = {"
            for name in carac.attrib.keys():
                if not isfirst:
                   line =line +","
                isfirst = False
                line_number = line_number + 1
                line =line +"\n\t\t\t\""+ name + "\" : \"" + carac.attrib[name] + "\""
            text = carac.text
            if text == None: text=""
            line = line +",\n\t\t\t\"valeur\" : \"" + text + "\""
            line = line + "\n\t\t}"
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
        line2=""
        
        for car in carac_princ:
            ret = add_carac(car)
            line2 = line2 + ret
        for car in carac_secon:
            ret = add_carac(car)
            line2 = line2 + ret
        line2=line2 +"\n\t\tself.tab_carac = ["
        isfirst = True
        for car in tab_carac:
            if not isfirst: line2 =line2 +", "
            isfirst = False
            line2 = line2 + "self."+car
        line2 = line2 +"]"
        line2 = line2 + "\n\t\tself.competances = []"
        line2 = line2 + "\n\t\tself.sorts = []"
        line2 = line2 + "\n\t\tself.equipements = []"
        line2 = line2 + "\n\t\tself.inventaire = []"
        
        line = line + "\n\tdef __init__(self, " 
        isfirst = True
        for car in tab_carac:
            if not isfirst: line =line +", "
            isfirst = False
            line = line + car[1:]
        line = line +"):"
        line = line + line2
        
        for car in tab_carac:
            line = line + "\n\n\t\tif " + car[1:] +" ==\"\" : \n\t\t\t"+ "self." +car + "[\"valeur\"] = Roll.Roll(self, self."+car+"[\"valeur\"])"
            line = line + "\n\t\telse:\n\t\t\t" + "self."+car + "[\"valeur\"] = " + car[1:]
   
        line = line + "\n\n\tdef modifier_value(self,nom_long,value):\n\t\tfor carac in self.tab_carac:\n\t\t\tif carac[\"nom_long\"]==nom_long: \
 carac[\"valeur\"] = value"

        line = line + "\n\n\tdef getCar(self): \n\t\treturn self.tab_carac"
        line = line + "\n\n\tdef addSpell(self, sort): \n\t\tvsorts.append(sort)"
        line = line + "\n\n\tdef getSpell(self): \n\t\treturn self.sorts"
        line = line + "\n\n\tdef addComp(self, comp): \n\t\tself.competances.append(comp)"
        line = line + "\n\n\tdef getComp(self): \n\t\treturn self.competances"
        line = line + "\n\n\tdef addEquip(self, equi): \n\t\tself.equipements.append(equip)"
        line = line + "\n\n\tdef getEquip(self): \n\t\treturn self.equipements"
        line = line + "\n\n\tdef addInvent(self, invent): \n\t\tself.inventaire.append(invent)"
        line = line + "\n\n\tdef getinvent(self): \n\t\treturn self.inventaire"
        
        fichier.write(line)
        fichier.close()
        

object = XML_Transceiver()
object.read_modele("C:/Application/Elyneum/Elyneum/Systeme/Algarne/Modele.xml")