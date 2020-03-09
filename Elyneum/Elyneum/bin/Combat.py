import random

class Combat(object):
    """description of class"""
    def __init__(self,joueurs=[],monstres=[]):
    
        self.joueur = joueurs
        self.monstre = monstres
        self.stackIni = []
        self.turn = 0

    def commencer(self):
        self.stackIni = self.monstre + self.joueur
        for perso in self.stackIni :
            perso.initiative = perso.initiative + random.randint(1,20)
        self.tri_bulle(self.stackIni)
        #for j in self.stackIni:
        #    print("{0}:{1}".format(j.desc["nom"],j.initiative))
            
    def nextTurn(self):
        self.turn = self.turn +1
        if self.turn == len(self.stackIni):
            self.turn=0

    def tri_bulle(self,tab):
        n = len(tab)
        # Traverser tous les éléments du tableau
        for i in range(n):
            for j in range(0, n-i-1):
                # échanger si l'élément trouvé est plus grand que le suivant
                if tab[j].initiative < tab[j+1].initiative :
                    tab[j], tab[j+1] = tab[j+1], tab[j]

    def getPlayers(self):
        return self.joueur

    def getPlayer(self, name):
        for play in self.players:
            if name == play.desc["nom"]:
                return play
        return None

    def getMonsters(self):
        return self.monstre

    def getMonster(self,name):
        for monst in self.monstre:
            if name == monstre.desc["nom"]:
                return monst
        return None
    
    def addPlayer(self,player):
        self.joueur.append(player)
        return True

    def addMonster(self, monster):
        self.monstre.append(monster)
        return True

    def isDead(self, perso):
        self.stackIni.remove(perso)