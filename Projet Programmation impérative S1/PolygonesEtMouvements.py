#Fichier étant utilisé par "le jeu du château". Ecrite par Soler Lillian et Genoud-Duvillaret Benoît.

import random
from turtle import *
from math import *

#Fonction de Base pour dessiner  :


def aller (x,y):
    up()
    goto(x,y)
    down()


def dessineRectangle(longueurCote,largeurCote,couleurTrait,couleurPlein):
    pencolor(couleurTrait)
    fillcolor(couleurPlein)
    begin_fill()
    i=0
    
    while i<2:
        forward(longueurCote)
        left(90)
        forward(largeurCote)
        left(90)
        i=i+1
    end_fill()

def dessineParallélépipède(longueurCote,largeurCote,angle,couleurTrait,couleurPlein):
    pencolor(couleurTrait)
    fillcolor(couleurPlein)
    begin_fill()
    i=0
    while i<2:
        left(angle)
        forward(longueurCote)
        left(90-angle)
        forward(largeurCote)
        left(90)
        i=i+1
    end_fill()

def dessinePolygone(nbCote,longueurCote,épaisseur,couleurTrait,couleurPlein,x,y):
    pencolor(couleurTrait)
    fillcolor(couleurPlein)
    begin_fill()
    width(épaisseur)
    up()
    goto(x,y)
    down()
    angle = 360/nbCote
    k=0
    while k<nbCote:
        right(angle)
        forward(longueurCote)
        k=k+1
    end_fill()

def trapeze(base,haut,hauteur,couleurTrait,couleurPlein):
    pencolor(couleurTrait)
    fillcolor(couleurPlein)
    begin_fill()
    coteBase=(1/2*(base-haut))
    cote=sqrt((hauteur*hauteur)+(coteBase*coteBase))
    angleBas=abs(90-acos(coteBase/cote)*180/pi)                     
    angleHaut=abs(90-angleBas)
    a=angleHaut
    b=angleBas+90

    if base>haut:
        a=angleBas+90
        b=angleHaut
        

    else:
        a=angleHaut
        b=angleBas+90
        
    forward(base)
    left(a)
    forward(cote)
    left(b)
    forward(haut)
    left(b)
    forward(cote)
    left(a)


    end_fill()

def hautTrapeze (base,haut,hauteur):
    up()
    coteBase=(1/2*(base-haut))
    cote=sqrt((hauteur*hauteur)+(coteBase*coteBase))
    angleBas=abs(90-acos(coteBase/cote)*180/pi)                     
    angleHaut=abs(90-angleBas)
    if base>haut:
        left(90-angleBas)
        forward(cote)
        right(-angleBas)
    else :
        left(90+angleBas)
        forward(cote)
        right(angleBas)
    right(90)
    down()
