# encoding: utf-8
import xml.etree.ElementTree as ET
import os.path as op

ENTETE_PYTHON = "# encoding: utf-8\nimport Roll\n\nclass Personnage(object):\n\t"


class XML_Transceiver(object):
    """Transceiver appelé depuis le managaer de transceiver pour utiliser des fichiers XML"""

    def __init__(self,sys):
        self.systeme = sys

    def lire_personnage(self,path):
        description =[]
        retour=[]
        competances =[]
        sorts =[]
        equip = []
        inv =[]

        tree = ET.parse(path)
        personnage = tree.getroot()
        carac_princ = personnage.find("Carac_Principal")
        carac_secon = personnage.find("Carac_Secondaire")
        competance = personnage.find("Competance")
        sort = personnage.find("Sort")
        equipement = personnage.find("Equipements")
        inventaire = personnage.find("Inventaire")
        if carac_princ is not None:
            for cara in carac_princ:
                retour.append(cara.text)

        if carac_secon is not None:
            for cara in carac_secon:
                retour.append(cara.text)

        if sort is not None:
            for spell in sort:
                sorts.append(spell.attrib["nom"])

        if equipement is not None:
            for stuff in equipement:
                equip.append(stuff.attrib["nom"])

        if inventaire is not None:
            for objet in inventaire:
                inv.append(objet.attrib["nom"])

        if personnage is not None:
            for objet in personnage.attrib.keys():
                description.append(personnage.attrib[objet])

        return description, retour, competances, sorts, equip, inv

    def lire_armure(self):
        path = "C:\Application\Elyneum\Elyneum\Systeme\\"+self.systeme+"\Collection\Armures.xml"
        tree = ET.parse(path)
        root = tree.getroot()
        tab = []
        dic = {}
        for armors in root:
           for armor in armors.attrib.keys():
               dic[armor] = armors.attrib[armor]
           dic["Description"] = armor.text
           tab.append(dic)
           dic={}
        return tab


    def lire_arme(self):
        path = "C:\Application\Elyneum\Elyneum\Systeme\\"+self.systeme+"\Collection\Armes.xml"
        tree = ET.parse(path)
        root = tree.getroot()
        tab = []
        dic = {}
        for armors in root:
           for armor in armors.attrib.keys():
               dic[armor] = armors.attrib[armor]
           dic["Description"] = armor.text
           tab.append(dic)
           dic={}
        return tab

    def lire_sort(self):
        path = "C:\Application\Elyneum\Elyneum\Systeme\\"+self.systeme+"\Collection\Sorts.xml"
        tree = ET.parse(path)
        root = tree.getroot()
        tab = []
        dic = {}
        for armors in root:
           for armor in armors.attrib.keys():
               dic[armor] = armors.attrib[armor]
           dic["Description"] = armor.text
           tab.append(dic)
           dic={}
        return tab

    def lire_competances(self):
        path = "C:\Application\Elyneum\Elyneum\Systeme\\"+self.systeme+"\Collection\Competances.xml"
        tree = ET.parse(path)
        root = tree.getroot()
        tab = []
        dic = {}
        for armors in root:
           for armor in armors.attrib.keys():
               dic[armor] = armors.attrib[armor]
           dic["Description"] = armor.text
           tab.append(dic)
           dic={}
        return tab
    
    def lire_objet(self):
        path = "C:\Application\Elyneum\Elyneum\Systeme\\"+self.systeme+"\Collection\Objets.xml"
        tree = ET.parse(path)
        root = tree.getroot()
        tab = []
        dic = {}
        for armors in root:
           for armor in armors.attrib.keys():
               dic[armor] = armors.attrib[armor]
           dic["Description"] = armor.text
           tab.append(dic)
           dic={}
        return tab

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
            nom_var=nom_var.lower()
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
        nbCaracPrinc = carac_princ.attrib["nombre"]
        carac_secon = personnage.find("Carac_Secondaire")
        competance = personnage.find("Competances")
        sort = personnage.find("Sorts")
        
       
        
        fichier  = open("Personnage.py","w", encoding='utf-8')
        line = ENTETE_PYTHON
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
        if not "initiative" in tab_carac:
            line2 = line2 + "\n\t\tself.initiative = 0"
        line2 = line2 + "\n\t\tself.nbCaracPrinc = " + nbCaracPrinc
        line2 = line2 + "\n\t\tself.competances = []"
        line2 = line2 + "\n\t\tself.sorts = []"
        line2 = line2 + "\n\t\tself.equipements = []"
        line2 = line2 + "\n\t\tself.inventaire = []"
        
        line = line + "\n\tdef __init__(self, " 
        isfirst = True
        for car in tab_carac:
            if not isfirst: line =line +", "
            isfirst = False
            line = line + car
        for car in personnage.attrib.keys():
            line =line +", "+ car
        line = line + "):"
        line = line + "\n\t\tself.systeme = \""+root.tag+"\""
        line = line + "\n\t\tself.desc = {"
        isfirst = True
        for name in personnage.attrib.keys():
            if not isfirst: line =line +", "
            isfirst = False
            line =line +"\n\t\t\t\""+ name + "\" : \"" + personnage.attrib[name] +"\""
            line_methodepersattrib = "\n\n\tdef get"+name.capitalize()+"(self):\n\t\treturn self." + name  +\
            "\n\n\tdef set"+name.capitalize()+"(self,val):\n\t\tself." + name + " = val"
        line = line + "\n\t\t}"   
        line = line + line2
        
        for name in personnage.attrib.keys():
            line = line + "\n\t\tself.desc[\""+name+"\"] = " + name

        for car in tab_carac:
            line = line + "\n\n\t\tif " + car +" ==\"\" : \n\t\t\t"+ "self." +car + "[\"valeur\"] = Roll.Roll(self, self."+car+"[\"valeur\"])"
            line = line + "\n\t\telse:\n\t\t\t" + "self."+car + "[\"valeur\"] = " + car
   
        line = line + "\n\n\tdef modifier_value(self,nom_long,value):\n\t\tfor carac in self.tab_carac:\n\t\t\tif carac[\"nom_long\"]==nom_long: \
 \n\t\t\t\tcarac[\"valeur\"] = value"
        line = line + line_methodepersattrib
        line = line + "\n\n\tdef addDesc(self, carac, val): \n\t\tself.desc[\"carac\"] = val"
        line = line + "\n\n\tdef getDesc(self): \n\t\treturn self.desc"
        line = line + "\n\n\tdef getCar(self): \n\t\treturn self.tab_carac"
        line = line + "\n\n\tdef addSpell(self, sort): \n\t\tself.sorts.append(sort)"
        line = line + "\n\n\tdef getSpell(self): \n\t\treturn self.sorts"
        line = line + "\n\n\tdef addComp(self, comp): \n\t\tself.competances.append(comp)"
        line = line + "\n\n\tdef getComp(self): \n\t\treturn self.competances"
        line = line + "\n\n\tdef addEquip(self, equip): \n\t\tself.equipements.append(equip)"
        line = line + "\n\n\tdef getEquip(self): \n\t\treturn self.equipements"
        line = line + "\n\n\tdef addInvent(self, invent): \n\t\tself.inventaire.append(invent)"
        line = line + "\n\n\tdef getinvent(self): \n\t\treturn self.inventaire"
        fichier.write(line)
        fichier.close()
        

    def sauver_personnage(self, personnage):
        line ="<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<Personnage"
        desc = personnage.getDesc()
        for car in desc.keys():
            line = line +" "+car+"=\""+ desc[car]+"\""
        line = line + ">\n\t<Carac_Principal>"
        nbCarPrin = personnage.nbCaracPrinc
        for i in range(nbCarPrin):
            line = line + "\n\t\t<Carac"
            attrib_list = personnage.tab_carac[i].keys()
            for attrib in attrib_list:
                if attrib != "valeur":
                    line = line + " " + attrib + "=\"" + personnage.tab_carac[i][attrib]+"\""
                else:
                    line = line + ">" + str(personnage.tab_carac[i]["valeur"]) + "</Carac>"
        line = line + "\n\t</Carac_Principal>\n\t<Carac_Secondaire>"
        for i in range(len(personnage.tab_carac)-nbCarPrin):
            line = line + "\n\t\t<Carac"
            attrib_list = personnage.tab_carac[i+nbCarPrin].keys()
            for attrib in attrib_list:
                if attrib != "valeur":
                    line = line + " " + attrib + "=\"" + personnage.tab_carac[i+nbCarPrin][attrib]+"\""
                else:
                    line = line + ">" + str(personnage.tab_carac[i+nbCarPrin]["valeur"]) + "</Carac>"
        line = line +"\n\t</Carac_Secondaire>\n\t<Competances>"
        for val in personnage.competances:
            line = line + "\n\t\t<Competance nom=\""+val[0]+"\">"+val[1]+"</Competance>"
        line = line +"\n\t</Competances>\n\t<Sorts>"
        for val in personnage.sorts:
            line = line + "\n\t\t<Sort nom=\""+val[0]+"\">"+val[1]+"</Sort>"
        line = line +"\n\t</Sorts>\n\t<Equipements>"
        for val in personnage.equipements:
            line = line + "\n\t\t<Equipement nom=\""+val[0]+"\">"+val[1]+"</Equipement>"
        line = line +"\n\t</Equipements>\n\t<Inventaire>"
        for val in personnage.inventaire:
            line = line + "\n\t\t<Objet nom=\""+val[0]+"\">"+val[1]+"</Objet>"
        line = line +"\n\t</Inventaire>\n</Personnage>"
        fichier = open("C:\Application\Elyneum\Elyneum\Systeme\\"+personnage.systeme+"\Collection\Personnage\\"+personnage.desc["nom"]+".xml","w", encoding='utf-8')
        fichier.write(line)
        fichier.close()

    def sauver_arme(self,arme):
        path = "C:\Application\Elyneum\Elyneum\Systeme\\"+self.systeme+"\Collection\Armes.xml"
        line =""
        
        if not op.isfile(path):
           line = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<Armes>"
        else:
            fichier = open(path,"r", encoding='utf-8')
            line = line + fichier.read()[:-9]
            fichier.close()
        line = line+ "\n\t<Arme"
        for attribut in arme.keys():
            if attribut != "Description":
                line = line +" "+attribut+"=\""+arme[attribut]+"\""
            else:
                line = line +">"+arme[attribut]+"</Arme>\n</Armes>"
        fichier = open(path,"w", encoding='utf-8')
        fichier.write(line)
        fichier.close()
        

    def sauver_armure(self, armure):
        path = "C:\Application\Elyneum\Elyneum\Systeme\\"+self.systeme+"\Collection\Armures.xml"
        line =""
        if not op.isfile(path):
           line = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<Armures>"
        else:
            fichier = open(path,"r", encoding='utf-8')
            line = line + fichier.read()[:-11]
            fichier.close()
        line = line+ "\n\t<Armure"
        for attribut in armure.keys():
            if attribut != "Description":
                line = line +" "+attribut+"=\""+armure[attribut]+"\""
            else:
                line = line +">"+armure[attribut]+"</Armure>\n</Armures>"
        fichier = open(path,"w", encoding='utf-8')
        fichier.write(line)
        fichier.close()

    def sauver_competance(self,competance):
        path = "C:\Application\Elyneum\Elyneum\Systeme\\"+self.systeme+"\Collection\Competances.xml"
        line =""
        if not op.isfile(path):
           line = "<?xml version=\"1.0\" encoding=\"utf-8\"?><Competances>"
        else:
            fichier = open(path,"r", encoding='utf-8')
            line = line + fichier.read()[:-15]
            fichier.close()
        line = line+ "\n\t<Competance"
        for attribut in competance.keys():
            if attribut != "Description":
                line = line +" "+attribut+"=\""+competance[attribut]+"\""
            else:
                line = line +">"+competance[attribut]+"</Competance>\n</Competances>"
        fichier = open(path,"w", encoding='utf-8')
        fichier.write(line)
        fichier.close()

    def sauver_sort(self,sort):
        path = "C:\Application\Elyneum\Elyneum\Systeme\\"+self.systeme+"\Collection\Sorts.xml"
        line =""
        if not op.isfile(path):
           line = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<Sorts>"
        else:
            fichier = open(path,"r", encoding='utf-8')
            line = line + fichier.read()[:-9]
            fichier.close()
        line = line+ "\n\t<Sort"
        for attribut in sort.keys():
            if attribut != "Description":
                line = line +" "+attribut+"=\""+sort[attribut]+"\""
            else:
                line = line +">"+sort[attribut]+"</Sort>\n</Sorts>"
        fichier = open(path,"w", encoding='utf-8')
        fichier.write(line)
        fichier.close()

    def sauver_objet(self,objet):
        path = "C:\Application\Elyneum\Elyneum\Systeme\\"+self.systeme+"\Collection\Objets.xml"
        line =""
        if not op.isfile(path):
           line = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<Objets>"
        else:
            fichier = open(path,"r", encoding='utf-8')
            line = line + fichier.read()[:-10]
            fichier.close()
        line = line+ "\n\t<Objet"
        for attribut in objet.keys():
            if attribut != "Description":
                line = line +" "+attribut+"=\""+objet[attribut]+"\""
            else:
                line = line +">"+objet[attribut]+"</Objet>\n</Objets>"
        fichier = open(path,"w", encoding='utf-8')
        fichier.write(line)
        fichier.close()

object = XML_Transceiver("Algarn")
object.read_modele("C:/Application/Elyneum/Elyneum/Systeme/Algarn/Modele.xml")