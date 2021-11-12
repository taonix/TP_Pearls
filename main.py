#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from turtle import *
from random import *
import time

import letters as l
import pearls

color = [random(), random(), random()]
functions = [pearls.perleA, pearls.perleB, pearls.perleD]

pearlCount = randint(2, 5)
rayon = (6 - pearlCount) * 10
necklaceSize = 200

reset()

print(pearlCount)

speed(l.defaultSpeed)


up()
goto(-300, 100)
down()

l.signature()
pencolor(pearls.defaultColor)

up()
goto(-300, 50)
down()

right(50)
for i in range(necklaceSize):
    down()
    forward(1)
    right(-0.5)
    if i % (pearlCount/necklaceSize) == 0:
        up()
        right(90)
        forward(rayon * 2)
        left(90)
        down()
        if randint(0, 1) == 0:
            choice(functions)(rayon, color)
        else:
            pearls.perleC(rayon, color, randint(2, 5))
        up()
        forward(rayon * 2)
        right(90)
        pencolor(pearls.defaultColor)

time.sleep(20)
