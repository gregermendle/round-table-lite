#!/usr/bin/python
from random import *
import pdb
from decimal import *
from Enemy import *
from Player import *
from Professions import *

totalEncounters = 0
player = Player(8, 0, 0, 0)
selection = input("Select a Class: ")


def choice(x):
    global player
    if x.lower() == "barbarian":
        player = Barbarian(20, 0, 0, 0)
    elif x.lower() == "drunkard":
        player = Drunkard(14, 1, 1, -2)
    elif x.lower() == "knight":
        player = Knight(12, 1, 1, -1)
    elif x.lower() == "priest":
        player = Priest(10, 0, 0, 0)
    elif x.lower() == "ranger":
        player = Ranger(10, 0, 0, 3)
    elif x.lower() == "rogue":
        player = Rogue(8, 0, 0, 1)
    elif x.lower() == "scribe":
        player = Scribe(10, 0, 0, 0)
    elif x.lower() == "sorcerer":
        player = Sorcerer(10, 0, 0, 0)

choice(selection)

while player.alive:
    # spawn enemy
    randy = randint(4, 9)
    creature = Enemy(randy, 0, 0, 0)
    # display enemy stats
    print("Creature HP: ", creature.health)

    # increment encounter number
    totalEncounters = totalEncounters + 1
    # roll for initiative
    player.rollInit()
    creature.rollInit()
    print("Your initiative roll: ", player.initiative)
    print("The creature's initiative roll: ", creature.initiative)
    input()
    # sort the attackOrder List
    # loop the attack phase until either the enemy or player is dead
    while player.alive and creature.alive:
        if player.initiative >= creature.initiative:
            player.attackTurn(creature)
            # print("human attacks with a score of ",hit,"\n")
            # print("Baddie's health: ",baddie.health,"\n")
            # input()
            if creature.alive:
                creature.attackTurn(player)
        else:
            creature.attackTurn(player)
            if player.alive:
                player.attackTurn(creature)

print("You survived ", totalEncounters, " encounters.")
