#Fichier étant utilisé par "le jeu du château". Ecrite par Soler Lillian et Genoud-Duvillaret Benoît.

import random
from turtle import *
from math import *
from PolygonesEtMouvements import *
from PolygonesOmbres import *
from ElementsChateaux import *


    
#Def nécessaire à Chateau:


def baseTourChateau(tailleBase,hauteurRectangle,hauteurTrapeze,tailleHaut,multiplLong1,multiplLong2,x,y):
    aller(x,y)
    rectangleOmbreBase(tailleBase,multiplLong1,multiplLong2,hauteurRectangle)
    trapezeOmbreBase(tailleBase,multiplLong1,multiplLong2,tailleHaut,hauteurTrapeze)

def tourNormale(baseTourLrgrRect,baseTourHtRect,baseTourHtTrap,baseTourBsTrap,htGrdCrénaux,htCrénaux,x,y):
    baseTourChateau(baseTourLrgrRect,baseTourHtRect,baseTourHtTrap,baseTourBsTrap,9/10,2/3,x,y)
    left(90)
    crénauxOmbre(4,4,3,htGrdCrénaux,1/9*baseTourBsTrap,1/9*baseTourBsTrap-1/36*baseTourBsTrap,1/9*baseTourBsTrap,1/81*baseTourBsTrap,1/81*baseTourBsTrap,1/9*baseTourBsTrap,1/9*baseTourBsTrap+1/36*baseTourBsTrap,htCrénaux,"#828282")
    right(90)
    aller(x,y)

#le Château :

    
def grandeTourEntrée(grandissement,x,y):
    baseTourChateau(30*grandissement,180*grandissement,10*grandissement,49*grandissement,9/10,2/3,x-15*grandissement,y)
    a=pos()
    drapeauxTourChateaux(165*grandissement,3,4*grandissement, 100*grandissement, 20*grandissement,x,y+190*grandissement)
    goto(a)
    forward(4*grandissement)
    rectangleOmbreSousToit(41*grandissement,9/10,2/3,30*grandissement)
    forward(20.5*grandissement)
    porte (5*grandissement,17*grandissement,"#434343","black")
    backward(20.5*grandissement)
    hautTrapeze(41*grandissement,41*grandissement,30*grandissement)
    backward(5*grandissement)
    toitOmbre(51*grandissement,2/3,1/3,80*grandissement)
    aller(x-15*grandissement,y)
    hautTrapeze(30*grandissement,30*grandissement,180*grandissement)
    hautTrapeze(30*grandissement,49*grandissement,10*grandissement)
    left(90)
    crénauxOmbre(3,3,2,10*grandissement,7*grandissement,5*grandissement,7*grandissement,3*grandissement,7*grandissement,7*grandissement,9*grandissement,5*grandissement,"#828282")
    right(90)
    aller(x,y)
    
def grandeTourMilieu(grandissement,x,y):
    aller(x-35*grandissement,y)
    dessineRectangle(70*grandissement,440*grandissement,"#434343","#6e6e6e")
    dessineRectangle(35*grandissement,440*grandissement,"#6e6e6e","#8a8a8a")
    forward(20*grandissement)
    dessineRectangle(30*grandissement,440*grandissement,"#434343","#7a7a7a")
    backward(20*grandissement)
    dessineRectangle(70*grandissement,440*grandissement,"#434343","")
    hautTrapeze(30*grandissement,30*grandissement,440*grandissement)
    trapeze(70*grandissement,88*grandissement,10*grandissement,"#434343","#6e6e6e")
    trapeze(35*grandissement,53*grandissement,10*grandissement,"#828282","#8a8a8a")
    forward(20*grandissement)
    trapeze(30*grandissement,40*grandissement,10*grandissement,"#7a7a7a","#7a7a7a")
    backward(20*grandissement)
    trapeze(70*grandissement,88*grandissement,10*grandissement,"#434343","")
    hautTrapeze(70*grandissement,88*grandissement,10*grandissement)
    forward(22*grandissement)
    rectangleOmbreSousToit(40*grandissement,2/3,1/3,30*grandissement)
    forward(20*grandissement)
    porte(5*grandissement,20*grandissement,"#434343","black")
    backward(20*grandissement)
    hautTrapeze(40*grandissement,40*grandissement,30*grandissement)
    backward(5*grandissement)
    toitOmbre(50*grandissement,2/3,1/3,120*grandissement)
    aller(x-35*grandissement,y)
    hautTrapeze(30*grandissement,30*grandissement,440*grandissement)
    hautTrapeze(70*grandissement,88*grandissement,10*grandissement)
    left(90)
    crénauxOmbre(5,4,1,12*grandissement,8*grandissement,6*grandissement,8*grandissement,0*grandissement,8*grandissement,8*grandissement,10*grandissement,6*grandissement,"#7a7a7a")
    right(90)
    aller(x,y)

