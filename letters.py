from random import random
from turtle import *

defaultSpeed = 500


def espacemment():
    up()
    forward(30)


def a():
    down()
    left(60)
    forward(80)
    right(130)
    forward(80)

    up()
    right(180)
    forward(40)
    left(70)

    down()
    forward(35)

    up()
    left(90)
    forward(30)
    left(90)
    forward(50)


def u():
    up()
    left(90)
    forward(70)
    right(180)

    down()
    forward(65)

    for x in range(18):
        forward(1)
        left(5)

    forward(20)

    for x in range(18):
        forward(1)
        left(5)

    forward(65)

    up()
    left(180)
    forward(80)
    left(90)


def s():
    down()
    forward(30)

    for x in range(60):
        forward(1)
        left(3)

    forward(20)

    for x in range(60):
        forward(1)
        right(3)
    forward(35)

    up()
    right(90)
    forward(70)
    left(90)


letters = [a, espacemment, u, espacemment, s, espacemment, a]


def signature():
    for i in range(len(letters)):
        pencolor(random(), random(), random())
        letters[i]()
