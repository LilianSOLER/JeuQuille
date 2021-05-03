#Fichier étant utilisé par "le jeu du château". Ecrite par Soler Lillian et Genoud-Duvillaret Benoît.

import random
from turtle import *
from math import *
from MoteurDeJeu import *
from PolygonesEtMouvements import *
from Tours import *
#from ElementsChateaux import *
#from GrandChateaux import *
from PolygonesOmbres import *
from Fond import *


# /!\ Les commentaires sont un peu écartés des actions. Vous pouvez agrandir la page pour les consulter.


##############################################################################################################################################
background()
ht()
aller(350,400)
pencolor("#cacaca")
write("▲___________▲___________▲",False,align="center",font=("Enchanted Land", 25,"normal"))

aller(350,370)
pencolor("#cacaca")
write("| | Bienvenue sur le jeu du Chateau | |",False,align="center",font=("Enchanted Land", 25,"normal"))

aller(350,350)
write("====================================",False,align="center",font=("Enchanted Land", 25,"normal"))

aller(480,290)
write("But :",False,align="center",font=("Enchanted Land", 25,"normal"))

aller(500,250)
write("Vainquez votre adversaire du",False,align="center",font=("Enchanted Land", 20,"normal"))

aller(500,220)
write("royaume voisin en détruisant la",False,align="center",font=("Enchanted Land", 20,"normal"))

aller(500,190)
write("dernière tour afin de remporter :",False,align="center",font=("Enchanted Land", 20,"normal"))

aller(480,150)
write("LE  CHATEAU",False,align="center",font=("Enchanted Land", 25,"normal"))


x=-570
y=-440
n=random.randint(15,20)
q=[[0,n-1]]
placementTour(afficheQuilles(q,n),0.5,x,y)
aller(-335,220)
pencolor("#cacaca")
write("A vous de jouer guerrier",False,align="center",font=("Enchanted Land", 25,"normal"))
aller(-350,185)
write('il y a',False,align="right",font=("Enchanted Land", 20,"normal"))
aller(-340,185)
write(len(q),False,align="center",font=("Enchanted Land", 20,"normal"))
aller(-330,185)
write("groupes(s)",False,align="left",font=("Enchanted Land", 20,"normal"))

while q!=[] :
    j=joueurJoue(q)
    q=jouer(j,q)
    cache()
    placementTour(afficheQuilles(q,n),0.5,x,y)
    aller(-335,220)
    pencolor("#cacaca")
    write("Votre ennemi joue",False,align="center",font=("Enchanted Land", 25,"normal"))
    aller(-350,185)
    write('il y a',False,align="right",font=("Enchanted Land", 20,"normal"))
    aller(-340,185)
    write(len(q),False,align="center",font=("Enchanted Land", 20,"normal"))
    aller(-330,185)
    write("groupes(s)",False,align="left",font=("Enchanted Land", 20,"normal"))
    aller(x,y)
    if q==[] :
        aller(0,-150)
        pencolor("#c0c603")
        write("Victoire ! ",False,align="center",font=("Enchanted Land", 100,"normal"))
    else :                                                                                
        i=ordiJoue(q)
        q=jouer(i,q)
        cache()
        placementTour(afficheQuilles(q,n),0.5,x,y)
        aller(-335,220)
        pencolor("#cacaca")
        write("A vous de jouer guerrier",False,align="center",font=("Enchanted Land", 25,"normal"))
        aller(-350,185)
        write('il y a',False,align="right",font=("Enchanted Land", 20,"normal"))
        aller(-340,185)
        write(len(q),False,align="center",font=("Enchanted Land", 20,"normal"))
        aller(-330,185)
        write("groupes(s)",False,align="left",font=("Enchanted Land", 20,"normal"))
        aller(x,y)
        if q==[] :
            aller(0,-150)
            pencolor("#b50005")
            write ("Vous avez perdu...",False,align="center",font=("Enchanted Land",100,"normal"))