def tourPetiteMilieu(grandissement,x,y):
    baseTourChateau(44*grandissement,205*grandissement,10*grandissement,64*grandissement,9/10,2/3,x-22*grandissement,y)
    rectangleOmbreSousToit(64*grandissement,2/3,1/3,64*grandissement)
    hautTrapeze(64*grandissement,64*grandissement,64*grandissement)
    backward(7*grandissement)
    toitOmbre(78*grandissement,2/3,1/3,55*grandissement)
    aller(x,y)
         

def portesEntrée(grandissement,x,y) :
    aller(x-66*grandissement,y)
    maison (132*grandissement ,175*grandissement,24*grandissement,"#434343","#8a8a8a")
    maison (132*grandissement ,165*grandissement,24*grandissement,"#434343","#6e6e6e")
    aller(x,y)
    porte (35*grandissement,100*grandissement,"#434343","#8a8a8a")
    porte (22*grandissement,100*grandissement,"#434343","black")

def grandeTourGauche(grandissement,x,y) :
    baseTourChateau(70*grandissement,310*grandissement,10*grandissement,81*grandissement,9/10,2/3,x-30*grandissement,y)
    forward(10.5*grandissement)
    rectangleOmbreSousToit(60*grandissement,9/10,2/3,30*grandissement)
    forward(30*grandissement)
    porte(5*grandissement,15*grandissement,"#434343","#434343")
    backward(30*grandissement)
    hautTrapeze(60*grandissement,60*grandissement,30*grandissement)
    backward(10*grandissement)
    toitOmbre(80*grandissement,2/3,1/3,40*grandissement)
    aller(x-30*grandissement,y)
    hautTrapeze(70*grandissement,70*grandissement,310*grandissement)
    hautTrapeze(70*grandissement,81*grandissement,10*grandissement)
    left(90)
    crénauxOmbre(4,4,3,10*grandissement,9*grandissement,7*grandissement,9*grandissement,0*grandissement,0*grandissement,9*grandissement,11*grandissement,5*grandissement,"#828282")
    right(90)

def grandeTourDroite(grandissement,x,y):
    baseTourChateau(40*grandissement,350*grandissement,10*grandissement,50*grandissement,9/10,2/3,x-20*grandissement,y)
    a=pos()
    drapeauxTourChateaux(170*grandissement,3,4*grandissement, 100*grandissement, 20*grandissement,x,y+360*grandissement)
    goto(a)
    forward(7*grandissement)
    rectangleOmbreSousToit(36*grandissement,9/10,2/3,25*grandissement)
    hautTrapeze(36*grandissement,36*grandissement,25*grandissement)
    backward(7*grandissement)
    toitOmbre(50*grandissement,2/3,1/3,110*grandissement)
    aller(x-30*grandissement,y)

