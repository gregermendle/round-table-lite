#!/usr/bin/python
from random import *
import pdb
from decimal import *
from Enemy import *
from Player import *


def attackTurn(p, e):
    hit = p.attackRoll()
    e.takeDamage(hit)


def healingSpell(h, p):
    p.health += h.castSpell(2)


def damageSpell(p, e):
    e.takeDamage(p.castSpell(2))

for he in range(5, 21):
    for hp in range(8, 14):
        human = Player(hp, 0, 0, 0)
        baddie = Enemy(he, 0, 0, 0)
        battles = 0
        humanWins = 0
        baddieWin = 0

        def fightSequence():
            # print("Human: HP = ",human.health,"\n")'''
            # print("Baddie: HP = ",baddie.health,"\n")'
            global hp
            global he
            baddie.rollInit()
            human.rollInit()
            spellcasts = 0
            '''if(human.initiative > baddie.initiative):
                print("human will attack first\n")
            else:
                print("baddie will attack first\n")'''
            fight = True
            while fight:
                if(human.initiative >= baddie.initiative):
                    attackTurn(human, baddie)
                    if spellcasts < 3:
                        spellcasts += 1
                        healingSpell(human, human)        # heal implementation
                    # damageSpell(human, baddie)          # flat spell cast
                    # print("human attacks with a score of ",hit,"\n")
                    # print("Baddie's health: ",baddie.health,"\n")
                    # input()
                    if (baddie.health <= 0):
                        fight = False
                    else:
                        attackTurn(baddie, human)
                        if (human.health <= 0):
                            fight = False
                else:
                    attackTurn(baddie, human)
                    if (human.health <= 0):
                        fight = False
                    else:
                        attackTurn(human, baddie)
                        if spellcasts < 3:
                            spellcasts += 1
                            healingSpell(human, human)  # heal implementation
                        # damageSpell(human, baddie)    #flat spell cast
                        if (baddie.health <= 0):
                            fight = False
            if(human.health <= 0):
                global baddieWin
                baddieWin += 1
                # print("Human has died.")
            elif(baddie.health <= 0):
                # print("Baddie is dead.")
                global humanWins
                humanWins += 1

        for i in range(1, 10000):
            fightSequence()
            battles += 1
            human.health = hp
            baddie.health = he
        chance = 100*humanWins/battles
        # print("Enemy HP: ",he,", Chance of Winning:",chance,"%")
        TWOPLACES = Decimal(10) ** -2
        print(Decimal(chance).quantize(TWOPLACES), "%", end="\t")
    print()
