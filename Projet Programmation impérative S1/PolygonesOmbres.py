#Fichier étant utilisé par "le jeu du château". Ecrite par Soler Lillian et Genoud-Duvillaret Benoît.

import random
from turtle import *
from math import *
from ElementsChateaux import *
from PolygonesEtMouvements import *

#Les ombrages :

def rectangleOmbreSousToit(longueurCote,muliplLong1,muliplLong2,largeurCote):
    dessineRectangle(longueurCote,largeurCote,"#434343","#5a5a5a")
    dessineRectangle(longueurCote,largeurCote-5,"#6e6e6e","#6e6e6e")
    dessineRectangle(longueurCote*muliplLong1,largeurCote-5,"#828282","#828282")
    dessineRectangle(longueurCote*muliplLong2,largeurCote-5,"#8a8a8a","#8a8a8a")
    dessineRectangle(longueurCote,largeurCote,"#434343","")
    
def rectangleOmbreBase(tailleBase,muliplLong1,muliplLong2,hauteurRectangle):
    dessineRectangle(tailleBase,hauteurRectangle,"#434343","#6e6e6e")
    dessineRectangle(tailleBase*muliplLong1,hauteurRectangle,"#6e6e6e","#828282")
    dessineRectangle(tailleBase*muliplLong2,hauteurRectangle,"#828282","#8a8a8a")
    dessineRectangle(tailleBase,hauteurRectangle,"#434343","")
    hautTrapeze(tailleBase,tailleBase,hauteurRectangle)

def trapezeOmbreBase(tailleBase,muliplLong1,muliplLong2,tailleHaut,hauteurTrapeze):
    trapeze(tailleBase,tailleHaut,hauteurTrapeze,"#434343","#6e6e6e")
    trapeze(tailleBase*muliplLong1,(tailleHaut*9)/10,hauteurTrapeze,"#6e6e6e","#828282")
    trapeze(tailleBase*muliplLong2,(tailleHaut*2)/3,hauteurTrapeze,"#828282","#8a8a8a")
    trapeze(tailleBase,tailleHaut,hauteurTrapeze,"#434343","")
    hautTrapeze(tailleBase,tailleHaut,hauteurTrapeze)

def toitOmbre(tailleBase,multipTaille1,multipTaille2,hauteur):
    a=(tailleBase-tailleBase*multipTaille1)/2
    b=(tailleBase*multipTaille1-tailleBase*multipTaille2)/2
    
    toit(tailleBase,hauteur,"#5f1300","#751800","#be1b00","#821b00")
    forward(a)
    toit(tailleBase*multipTaille1,hauteur,"#af1b00","#911b00","#af1b00","#911b00")
    forward(b)
    toit(tailleBase*multipTaille2,hauteur,"#a01b00","#a01b00","#a01b00","#a01b00")
    backward(a+b)
    toit(tailleBase,hauteur,"#5f1300","#5f1300","","")

def crénauxOmbre(nbreCrnx1,nbreCrnx2,nbreCrnx3,ht,longHautDébut1,longHautDébut2,longHautFin1,longHautFin2,longHautFin3,longBas1,longBas2,htCrénaux,couleurMilieu):
    créneaux (nbreCrnx1,ht,longHautDébut1,longHautFin1,longBas1,htCrénaux,"#434343","#6e6e6e")
    créneaux (nbreCrnx2,ht,longHautDébut2,longHautFin2,longBas2,htCrénaux,"#6e6e6e",couleurMilieu)
    créneaux (nbreCrnx3,ht,longHautDébut2,longHautFin3,longBas2,htCrénaux,couleurMilieu,"#8a8a8a")
    créneaux (nbreCrnx1,ht,longHautDébut1,longHautFin1,longBas1,htCrénaux,"#434343","")

def sapinOmbre(tailleBase,multipTaille1,multipTaille2,hauteur,tailleT2,hauteurT2,x,y):
    a=(tailleBase-tailleBase*multipTaille1)/2
    b=(tailleBase*multipTaille1-tailleBase*multipTaille2)/2
    width(1.5)
    aller(x,y)
    toit(tailleBase,hauteur,"black","black","#14c800","#147800")
    forward(a)
    toit(tailleBase*multipTaille1,hauteur,"#14b400","#148c00","#14b400","#148c00")
    forward(b)
    toit(tailleBase*multipTaille2,hauteur,"#14a000","#14a000","#14a000","#14a000")
    backward(a+b)
    hautTrapeze(tailleBase,tailleT2,hauteur-hauteurT2)
    toit (tailleT2, hauteurT2,"#146900","#146900","#146900","#146900")
    aller(x,y)
    toit(tailleBase,hauteur,"#136200","#136200","","")

def troncOmbre(tailleBase,multipTaille1,multipTaille2,hauteurRectangle,multipHaut):
    dessineRectangle(tailleBase,hauteurRectangle,"#42270d","#4b2d0e")
    dessineRectangle(tailleBase,hauteurRectangle*multipHaut,"#3f2204","#503213")
    dessineRectangle(tailleBase*multipTaille1,hauteurRectangle*multipHaut,"#503213","#5f3c18")
    dessineRectangle(tailleBase*multipTaille2,hauteurRectangle*multipHaut,"#5f3c18","#744c23")
    dessineRectangle(tailleBase,hauteurRectangle,"#42270d","")   
