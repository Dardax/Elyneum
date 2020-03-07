# encoding: utf-8
import Roll

class Personnage(object):
	
	def __init__(self, Force, Agilite, Intelligence, Charisme, Perseption, Point_de_vie, Point_de_mana, Esquive, Parade, Armure):
		self.mForce = {
			"nom_long" : "Force",
			"nom_court" : "FOR",
			"valeur" : "30+1d50"
		}
		self.mAgilite = {
			"nom_long" : "Agilité",
			"nom_court" : "AGI",
			"valeur" : "30+1d50"
		}
		self.mIntelligence = {
			"nom_long" : "Intelligence",
			"nom_court" : "INT",
			"valeur" : "30+1d50"
		}
		self.mCharisme = {
			"nom_long" : "Charisme",
			"nom_court" : "CHA",
			"valeur" : "30+1d50"
		}
		self.mPerseption = {
			"nom_long" : "Perseption",
			"nom_court" : "PER",
			"valeur" : "30+1d50"
		}
		self.mPoint_de_vie = {
			"nom_long" : "Point de vie",
			"nom_court" : "PV",
			"valeur" : "FOR/3"
		}
		self.mPoint_de_mana = {
			"nom_long" : "Point de mana",
			"nom_court" : "PM",
			"valeur" : "INT/10"
		}
		self.mEsquive = {
			"nom_long" : "Esquive",
			"nom_court" : "Esq",
			"valeur" : "AGI/2"
		}
		self.mParade = {
			"nom_long" : "Parade",
			"nom_court" : "Par",
			"valeur" : "AGI/10"
		}
		self.mArmure = {
			"nom_long" : "Armure",
			"nom_court" : "Arm",
			"valeur" : ""
		}
		self.tab_carac = [self.mForce, self.mAgilite, self.mIntelligence, self.mCharisme, self.mPerseption, self.mPoint_de_vie, self.mPoint_de_mana, self.mEsquive, self.mParade, self.mArmure]
		self.competances = []
		self.sorts = []
		self.equipements = []
		self.inventaire = []

		if Force =="" : 
			self.mForce["valeur"] = Roll.Roll(self, self.mForce["valeur"])
		else:
			self.mForce["valeur"] = Force

		if Agilite =="" : 
			self.mAgilite["valeur"] = Roll.Roll(self, self.mAgilite["valeur"])
		else:
			self.mAgilite["valeur"] = Agilite

		if Intelligence =="" : 
			self.mIntelligence["valeur"] = Roll.Roll(self, self.mIntelligence["valeur"])
		else:
			self.mIntelligence["valeur"] = Intelligence

		if Charisme =="" : 
			self.mCharisme["valeur"] = Roll.Roll(self, self.mCharisme["valeur"])
		else:
			self.mCharisme["valeur"] = Charisme

		if Perseption =="" : 
			self.mPerseption["valeur"] = Roll.Roll(self, self.mPerseption["valeur"])
		else:
			self.mPerseption["valeur"] = Perseption

		if Point_de_vie =="" : 
			self.mPoint_de_vie["valeur"] = Roll.Roll(self, self.mPoint_de_vie["valeur"])
		else:
			self.mPoint_de_vie["valeur"] = Point_de_vie

		if Point_de_mana =="" : 
			self.mPoint_de_mana["valeur"] = Roll.Roll(self, self.mPoint_de_mana["valeur"])
		else:
			self.mPoint_de_mana["valeur"] = Point_de_mana

		if Esquive =="" : 
			self.mEsquive["valeur"] = Roll.Roll(self, self.mEsquive["valeur"])
		else:
			self.mEsquive["valeur"] = Esquive

		if Parade =="" : 
			self.mParade["valeur"] = Roll.Roll(self, self.mParade["valeur"])
		else:
			self.mParade["valeur"] = Parade

		if Armure =="" : 
			self.mArmure["valeur"] = Roll.Roll(self, self.mArmure["valeur"])
		else:
			self.mArmure["valeur"] = Armure

	def modifier_value(self,nom_long,value):
		for carac in self.tab_carac:
			if carac["nom_long"]==nom_long:  carac["valeur"] = value

	def getCar(self): 
		return self.tab_carac

	def addSpell(self, sort): 
		vsorts.append(sort)

	def getSpell(self): 
		return self.sorts

	def addComp(self, comp): 
		self.competances.append(comp)

	def getComp(self): 
		return self.competances

	def addEquip(self, equi): 
		self.equipements.append(equip)

	def getEquip(self): 
		return self.equipements

	def addInvent(self, invent): 
		self.inventaire.append(invent)

	def getinvent(self): 
		return self.inventaire