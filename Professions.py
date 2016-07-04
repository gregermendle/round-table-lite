from Player import *
from Enemy import *
from random import *

# The Professions file contains individual classes
# Each class overrides or specifies the attributes of the player based on
# the core Player class


class Barbarian(Player):
    def attackTurn(self, e):
        roll_1 = self.attackRoll()
        roll_2 = self.attackRoll()
        if(roll_1 == roll_2):
            e.takeDamage(roll_1 + roll_2)
        else:
            e.takeDamage(roll_1)


class Drunkard(Player):
    attack = 1
    defense = 1


class Knight(Player):
    attack = 1
    defense = 1


class Priest(Player):
    spellCasts = 0          # tracks the number of times a spell is used

    def heal(self, target, amount):
        target.health += amount


class Ranger(Player):
    initMod = 3


class Rogue(Player):
    initMod = 1

    def takeDamage(self, nmeATK):
        mitigation = randint(1, 6)
        dmg = (nmeATK - self.defense)-mitigation
        if dmg > 0:
            self.health = self.health - dmg
        if self.health <= 0:
            self.alive = False


class Scribe(Player):
    def attackTurn(self, e):
        elementalDmg = randint(1, 2)
        hit = self.attackRoll() + elementalDmg
        e.takeDamage(hit)


class Sorcerer(Player):
    def castSpell(self, target, dmg):
        # roll = randint(1,6)
        # if roll > 3:
        target.takeDamage(dmg)
        # else:
        # return 0
