# encoding: utf-8
import xml.etree.ElementTree as ET
import os
import os.path as op
import time

ENTETE_PYTHON = "# encoding: utf-8\nimport Roll\n\nclass Personnage(object):\n\t"


class XML_Transceiver:
    """Transceiver appelé depuis le managaer de transceiver pour utiliser des fichiers XML"""

    def __init__(self,sys=""):
        self.systeme = sys

    def supprimer_personnage(self, nom):
        path = "C:\Application\Elyneum\Elyneum\Systeme\\"+self.systeme+"\\Collection\\Personnage\\"+nom+".xml" 
        os.remove(path)

    def supprimer_arme(self, nom):
        path = "C:\Application\Elyneum\Elyneum\Systeme\\"+self.systeme+"\\Collection\\Armes.xml" 
        text = ""
        file = open(path,"r")
        lines = file.readlines()
        for line in lines:
            if line.find("nom=\""+nom+"\"") == -1:
                text = text + line
        file.close()
        file=open(path, "w")
        file.write(text)
        file.close()

    def supprimer_armure(self, nom):
        path = "C:\Application\Elyneum\Elyneum\Systeme\\"+self.systeme+"\\Collection\\Armures.xml" 
        text = ""
        file = open(path,"r")
        lines = file.readlines()
        for line in lines:
            if line.find("nom=\""+nom+"\"") == -1:
                text = text + line
        file.close()
        file=open(path, "w")
        file.write(text)
        file.close()

    def supprimer_objet(self, nom):
        path = "C:\Application\Elyneum\Elyneum\Systeme\\"+self.systeme+"\\Collection\\Objets.xml" 
        text = ""
        file = open(path,"r")
        lines = file.readlines()
        for line in lines:
            if line.find("nom=\""+nom+"\"") == -1:
                text = text + line
        file.close()
        file=open(path, "w")
        file.write(text)
        file.close()

    def supprimer_sort(self, nom):
        path = "C:\Application\Elyneum\Elyneum\Systeme\\"+self.systeme+"\\Collection\\Sorts.xml" 
        text = ""
        file = open(path,"r")
        lines = file.readlines()
        for line in lines:
            if line.find("nom=\""+nom+"\"") == -1:
                text = text + line
        file.close()
        file=open(path, "w")
        file.write(text)
        file.close()

    def supprimer_competence(self, nom):
        path = "C:\Application\Elyneum\Elyneum\Systeme\\"+self.systeme+"\\Collection\\Competences.xml" 
        text = ""
        file = open(path,"r")
        lines = file.readlines()
        for line in lines:
            if line.find("nom=\""+nom+"\"") == -1:
                text = text + line
        file.close()
        file=open(path, "w")
        file.write(text)
        file.close()


    def lire_sauvegarde(self, nom):
        #TODO: A refaire
        from Combat import Combat
        from Personnage import Personnage
        from Elyneum import Partie
        path = "C:\Application\Elyneum\Elyneum\Systeme\\"+self.systeme+"\Sauvegarde\\"+nom+".xml" 
        tree = ET.parse(path)
        combats = tree.getroot()
        combats = combats.findall("Combat")
        partie = Partie(nom)
        for combat in combats:
            comb = Combat([],[])
            comb.rename(combat.attrib["nom"])
            comb.turn = combat.attrib["turn"]
            stack =  combat.attrib["stack"]
            joueurs = combat.find("Joueurs")
            monstres = combat.find("Monstres")


            for personnage in joueurs:
                description =[]
                retour=[]
                competances =[]
                sorts =[]
                equip = []
                inv =[]
                carac_princ = personnage.find("Carac_Principal")
                carac_secon = personnage.find("Carac_Secondaire")
                competance = personnage.find("Competances")
                sort = personnage.find("Sorts")
                equipement = personnage.find("Equipements")
                inventaire = personnage.find("Inventaire")
                if carac_princ is not None:
                    for cara in carac_princ:
                        retour.append(cara.text)

                if carac_secon is not None:
                    for cara in carac_secon:
                        retour.append(cara.text)

                if competance is not None:
                    for comp in competance:
                        dic = comp.attrib
                        dic["Description"] = comp.text
                        competances.append(dic)

                if sort is not None:
                    for spell in sort:
                        dic = spell.attrib
                        dic["Description"] = spell.text
                        sorts.append(dic)

                if equipement is not None:
                    for stuff in equipement:
                        dic = stuff.attrib
                        dic["Description"] = stuff.text
                        equip.append(dic)

                if inventaire is not None:
                    for objet in inventaire:
                        dic = objet.attrib
                        dic["Description"] = objet.text
                        inv.append(dic)

                if personnage is not None:
                    for objet in personnage.attrib.keys():
                        description.append(personnage.attrib[objet])
                
                
                perso = Personnage(*retour,*description)
                for comp in competances:
                    perso.addComp(comp)

                for sor in sorts:
                    perso.addSpell(sor)

                for equi in equip:
                    perso.addEquip(equi)
                    
                for objet_n in inv:
                    perso.addInvent(objet_n)

                comb.addPlayer(perso)
        

            for personnage in monstres:
                description =[]
                retour=[]
                competances =[]
                sorts =[]
                equip = []
                inv =[]
                carac_princ = personnage.find("Carac_Principal")
                carac_secon = personnage.find("Carac_Secondaire")
                competance = personnage.find("Competances")
                sort = personnage.find("Sorts")
                equipement = personnage.find("Equipements")
                inventaire = personnage.find("Inventaire")
                if carac_princ is not None:
                    for cara in carac_princ:
                        retour.append(cara.text)

                if carac_secon is not None:
                    for cara in carac_secon:
                        retour.append(cara.text)

                if competance is not None:
                    for comp in competance:
                        dic = comp.attrib
                        dic["Description"] = comp.text
                        competances.append(dic)

                if sort is not None:
                    for spell in sort:
                        dic = spell.attrib
                        dic["Description"] = spell.text
                        sorts.append(dic)

                if equipement is not None:
                    for stuff in equipement:
                        dic = stuff.attrib
                        dic["Description"] = stuff.text
                        equip.append(dic)

                if inventaire is not None:
                    for objet in inventaire:
                        dic = objet.attrib
                        dic["Description"] = objet.text
                        inv.append(dic)

                if personnage is not None:
                    for objet in personnage.attrib.keys():
                        description.append(personnage.attrib[objet])
                
                
                perso = Personnage(*retour,*description)
                for comp in competances:
                    perso.addComp(comp)

                for sor in sorts:
                    perso.addSpell(sor)

                for equi in equip:
                    perso.addEquip(equi)
                    
                for objet_n in inv:
                    perso.addInvent(objet_n)
                comb.addMonster(perso)
            stack = stack.replace("[","").replace("]","").replace(" ","").replace("'","").split(",")
            comb.remake_stack(stack) 
            partie.addCombat(comb)
        return partie

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
        competance = personnage.find("Competances")
        sort = personnage.find("Sorts")
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

        if competance is not None:
            for spell in competance:
                competances.append(spell.attrib["nom"])

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
        tab = []
        if not op.isfile(path):
            return tab
        tree = ET.parse(path)
        root = tree.getroot()
        
        dic = {}
        for armors in root:
           for armor in armors.attrib.keys():
               dic[armor] = armors.attrib[armor]
           dic["Description"] = armors.text
           tab.append(dic)
           dic={}
        return tab

    def lire_arme(self):
        path = "C:\Application\Elyneum\Elyneum\Systeme\\"+self.systeme+"\Collection\Armes.xml"
        tab = []
        if not op.isfile(path):
            return tab
        tree = ET.parse(path)
        root = tree.getroot()
        
        dic = {}
        for armors in root:
           for armor in armors.attrib.keys():
               dic[armor] = armors.attrib[armor]
           dic["Description"] = armors.text
           tab.append(dic)
           dic={}
        return tab

    def lire_sort(self):
        path = "C:\Application\Elyneum\Elyneum\Systeme\\"+self.systeme+"\Collection\Sorts.xml"
        tab=[]
        if not op.isfile(path):
            return tab
        tree = ET.parse(path)
        root = tree.getroot()
        
        dic = {}
        for armors in root:
           for armor in armors.attrib.keys():
               dic[armor] = armors.attrib[armor]
           dic["Description"] = armors.text
           tab.append(dic)
           dic={}
        return tab

    def lire_competance(self):
        tab = []
        path = "C:\Application\Elyneum\Elyneum\Systeme\\"+self.systeme+"\Collection\Competances.xml"
        if not op.isfile(path):
            return tab
        tree = ET.parse(path)
        root = tree.getroot()
        dic = {}
        for armors in root:
           for armor in armors.attrib.keys():
               dic[armor] = armors.attrib[armor]
           dic["Description"] = armors.text
           tab.append(dic)
           dic={}
        return tab
    
    def lire_objet(self):
        tab = []
        path = "C:\Application\Elyneum\Elyneum\Systeme\\"+self.systeme+"\Collection\Objets.xml"
        if not op.isfile(path):
            return tab
        tree = ET.parse(path)
        root = tree.getroot()
        tab = []
        dic = {}
        for armors in root:
           for armor in armors.attrib.keys():
               dic[armor] = armors.attrib[armor]
           dic["Description"] = armors.text
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
            line =line +", "+ car + "=\"\""
        line = line + "getModel=False):"
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
        line = line + "\n\t\tif getModel: return None"
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
            line = line + "\n\t\t<Competance"
            for attribut in val.keys():
                if attribut != "Description":
                    line = line +" "+attribut+"=\""+val[attribut]+"\""
                else:
                    line = line +">"+val[attribut]+"</Competance>"
        line = line +"\n\t</Competances>\n\t<Sorts>"
        for val in personnage.sorts:
            line = line + "\n\t\t<Sort "
            for attribut in val.keys():
                if attribut != "Description":
                    line = line +" "+attribut+"=\""+val[attribut]+"\""
                else:
                    line = line +">"+val[attribut]+"</Sort>"
        line = line +"\n\t</Sorts>\n\t<Equipements>"
        for val in personnage.equipements:
            line = line + "\n\t\t<Equipement "
            for attribut in val.keys():
                if attribut != "Description":
                    line = line +" "+attribut+"=\""+val[attribut]+"\""
                else:
                    line = line +">"+val[attribut]+"</Equipement>"
        line = line +"\n\t</Equipements>\n\t<Inventaire>"
        for val in personnage.inventaire:
            line = line + "\n\t\t<Objet "
            for attribut in val.keys():
                if attribut != "Description":
                    line = line +" "+attribut+"=\""+val[attribut]+"\""
                else:
                    line = line +">"+val[attribut]+"</Objet>"
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

    def sauvegarder(self, partie):
        path = "C:\Application\Elyneum\Elyneum\Systeme\\"+self.systeme+"\Sauvegarde\\"+partie.getNom().replace(" ","_")+".xml"
        line = "<Partie>"
        combats= partie.getCombats()
        for combat in combats:
            line = line + "\n\t<Combat nom=\""+combat.nom+"\" turn=\""+str(combat.turn)+"\" stack =\""+str(combat.getStack())+"\">"
            line =line + "\n\t\t<Joueurs>"
            for personnage in combat.getPlayers():
                line = line + "\n\t\t\t<Joueur"
                desc = personnage.getDesc()
                for car in desc.keys():
                    line = line +" "+car+"=\""+ desc[car]+"\""
                line = line + ">\n\t\t\t\t<Carac_Principal>"
                nbCarPrin = personnage.nbCaracPrinc
                for i in range(nbCarPrin):
                    line = line + "\n\t\t\t\t\t<Carac"
                    attrib_list = personnage.tab_carac[i].keys()
                    for attrib in attrib_list:
                        if attrib != "valeur":
                            line = line + " " + attrib + "=\"" + personnage.tab_carac[i][attrib]+"\""
                        else:
                            line = line + ">" + str(personnage.tab_carac[i]["valeur"]) + "</Carac>"
                line = line + "\n\t\t\t\t</Carac_Principal>\n\t\t\t\t<Carac_Secondaire>"
                for i in range(len(personnage.tab_carac)-nbCarPrin):
                    line = line + "\n\t\t\t\t\t<Carac"
                    attrib_list = personnage.tab_carac[i+nbCarPrin].keys()
                    for attrib in attrib_list:
                        if attrib != "valeur":
                            line = line + " " + attrib + "=\"" + personnage.tab_carac[i+nbCarPrin][attrib]+"\""
                        else:
                            line = line + ">" + str(personnage.tab_carac[i+nbCarPrin]["valeur"]) + "</Carac>"
                line = line +"\n\t\t\t\t</Carac_Secondaire>\n\t\t\t\t<Competances>"
                for val in personnage.competances:
                    line = line + "\n\t\t\t\t\t<Competance"
                    for attribut in val.keys():
                        if attribut != "Description":
                            line = line +" "+attribut+"=\""+val[attribut]+"\""
                        else:
                            line = line +">"+val[attribut]+"</Competance>"
                line = line +"\n\t\t\t\t</Competances>\n\t\t\t\t<Sorts>"
                for val in personnage.sorts:
                    line = line + "\n\t\t\t\t\t<Sort"
                    for attribut in val.keys():
                        if attribut != "Description":
                            line = line +" "+attribut+"=\""+val[attribut]+"\""
                        else:
                            line = line +">"+val[attribut]+"</Sort>"
                line = line +"\n\t\t\t\t</Sorts>\n\t\t\t\t<Equipements>"
                for val in personnage.equipements:
                    line = line + "\n\t\t\t\t\t<Equipement"
                    for attribut in val.keys():
                        if attribut != "Description":
                            line = line +" "+attribut+"=\""+val[attribut]+"\""
                        else:
                            line = line +">"+val[attribut]+"</Equipement>"
                line = line +"\n\t\t\t\t</Equipements>\n\t\t\t\t<Inventaire>"
                for val in personnage.inventaire:
                    line = line + "\n\t\t\t\t\t<Objet"
                    for attribut in val.keys():
                        if attribut != "Description":
                            line = line +" "+attribut+"=\""+val[attribut]+"\""
                        else:
                            line = line +">"+val[attribut]+"</Objet>"
                line = line + "\n\t\t\t\t</Inventaire>\n\t\t\t</Joueur>"
            line = line +"\n\t\t</Joueurs>\n\t\t<Monstres>"
