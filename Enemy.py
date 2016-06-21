from random import *

#The Enemy class closely resemble the Player class
#It is the template on which enemies are created

class Enemy:
    #Base Stats for all enemies
    name = "Goblin"
    health = 4
    maxHealth = 4
    attack = 0
    defense = 0
    initiative = 0
    initMod = 0
    alive = True

    def __init__(self, HP, ATK, DEF, INIT):
        self.maxHealth = HP
        self.health = HP
        self.attack = ATK
        self.defense = DEF
        self.initMod = INIT

    #rolls a D6 to determine damage
    def attackRoll(self):
        diceRoll = randint(1,6)
        atkRoll = self.attack + diceRoll
        return atkRoll

    #rolls a D6 for initiative
    def rollInit(self):
        roll = randint(1, 6) + self.initMod
        self.initiative = roll
        return roll

    #Causes enemy to lose health on attack
    def takeDamage(self, nmeATK):
        dmg = (nmeATK - self.defense)
        if dmg > 0:
            self.health = self.health - (nmeATK - self.defense)
        if self.health <= 0:
            self.alive = False

    def attackTurn(self, e):
        hit = self.attackRoll()
        e.takeDamage(hit)