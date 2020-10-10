from Elyneum import Partie
from threading import Thread

import time
queue = []
class Presenter(Thread):
    """description of class"""
    def __init__(self,callback):
        Thread.__init__(self)
        self.modele = Partie()
        self.callback=callback
        
        
        
    def run(self):
        end= False
        
        
        while(not end):
            
            if len(queue) != 0:
                commande=queue.pop()
                print("Queue : " + commande[0])

                if commande[0]=="END":   
                    end=True                

                elif commande[0] == "LOAD_COLLECTION":
                    queue.insert(0,("LOAD_ARMES",None))
                    queue.insert(0,("LOAD_ARMURES",None))
                    queue.insert(0,("LOAD_COMPETANCES",None))
                    queue.insert(0,("LOAD_OBJETS",None))
                    queue.insert(0,("LOAD_SORTS",None))
                    queue.insert(0,("LOAD_PERSOS",None))

                elif commande[0] == "LOAD_ARMES": 
                    self.modele.collection.reload_arme()
                    self.callback("READ_COL_ARMES",self.modele.collection.armes)

                elif commande[0] == "LOAD_ARMURES": 
                    self.modele.collection.reload_armure()
                    self.callback("READ_COL_ARMURES",self.modele.collection.armures)

                elif commande[0] == "LOAD_COMPETANCES": 
                    self.modele.collection.reload_competances()
                    self.callback("READ_COL_COMPETANCES",self.modele.collection.competances)

                elif commande[0] == "LOAD_OBJETS": 
                    self.modele.collection.reload_objet()
                    self.callback("READ_COL_OBJETS",self.modele.collection.objets)

                elif commande[0] == "LOAD_SORTS": 
                    self.modele.collection.reload_sort()
                    self.callback("READ_COL_SORTS",self.modele.collection.sorts)

                elif commande[0] == "LOAD_PERSOS": 
                    self.modele.collection.reload_perso()
                    self.callback("READ_COL_PERSOS",self.modele.collection.personnages)

                elif commande[0] == "SAVE_PERSO": 
                    self.modele.collection.sauver_personnage(commande[1])
                    queue.insert(0,("LOAD_PERSOS",None))

                elif commande[0] == "SAVE_SORT": 
                    self.modele.collection.sauver_sort(commande[1])
                    queue.insert(0,("LOAD_SORTS",None))

                elif commande[0] == "SAVE_ARME": 
                    self.modele.collection.sauver_arme(commande[1])
                    time.sleep(1)
                    queue.insert(0,("LOAD_ARMES",None))

                elif commande[0] == "SAVE_ARMURE": 
                    self.modele.collection.sauver_armure(commande[1])
                    queue.insert(0,("LOAD_ARMURES",None))

                elif commande[0] == "SAVE_OBJET": 
                    self.modele.collection.sauver_objet(commande[1])
                    queue.insert(0,("LOAD_OBJETS",None))

                elif commande[0] == "SAVE_COMPETANCE": 
                    self.modele.collection.sauver_competance(commande[1])
                    queue.insert(0,("LOAD_COMPETANCES",None))

                elif commande[0] == "DELETE_PERSONNAGE": 
                    self.modele.collection.supprimer_personnage(commande[1])
                    queue.insert(0,("LOAD_PERSOS",None))
                
                elif commande[0] == "DELETE_ITEM": 
                    if commande[1] == "ARME":
                        self.modele.collection.supprimer_arme(commande[2])
                    elif commande[1] == "ARMURE":
                        self.modele.collection.supprimer_armure(commande[2])
                    elif commande[1] == "COMPETENCE":
                        self.modele.collection.supprimer_competence(commande[2])
                    elif commande[1] == "SORT":
                        self.modele.collection.supprimer_sort(commande[2])
                    elif commande[1] == "OBJET":
                        self.modele.collection.supprimer_objet(commande[2])
                    
                    queue.insert(0,("LOAD_COLLECTION",None))

                elif commande[0]=="ADD_CBT":
                    self.modele.create_combat(commande[1])
                    self.callback("UPDT_CBT_LIST",self.modele.getCombats())   
                    
                elif commande[0]=="ADD_CHAR_TO_CBT":
                    self.modele.addCharToCbt(commande[1])
                    self.callback("LOAD_CBT",self.modele.actualCbt)
                
                elif commande[0]=="SWITCH_CBT":
                    self.modele.setActualCbt(commande[1])
                    self.callback("LOAD_CBT",self.modele.actualCbt)
                
                
            else:
                time.sleep(0.1)
                