#--------------------------------------------------------------------------------------------------------------------------------
            for personnage in combat.getMonsters():
                line = line + "\n\t\t\t<Monstre"
                desc = personnage.getDesc()
                for car in desc.keys():
                    line = line +" "+car+"=\""+ desc[car]+"\""
                line = line + ">\n\t\t\t\t<Carac_Principal>"
                nbCarPrin = personnage.nbCaracPrinc
                for i in range(nbCarPrin):
                    line = line + "\n\t\t\t\t\t<Carac"
                    attrib_list = personnage.tab_carac[i].keys()
                    for attrib in attrib_list:
                        if attrib != "valeur":
                            line = line + " " + attrib + "=\"" + personnage.tab_carac[i][attrib]+"\""
                        else:
                            line = line + ">" + str(personnage.tab_carac[i]["valeur"]) + "</Carac>"
                line = line + "\n\t\t\t\t</Carac_Principal>\n\t\t\t\t<Carac_Secondaire>"
                for i in range(len(personnage.tab_carac)-nbCarPrin):
                    line = line + "\n\t\t\t\t\t<Carac"
                    attrib_list = personnage.tab_carac[i+nbCarPrin].keys()
                    for attrib in attrib_list:
                        if attrib != "valeur":
                            line = line + " " + attrib + "=\"" + personnage.tab_carac[i+nbCarPrin][attrib]+"\""
                        else:
                            line = line + ">" + str(personnage.tab_carac[i+nbCarPrin]["valeur"]) + "</Carac>"
                line = line +"\n\t\t\t\t</Carac_Secondaire>\n\t\t\t\t<Competances>"
                for val in personnage.competances:
                    line = line + "\n\t\t\t\t\t<Competance"
                    for attribut in val.keys():
                        if attribut != "Description":
                            line = line +" "+attribut+"=\""+val[attribut]+"\""
                        else:
                            line = line +">"+val[attribut]+"</Competance>"
                line = line +"\n\t\t\t\t</Competances>\n\t\t\t\t<Sorts>"
                for val in personnage.sorts:
                    line = line + "\n\t\t\t\t\t<Sort"
                    for attribut in val.keys():
                        if attribut != "Description":
                            line = line +" "+attribut+"=\""+val[attribut]+"\""
                        else:
                            line = line +">"+val[attribut]+"</Sort>"
                line = line +"\n\t\t\t\t</Sorts>\n\t\t\t\t<Equipements>"
                for val in personnage.equipements:
                    line = line + "\n\t\t\t\t\t<Equipement"
                    for attribut in val.keys():
                        if attribut != "Description":
                            line = line +" "+attribut+"=\""+val[attribut]+"\""
                        else:
                            line = line +">"+val[attribut]+"</Equipement>"
                line = line +"\n\t\t\t\t</Equipements>\n\t\t\t\t<Inventaire>"
                for val in personnage.inventaire:
                    line = line + "\n\t\t\t\t\t<Objet"
                    for attribut in val.keys():
                        if attribut != "Description":
                            line = line +" "+attribut+"=\""+val[attribut]+"\""
                        else:
                            line = line +">"+val[attribut]+"</Objet>"
                line = line + "\n\t\t\t\t</Inventaire>\n\t\t\t</Monstre>"
            line = line +"\n\t\t</Monstres>\n\t</Combat>"
        line = line + "\n</Partie>"
        fichier = open(path,"w", encoding='utf-8')
        fichier.write(line)
        fichier.close()

#transceiver = XML_Transceiver("Algarn")
#transceiver.read_modele("C:\Application\Elyneum\Elyneum\Systeme\Algarn\Modele.xml")
#transceiver.lire_sauvegarde("aLELJD")