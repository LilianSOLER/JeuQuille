#Fichier étant utilisé par "le jeu du château". Ecrite par Soler Lillian et Genoud-Duvillaret Benoît.

import random
from turtle import *
from math import *
from PolygonesEtMouvements import *
from ElementsChateaux import *
from PolygonesOmbres import *


#Quilles:

def Tour(grandissement,x,y,épaisseur):
    tracer(0,0)
    width(épaisseur)
    aller(x,y)
    trapeze(122*grandissement,88*grandissement,sqrt(200*200-17*17)*grandissement,"#434343","#6e6e6e")
    trapeze(111*grandissement,77*grandissement,sqrt(200*200-17*17)*grandissement,"#6e6e6e","#828282")
    trapeze(88*grandissement,54*grandissement,sqrt(200*200-17*17)*grandissement,"#828282","#8a8a8a")
    aller(x,y)
    briqueTour(122*grandissement,112*grandissement,sqrt(60*60-5*5)*grandissement,40*grandissement,60*grandissement,72*grandissement,"#595959","#767676")
    briqueTour(112*grandissement,103*grandissement,sqrt(55*55-4.5*4.5)*grandissement,15*grandissement,55*grandissement,78*grandissement,"#595959","#767676")
    briqueTour(112*grandissement,112*grandissement,1/100000000*grandissement,78*grandissement,55*grandissement,25*grandissement,"#595959","#767676")
    briqueTour(103*grandissement,95*grandissement,sqrt(45*45-4*4)*grandissement,60*grandissement,45*grandissement,35*grandissement,"#595959","#767676")
    briqueTour(95*grandissement,88*grandissement,sqrt(40*40-3.5*3.5)*grandissement,30*grandissement,40*grandissement,58*grandissement,"#595959","#767676")
    aller(x,y)
    trapeze(122*grandissement,88*grandissement,sqrt(200*200-17*17)*grandissement,"#434343","")
    hautTrapeze (111*grandissement,77*grandissement,sqrt(200*200-17*17)*grandissement)
    trapezeOmbreBase(88*grandissement,9/10,2/3,110*grandissement,25*grandissement)
    x1=xcor()
    y1=ycor()
    aller(x+59*grandissement,y+(sqrt(200*200-17*17)+25)*grandissement)
    drapeauxTourChateaux(90*grandissement,4*grandissement,6*grandissement, 100*grandissement,30*grandissement,x+59*grandissement,y+(sqrt(200*200-17*17)+25)*grandissement)
    left(90)
    aller(x1,y1)
    crénauxOmbre(3,3,2,35*grandissement,20*grandissement,15*grandissement,20*grandissement,10*grandissement,15*grandissement,10*grandissement,15*grandissement,20*grandissement,"#828282")
    right(90)
    aller(x,y)
    

def TourCassee(grandissement,x,y,épaisseur):
    tracer(0,0)
    width(épaisseur)
    aller(x+17*grandissement,y)
    dessineRectangle(88*grandissement,50*grandissement,"#434343","#3A3A3A")
    hautTrapeze(88*grandissement,88*grandissement,50*grandissement)
    trapezeOmbreBase(88*grandissement,9/10,2/3,110*grandissement,25*grandissement)
    x1=xcor()
    y1=ycor()
    aller(x+44*grandissement,y+(75*grandissement))
    drapeauxBlanc(90*grandissement,4*grandissement,50*grandissement,30*grandissement,x+44*grandissement,y+(75*grandissement))
    aller(x1,y1)
    left(90)
    crénauxOmbre(3,3,2,35*grandissement,20*grandissement,15*grandissement,20*grandissement,10*grandissement,15*grandissement,10*grandissement,15*grandissement,20*grandissement,"#828282")
    right(90)
    briqueTombée(30*grandissement,25*grandissement,0.63,x,y)
    left(35)
    briqueTombée(50*grandissement,25*grandissement,0.78,x+43*grandissement,y)
    right(35)
    briqueTombée(47*grandissement,22*grandissement,0.76,x+75*grandissement,y)
    left(20)
    briqueTombée(50*grandissement,25*grandissement,0.78,x+14*grandissement,y+25*grandissement)
    right(58)
    briqueTombée(50*grandissement,25*grandissement,0.78,x+63*grandissement,y+52*grandissement)
    aller(x,y)
    left(38)

def placementTour(ligneQuille,grandissement,x,y):
    aller(x,y)
    n=1
    ecart=((1140)/len(ligneQuille))-(122*grandissement)
    while n<=(len(ligneQuille)//2) :
            while n<=(len(ligneQuille)//2) and ligneQuille[n-1]=="|" :
                y=-440
                if  n%2==0 :
                    y=y+(n//2)*50
                else :
                    y=y+(n//2)*20
                Tour(grandissement,x,y,1.5)
                x=x+ecart+(122*grandissement)
                n=n+1
            while n<=(len(ligneQuille)//2) and ligneQuille[n-1]=="." :
                y=-440
                if  n%2==0 :
                    y=y+(n//2)*50
                else :
                    y=y+(n//2)*20
                TourCassee(grandissement,x,y,1.5)
                x=x+ecart+(122*grandissement)
                n=n+1
    if len(ligneQuille)%2==0:
        while n<=len(ligneQuille) :
            while n<=len(ligneQuille) and ligneQuille[n-1]=="|" :
                y=-440
                if  n%2==1 :
                    y=y+((len(ligneQuille)-n)//2+1)*50
                else :
                    y=y+((len(ligneQuille)-n)//2)*20
                Tour(grandissement,x,y,1.5)
                x=x+ecart+(122*grandissement)
                n=n+1

            while n<=len(ligneQuille) and ligneQuille[n-1]=="." :
                y=-440
                if  n%2==1 :
                    y=y+((len(ligneQuille)-n)//2+1)*50
                else :
                    y=y+((len(ligneQuille)-n)//2)*20
                TourCassee(grandissement,x,y,1.5)
                x=x+ecart+(122*grandissement)
                n=n+1

    else :
        while n<=len(ligneQuille) :
            while n<=len(ligneQuille) and ligneQuille[n-1]=="|" :
                y=-440
                if  n%2==0 :
                    y=y+((len(ligneQuille)-n)//2+1)*50
                else :
                    y=y+((len(ligneQuille)-n)//2)*20
                Tour(grandissement,x,y,1.5)
                x=x+ecart+(122*grandissement)
                n=n+1
            while n<=len(ligneQuille) and ligneQuille[n-1]=="." :
                y=-440
                if  n%2==0 :
                    y=y+((len(ligneQuille)-n)//2+1)*50
                else :
                    y=y+((len(ligneQuille)-n)//2)*20
                TourCassee(grandissement,x,y,1.5)
                x=x+ecart+(122*grandissement)
                n=n+1



