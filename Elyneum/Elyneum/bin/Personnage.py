# encoding: utf-8
import roll from Roll.py

class Personnage(object):
	
	mForce = {
		"nom_long" : "Force",
		"nom_court" : "FOR"
		"valeur" : "30+1d50"
	}
	mAgilite = {
		"nom_long" : "Agilité",
		"nom_court" : "AGI"
		"valeur" : "30+1d50"
	}
	mIntelligence = {
		"nom_long" : "Intelligence",
		"nom_court" : "INT"
		"valeur" : "30+1d50"
	}
	mCharisme = {
		"nom_long" : "Charisme",
		"nom_court" : "CHA"
		"valeur" : "30+1d50"
	}
	mPerseption = {
		"nom_long" : "Perseption",
		"nom_court" : "PER"
		"valeur" : "30+1d50"
	}
	mPoint_de_vie = {
		"nom_long" : "Point de vie",
		"nom_court" : "PV"
		"valeur" : "FOR/3"
	}
	mPoint_de_mana = {
		"nom_long" : "Point de mana",
		"nom_court" : "PM"
		"valeur" : "INT/10"
	}
	mEsquive = {
		"nom_long" : "Esquive",
		"nom_court" : "Esq"
		"valeur" : "AGI/2"
	}
	mParade = {
		"nom_long" : "Parade",
		"nom_court" : "Par"
		"valeur" : "AGI/10"
	}
	mArmure = {
		"nom_long" : "Armure",
		"nom_court" : "Arm"
		"valeur" : ""
	}
	tab_carac = [mForce, mAgilite, mIntelligence, mCharisme, mPerseption, mPoint_de_vie, mPoint_de_mana, mEsquive, mParade, mArmure]
	competances = []
	sorts = []
	equipements = []
	inventaire = []
	def __init__(self, Force, Agilite, Intelligence, Charisme, Perseption, Point_de_vie, Point_de_mana, Esquive, Parade, Armure):

		if Force =="" : 
			mForce["valeur"] = Roll(self, mForce["valeur"])
		else:
			mForce["valeur"] = Force

		if Agilite =="" : 
			mAgilite["valeur"] = Roll(self, mAgilite["valeur"])
		else:
			mAgilite["valeur"] = Agilite

		if Intelligence =="" : 
			mIntelligence["valeur"] = Roll(self, mIntelligence["valeur"])
		else:
			mIntelligence["valeur"] = Intelligence

		if Charisme =="" : 
			mCharisme["valeur"] = Roll(self, mCharisme["valeur"])
		else:
			mCharisme["valeur"] = Charisme

		if Perseption =="" : 
			mPerseption["valeur"] = Roll(self, mPerseption["valeur"])
		else:
			mPerseption["valeur"] = Perseption

		if Point_de_vie =="" : 
			mPoint_de_vie["valeur"] = Roll(self, mPoint_de_vie["valeur"])
		else:
			mPoint_de_vie["valeur"] = Point_de_vie

		if Point_de_mana =="" : 
			mPoint_de_mana["valeur"] = Roll(self, mPoint_de_mana["valeur"])
		else:
			mPoint_de_mana["valeur"] = Point_de_mana

		if Esquive =="" : 
			mEsquive["valeur"] = Roll(self, mEsquive["valeur"])
		else:
			mEsquive["valeur"] = Esquive

		if Parade =="" : 
			mParade["valeur"] = Roll(self, mParade["valeur"])
		else:
			mParade["valeur"] = Parade

		if Armure =="" : 
			mArmure["valeur"] = Roll(self, mArmure["valeur"])
		else:
			mArmure["valeur"] = Armure

	def modifier_value(self,nom_long,value):
		for carac in tab_carac:
			if carac["nom_long"]==nom_long: carac["valeur"] = value

	def getCar(self): 
		return tab_carac

	def addSpell(self, sort): 
		sorts.append(sort)

	def getSpell(self): 
		return sorts

	def addComp(self, comp): 
		competances.append(comp)

	def getComp(self): 
		return competances

	def addEquip(self, equi): 
		equipements.append(equip)

	def getEquip(self): 
		return equipements

	def addInvent(self, invent): 
		inventaire.append(invent)

	def getinvent(self): 
		return inventaire