def grosseTourMoyenneGauche(grandissement,x,y):
    aller(x-38.5*grandissement,y)
    rectangleOmbreBase(77*grandissement,9/10,2/3,200*grandissement)
    backward(7*grandissement)
    left(90)
    crénauxOmbre(3,3,2,30*grandissement,13*grandissement,10*grandissement,13*grandissement,0*grandissement,5*grandissement,13*grandissement,16*grandissement,6*grandissement,"#828282")
    right(90)
    n=1
    while n<=5:
        aller(x-45.5*grandissement+14*grandissement*n,y+170*grandissement)
        dessineRectangle(7*grandissement,14*grandissement,"#434343","black")
        n=n+1
    aller(x,y)
    
def petiteTourDroite(grandissement,x,y):
    tourNormale(50*grandissement,140*grandissement,10*grandissement,72*grandissement,20*grandissement,5*grandissement,x-20*grandissement,y)

def petiteTourGauche(grandissement,x,y):
    tourNormale(70*grandissement,110*grandissement,15*grandissement,81*grandissement,20*grandissement,9*grandissement,x-20*grandissement,y)

def fineTourDroite(tailleBase,hauteurRectangle1,hauteurTrapeze,largeurRectangle2,hauteurRectangle2,hauteurToit,grandissement,x,y):
    baseTourChateau(tailleBase*grandissement,hauteurRectangle1*grandissement,hauteurTrapeze*grandissement,largeurRectangle2*grandissement,9/10,2/3,x,y)
    a=pos()
    drapeauxTourChateaux(100*grandissement,3,4*grandissement, 100*grandissement, 15*grandissement,x+(tailleBase/2)*grandissement,y+(hauteurRectangle1+hauteurTrapeze)*grandissement)
    goto(a)
    rectangleOmbreSousToit(largeurRectangle2*grandissement,9/10,2/3,hauteurRectangle2*grandissement)
    hautTrapeze(largeurRectangle2*grandissement,largeurRectangle2*grandissement,hauteurRectangle2*grandissement)
    backward(1/10*largeurRectangle2)
    toitOmbre(6/5*largeurRectangle2*grandissement,2/3,1/3,hauteurToit*grandissement)
    aller(x,y)


    
#La définition du chateau:
    

def grosChateauStylé(grandissement,x,y):
    width(1.5)
    grandeTourMilieu(grandissement,x,y)
    tourPetiteMilieu(grandissement,x,y)
    bannièreChateau(38*grandissement,3*grandissement,4*grandissement,70*grandissement,x,y+270*grandissement)
    grandeTourGauche(grandissement,x-96*grandissement,y)
    grosseTourMoyenneGauche(grandissement,x-134.5*grandissement,y)
    petiteTourGauche(grandissement,x-220*grandissement,y)
    grandeTourDroite(grandissement,x+75*grandissement,y)
    aller(x+95*grandissement,y+295*grandissement)
    dessineParallélépipède(160*grandissement,45*grandissement,-60,"#434343","#6e6e6e")
    fineTourDroite(16,220,8,25,15,60,grandissement,x+175*grandissement,y)
    aller(x+191*grandissement,y+148*grandissement)
    dessineParallélépipède(57*grandissement,32*grandissement,-30,"#434343","#6e6e6e")
    fineTourDroite(16,180,8,25,15,60,grandissement,x+240*grandissement,y)
    aller(x+256*grandissement,y+116*grandissement)
    dessineParallélépipède(38*grandissement,28*grandissement,-10,"#434343","#6e6e6e")
    fineTourDroite(16,160,8,25,15,60,grandissement,x+290*grandissement,y)
    petiteTourDroite(grandissement,x+116*grandissement,y)
    portesEntrée(grandissement,x,y)
    bannièreChateau(21*grandissement,1*grandissement,2*grandissement,80*grandissement,x-50.5*grandissement,y+140*grandissement)
    bannièreChateau(21*grandissement,1*grandissement,2*grandissement,80*grandissement,x+50.5*grandissement,y+140*grandissement)
    grandeTourEntrée(grandissement,x-81*grandissement,y)
    grandeTourEntrée(grandissement,x+81*grandissement,y)
