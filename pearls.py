from turtle import *
import math
from random import *

defaultColor = "black"


def perleA(rayon, couleur):
    
    down()
    circle(rayon)  # Trace un cercle de rayon "rayon"
    fillcolor(couleur)  # Défini la couleur de remplissage par "couleur"

    up()  # Lève le stylo
    left(90)  # Se recentre
    forward(rayon)  # Va au centre du cercle
    backward(rayon / 2)  # Va à la première position du tracé
    right(45)  # S'oriente pour tracer le carré

    down()  # Pose le stylo

    begin_fill()  # Pos1 du fill

    for i in range(4):  # Boucle qui trace le carré
        forward(math.sqrt((rayon / 2) ** 2 + (rayon / 2) ** 2))  # Ligne qui s'occupe de créer les côtés du carré
        left(90)  # Ligne qui s'occuppe de se tourner

    end_fill()  # Pos2 du fill (fin du fill)

    up()  # Lève le stylo (se placer en pos de fin)
    right(45 + 90)  # Tourne de 45+90
    forward(rayon / 2)  # Se replace en desous du cercle
    right(180)  # Se recentre

    fillcolor(defaultColor)  # Reset de la couleur de fill


def perleB(rayon, couleur):
    circle(rayon)  # Trace un cercle de rayon "rayon"
    fillcolor(couleur)  # Défini la couleur de remplissage par "couleur"

    up()  # Lève le stylo
    left(90)  # Se recentre
    forward(rayon)  # Va au centre du cercle
    forward(rayon / 3)  # Va à la première position du tracé
    right(180 - 30)  # S'oriente pour tracer la goutte

    down()                  # Baisse le stylo
    begin_fill()            # Commence le remplissage
    forward(rayon / 2)      # Fait la première paroie

    right(30)               # Tourne de 30°
    circle(-rayon / 4, 180) # trace le demi cerle

    left(-30)               # Se tourne pour tracer 2e paroie
    forward(rayon / 2)      # Tracer de la 2e paroie
    end_fill()              # Fini le remplissage
    
    up()
    left(210)
    forward(rayon)
    forward(rayon / 3)
    left(180)
    
    fillcolor(defaultColor)  # Reset de la couleur de fill


def perleC(rayon, couleur, n):
    
    down()
    circle(rayon)  # Trace un cercle de rayon "rayon"
    fillcolor(couleur)  # Défini la couleur de remplissage par "couleur"
    left(90)
    up()
    forward(rayon)
    left(180)
    
    for i in range(1,n+1):
        up()
        forward(rayon/n)
        
        down()
        left(90)
        if i%2 != 0: begin_fill()
        circle(rayon*i/n)
        if i%2 == 0: end_fill()
        right(90)
        
    right(180)
    fillcolor(defaultColor)  # Reset de la couleur de fill
        
        
def perleD(rayon, couleur):
    
    down()
    circle(rayon)  # Trace un cercle de rayon "rayon"
    fillcolor(couleur)  # Défini la couleur de remplissage par "couleur"
    left(90)
    up()
    forward(rayon)
    left(180)
    
    for i in range(3, 1, -1):
        up()
        forward(rayon/i)
        
        down()
        left(90)
        if i%2 != 0: begin_fill()
        circle(rayon/i)
        if i%2 == 0: end_fill()
        right(90)
    
    up()
    left(180)
    forward(rayon)
    
    down()
    for i in range(2):
        a = 1
        begin_fill()
        if i == 0 : a = -1
        circle((rayon/3)*a)
        end_fill()
    
    up()
    left(180)
    forward(rayon+rayon/6)
    left(180)
    
    fillcolor(defaultColor)  # Reset de la couleur de fill