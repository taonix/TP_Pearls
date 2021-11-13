#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from turtle import *
from random import *
import time

import letters as l
import pearls

color = [random(), random(), random()]                                  # Couleur random
functions = [pearls.perleA, pearls.perleB, pearls.perleD]               # Liste de toutes les perles à deux args

pearlCount = randint(3, 5)                                              # Génération du nmbr de Pearls
rayon = (6 - pearlCount) * 10                                           # Rayon statique
necklaceSize = 200                                                      # Taille du collier

reset()                                                                 # Reset de l'affichage

speed(l.defaultSpeed)                                                   # Set de la vitesse


up()                                                                    # Positionemment de
goto(-300, 100)                                                         # la compostion
down()                                                                  # de la signature

l.signature()                                                           # Signature
pencolor(pearls.defaultColor)                                           # Redéfinission de la couleur par défaut pour le collier

up()                                                                    # Positionemment de
goto(-250, 50)                                                          # la compostion
down()                                                                  # du collier


right(50)                                                               # Recentrage
for i in range(pearlCount - 1):                                         # Génération des pearl
    for j in range(necklaceSize // pearlCount):                         # Génération du collier
        down()                                                          # Position écriture
        forward(1)                                                      # Trace le collier
        right(-0.5)                                                     # Défini l'angle de rotation pour le collier
    up()                                                          # lève le stylo
    right(90)                                                     # et se déplace
    forward(rayon * 2)                                            # pour générer
    left(90)                                                      # une nouvelle
    down()                                                        # pearl
    if randint(0, 4) >= 3:                                        # Choisi
        choice(functions)(rayon, color)                           # aléatoiremment
    else:                                                         # les pearl
        pearls.perleC(rayon, color, randint(2, 5))
    up()                                                            # Repositionemment
    forward(rayon * 2)                                              # du
    right(90)                                                       # turtle
    pencolor(pearls.defaultColor)

for i in range(necklaceSize//pearlCount):                         # Finission
    down()                                                        # du collier
    forward(1)                                                    #
    right(-0.5)                                                   #
