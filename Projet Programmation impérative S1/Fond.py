#Fichier étant utilisé par "le jeu du château". Ecrite par Soler Lillian et Genoud-Duvillaret Benoît.

import random
from turtle import *
from math import *
from PolygonesEtMouvements import *
from PolygonesOmbres import *
from GrandChateaux import *

#Le Fond :

def rayonSoleil(base,haut,hauteur,angle,x,y):
    aller(x,y)
    width (6)
    right(angle)
    trapeze(base,haut,hauteur,"#66e2ff","#8de9ff")
    left(angle)

def nuage(grandissement,x,y,couleurTrait,couleurPlein):
    aller(x,y)
    width(3)
    pencolor(couleurTrait)
    fillcolor(couleurPlein)
    begin_fill()
    speed(0)
    circle (30*grandissement,180)
    right(100)
    circle (70*grandissement,140)
    right(120)
    circle (50*grandissement,160)
    right(105)
    circle (60*grandissement,130)
    right(95)
    circle (30*grandissement,180)
    right(100)
    circle (50*grandissement,140)
    right(115)
    circle (80*grandissement,140)
    right(100)
    circle (34*grandissement,100)
    setheading(0)
    end_fill()

def nuageOmbre(grandissement,x,y):
    width(4)
    nuage(grandissement,x,y,"#d1d1d1","#e1e1e1")
    nuage(0.94*grandissement,x-17*grandissement,y+2*grandissement,"#e1e1e1","#efefef")

def sapin(grandissement,x,y):
    aller(x,y)
    troncOmbre(25*grandissement,2/3,1/3,25*grandissement,9/10)
    sapinOmbre(100*grandissement,2/3,1/3,100*grandissement,55*grandissement,55*grandissement,x-(37.5)*grandissement,y+25*grandissement)
    sapinOmbre(75*grandissement,2/3,1/3,75*grandissement,24*grandissement,24*grandissement,x-(25)*grandissement,y+75*grandissement)
    sapinOmbre(37.5*grandissement,2/3,1/3,37.5*grandissement,1/100000000000,1/100000000000,x-(6.25)*grandissement,y+130*grandissement)


def placeSapin(x,y,limx,avancementx,avancementy,épaisseur):
    width(épaisseur)
    while x<limx :
        sapin(0.7,x,y)
        x+=avancementx
        y+=avancementy

def sol(x,y):
    dessinePolygone(300,50,3,"#197814","#1e8c16",x,y-20)
    dessinePolygone(300,50,3,"#1d9215","#1d9215",x,y-40)
    dessinePolygone(300,50,3,"#1f9b17","#1f9b17",x,y-110)
    dessinePolygone(300,50,3,"#23a21a","#23a21a",x,y-210)
    placeSapin (-565,-100,-360,60,10,1)
    #placeSapin (-650,-120,-320,60,10,1)
    placeSapin (-670,-155,-280,60,10,1)
    #placeSapin (-650,-160,-330,60,10,1)
    placeSapin (-570,-190,-360,60,10,1)
    placeSapin (360,-80,570,60,-10,1)
    #placeSapin (320,-100,650,60,-10,1)
    placeSapin (280,-120,670,60,-10,1)
    #placeSapin (330,-140,650,60,-10,1)
    placeSapin (360,-170,550,60,-10,1)

def background():
    tracer(0,0)
    speed(0)
    width(1.5)
    bgcolor("#1dd3ff")
    rayonSoleil(30,100,1500,95,-600,540)
    rayonSoleil(30,100,1500,105,-600,520)
    rayonSoleil(30,100,1500,115,-640,500)
    rayonSoleil(30,100,1700,125,-670,480)
    rayonSoleil(30,100,1500,135,-700,470)
    rayonSoleil(30,100,1500,145,-720,460)
    rayonSoleil(30,100,1500,155,-740,450)
    nuageOmbre (1.2,540,300)
    nuageOmbre (1,650,180)
    nuageOmbre (0.7,280,250)
    nuageOmbre (1,-150,300)
    nuageOmbre (1.3,-300,230)
    nuageOmbre (0.8,-210,180)
    grosChateauStylé(1,0,-60)
    sol(0,0)


#Le cache des tours :

def cache():
    speed(0)
    sol(0,0)
    nuageOmbre (0.8,-210,180)
    

