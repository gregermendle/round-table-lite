from Player import *

class Barbarian(Player):
    #something here

class Priest(Player):
    def heal(self,target, amount):
        target.health += amount

class Sorcerer(Player):
    def castSpell(self, target, dmg):
        # roll = randint(1,6)
        # if roll > 3:
        target.takeDamage(dmg)
        # else:
        # return 0

class Scribe(Player):
    #imbued weapon