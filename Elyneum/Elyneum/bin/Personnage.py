# encoding: utf-8
import Roll

class Personnage(object):
	
	def __init__(self, force, agilite, intelligence, charisme, perseption, point_de_vie, point_de_mana, esquive, parade, armure, nom, race, niveau, age):
		self.systeme = "Algarn"
		self.desc = {
			"nom" : "", 
			"race" : "", 
			"niveau" : "", 
			"age" : ""
		}
		self.force = {
			"nom_long" : "Force",
			"nom_court" : "FOR",
			"valeur" : "30+1d50"
		}
		self.agilite = {
			"nom_long" : "Agilité",
			"nom_court" : "AGI",
			"valeur" : "30+1d50"
		}
		self.intelligence = {
			"nom_long" : "Intelligence",
			"nom_court" : "INT",
			"valeur" : "30+1d50"
		}
		self.charisme = {
			"nom_long" : "Charisme",
			"nom_court" : "CHA",
			"valeur" : "30+1d50"
		}
		self.perseption = {
			"nom_long" : "Perseption",
			"nom_court" : "PER",
			"valeur" : "30+1d50"
		}
		self.point_de_vie = {
			"nom_long" : "Point de vie",
			"nom_court" : "PV",
			"valeur" : "FOR/3"
		}
		self.point_de_mana = {
			"nom_long" : "Point de mana",
			"nom_court" : "PM",
			"valeur" : "INT/10"
		}
		self.esquive = {
			"nom_long" : "Esquive",
			"nom_court" : "Esq",
			"valeur" : "AGI/2"
		}
		self.parade = {
			"nom_long" : "Parade",
			"nom_court" : "Par",
			"valeur" : "AGI/10"
		}
		self.armure = {
			"nom_long" : "Armure",
			"nom_court" : "Arm",
			"valeur" : "0"
		}
		self.tab_carac = [self.force, self.agilite, self.intelligence, self.charisme, self.perseption, self.point_de_vie, self.point_de_mana, self.esquive, self.parade, self.armure]
		self.initiative = 0
		self.nbCaracPrinc = 5
		self.competances = []
		self.sorts = []
		self.equipements = []
		self.inventaire = []
		self.desc["nom"] = nom
		self.desc["race"] = race
		self.desc["niveau"] = niveau
		self.desc["age"] = age

		if force =="" : 
			self.force["valeur"] = Roll.Roll(self, self.force["valeur"])
		else:
			self.force["valeur"] = force

		if agilite =="" : 
			self.agilite["valeur"] = Roll.Roll(self, self.agilite["valeur"])
		else:
			self.agilite["valeur"] = agilite

		if intelligence =="" : 
			self.intelligence["valeur"] = Roll.Roll(self, self.intelligence["valeur"])
		else:
			self.intelligence["valeur"] = intelligence

		if charisme =="" : 
			self.charisme["valeur"] = Roll.Roll(self, self.charisme["valeur"])
		else:
			self.charisme["valeur"] = charisme

		if perseption =="" : 
			self.perseption["valeur"] = Roll.Roll(self, self.perseption["valeur"])
		else:
			self.perseption["valeur"] = perseption

		if point_de_vie =="" : 
			self.point_de_vie["valeur"] = Roll.Roll(self, self.point_de_vie["valeur"])
		else:
			self.point_de_vie["valeur"] = point_de_vie

		if point_de_mana =="" : 
			self.point_de_mana["valeur"] = Roll.Roll(self, self.point_de_mana["valeur"])
		else:
			self.point_de_mana["valeur"] = point_de_mana

		if esquive =="" : 
			self.esquive["valeur"] = Roll.Roll(self, self.esquive["valeur"])
		else:
			self.esquive["valeur"] = esquive

		if parade =="" : 
			self.parade["valeur"] = Roll.Roll(self, self.parade["valeur"])
		else:
			self.parade["valeur"] = parade

		if armure =="" : 
			self.armure["valeur"] = Roll.Roll(self, self.armure["valeur"])
		else:
			self.armure["valeur"] = armure

	def modifier_value(self,nom_long,value):
		for carac in self.tab_carac:
			if carac["nom_long"]==nom_long:  
				carac["valeur"] = value

	def getAge(self):
		return self.age

	def setAge(self,val):
		self.age = val

	def addDesc(self, carac, val): 
		self.desc["carac"] = val

	def getDesc(self): 
		return self.desc

	def getCar(self): 
		return self.tab_carac

	def addSpell(self, sort): 
		self.sorts.append(sort)

	def getSpell(self): 
		return self.sorts

	def addComp(self, comp): 
		self.competances.append(comp)

	def getComp(self): 
		return self.competances

	def addEquip(self, equip): 
		self.equipements.append(equip)

	def getEquip(self): 
		return self.equipements

	def addInvent(self, invent): 
		self.inventaire.append(invent)

	def getinvent(self): 
		return self.inventaire