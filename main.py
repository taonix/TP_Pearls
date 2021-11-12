#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from turtle import *
from random import *
import time

import letters as l
import pearls


def signature():
    l.a()
    l.espacemment()
    l.u()
    l.espacemment()
    l.s()
    l.espacemment()
    l.a()


reset()

color = [random(), random(), random()]
functions = [pearls.perleA, pearls.perleB, pearls.perleD]
pearl = randint(2, 5)
rayon = 50

speed(500)

up()
goto(-300, 100)
down()

# signature()

left(50)
for i in range(pearl * 200):
    down()
    forward(1)
    right(-0.5)
    if i % pearl * 200 == 0 and i != 0 and i != 200:
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

time.sleep(20)
