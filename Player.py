from random import *

class Player:
    health = 8
    attack = 0
    defense = 0
    initiative = 0
    initMod = 0

    def __init__(self, HP, ATK, DEF, INIT):
        self.health = HP
        self.attack = ATK
        self.defense = DEF
        self.initMod = INIT

    def attackRoll(self):
        diceRoll = randint(1,6)
        atkRoll = self.attack + diceRoll
        return atkRoll

    def rollInit(self):
        roll = randint(1,6) + self.initMod
        self.initiative = roll

    def takeDamage(self, nmeATK):
        dmg = (nmeATK - self.defense)
        if dmg > 0:
            self.health = self.health - (nmeATK - self.defense)

    def castSpell(self, dmg):
        # roll = randint(1,6)
        # if roll > 3:
        return dmg
        # else:
        # return 0