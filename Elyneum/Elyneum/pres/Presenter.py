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
                if commande=="END":   
                    end=True                

                elif commande == "LOAD_COLLECTION":
                    queue.insert(0,"LOAD_ARMES")
                    queue.insert(0,"LOAD_ARMURES")
                    queue.insert(0,"LOAD_COMPETANCES")
                    queue.insert(0,"LOAD_OBJETS")
                    queue.insert(0,"LOAD_SORTS")
                    queue.insert(0,"LOAD_PERSOS")
                    

                elif commande == "LOAD_ARMES": 
                    self.modele.collection.reload_arme()
                    self.callback("READ_COL_ARMES",self.modele.collection.armes)

                elif commande == "LOAD_ARMURES": 
                    self.modele.collection.reload_armure()
                    self.callback("READ_COL_ARMURES",self.modele.collection.armures)

                elif commande == "LOAD_COMPETANCES": 
                    self.modele.collection.reload_competances()
                    self.callback("READ_COL_COMPETANCES",self.modele.collection.competances)

                elif commande == "LOAD_OBJETS": 
                    self.modele.collection.reload_objet()
                    self.callback("READ_COL_OBJETS",self.modele.collection.objets)

                elif commande == "LOAD_SORTS": 
                    self.modele.collection.reload_sort()
                    self.callback("READ_COL_SORTS",self.modele.collection.sorts)

                elif commande == "LOAD_PERSOS": 
                    self.modele.collection.reload_perso()
                    self.callback("READ_COL_PERSOS",self.modele.collection.personnages)

                elif commande[0] == "SAVE_PERSO": 
                    self.modele.collection.sauver_personnage(commande[1])
                    queue.insert(0,"LOAD_PERSOS")

                elif commande[0] == "SAVE_SORT": 
                    self.modele.collection.sauver_sort(commande[1])
                    queue.insert(0,"LOAD_SORTS")

                elif commande[0] == "SAVE_ARME": 
                    self.modele.collection.sauver_arme(commande[1])
                    time.sleep(1)
                    queue.insert(0,"LOAD_ARMES")

                elif commande[0] == "SAVE_ARMURE": 
                    self.modele.collection.sauver_armure(commande[1])
                    queue.insert(0,"LOAD_ARMURES")

                elif commande[0] == "SAVE_OBJET": 
                    self.modele.collection.sauver_objet(commande[1])
                    queue.insert(0,"LOAD_OBJETS")

                elif commande[0] == "SAVE_COMPETANCE": 
                    self.modele.collection.sauver_competance(commande[1])
                    queue.insert(0,"LOAD_COMPETANCES")

                elif commande[0] == "DELETE_PERSONNAGE": 
                    self.modele.collection.supprimer_personnage(commande[1])
                    queue.insert(0,"LOAD_PERSOS")
                
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
                    
                    queue.insert(0,"LOAD_COLLECTION")

               
                
                
            else:
                time.sleep(0.1)
                