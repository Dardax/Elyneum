import re
import random

def Roll(perso,jet):
    result = re.split(r"[+\-*/]",jet)
    for number in result:
        try:
            int(number)
        except(ValueError):
            dice = re.match(r"[0-9]+[dD][0-9]+", number)
            if dice is not None:
                res = re.split(r"[dD]",number)
                multiplicator = int(res[0])
                dice = int(res[1])
                val =  multiplicator * random.randint(1,dice)
                jet = jet.replace(number,str(val),1)
            else:
                try:
                    for cara in perso.getcar():
                        if cara["nom_court"] == number:
                            try:
                                val = int(cara["valeur"])
                                jet = jet.replace(number,val.tostring(),1)
                            except ValueError:
                                return -1
                except AttributeError:
                    return -1
    res = eval(jet)
    return res
print(Roll(152,"155+1d15+agi"))