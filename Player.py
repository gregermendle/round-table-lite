from random import *
import Die


# Player creates a template on which professions are built

class Player:
    # Base stats for player
    health = 8
    maxHealth = 8
    attack = 0
    defense = 0
    initiative = 0
    initMod = 0
    alive = True
    # Skill Checks
    # to be added soon

    def __init__(self, HP, ATK, DEF, INIT):
        self.maxHealth = HP
        self.health = HP
        self.attack = ATK
        self.defense = DEF
        self.initMod = INIT

    # rolls a D6 for damage
    def attackRoll(self):
        diceRoll = randint(1, 6)
        atkRoll = self.attack + diceRoll
        return atkRoll

    # rolls a D6 for initiative
    def rollInit(self):
        roll = randint(1, 6) + self.initMod
        self.initiative = roll
        return roll

    # Causes player to lose health on attack
    def takeDamage(self, nmeATK):
        dmg = (nmeATK - self.defense)
        if dmg > 0:
            self.health = self.health - (nmeATK - self.defense)
        if self.health <= 0:
            self.alive = False

    # what happens when the player deals damage to the enemy
    def attackTurn(self, e):
        hit = self.attackRoll()
        e.takeDamage(hit)

    def revive(self):
        self.alive = True
        self.health = self.maxHealth

    # To be overriden by professsion classes
    def specialAbility(self):
        randint(1, 6)
