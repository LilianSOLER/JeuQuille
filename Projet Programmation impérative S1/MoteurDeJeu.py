#Fichier étant utilisé par "le jeu du château". Ecrite par Soler Lillian et Genoud-Duvillaret Benoît.

from turtle import *
from math import *
import random
#Moteur de jeu:

def afficheQuilles(q,n):  
    ligneQuille=""
    l=0
    if q!=[]:                                                       
        if q[0][0]!=0:                                             
            ligneQuille="."*(q[0][0])                   
        while l+1<len(q):
            ligneQuille=ligneQuille+"|"*(q[l][1]-q[l][0]+1)         
            ligneQuille=ligneQuille+"."*(q[l+1][0]-q[l][1]-1)       
            l=l+1
        ligneQuille=ligneQuille+"|"*(q[l][1]-q[l][0]+1)             
        ligneQuille=ligneQuille+"."*(n-q[l][1]-1)                   
    else :                                                          
        ligneQuille=ligneQuille+n*"."

    return ligneQuille



def joueurJoue(q):                                                        
    l="erreur"
    while l=="erreur" :                                                   
        i=int(numinput("Le Jeu du Château","Quelle ligne choisissez vous ? "))                                      
        p=str(textinput("Le Jeu du Château","Vous choisissez gauche, droite ou milieu ? (G,D,M) "))                  
        if 1<=i<=len(q) and (p=="M" or p=="G" or p=="D"):                                    
            l=str(i)+":"+p
        else :
            l="erreur"                                                                       
            print("Les valeurs que vous avez entré sont incorectes. Veuillez réessayer.")
    return l


def ordiJoue (q):                                                        
    p = random.choice(["G","M","D"])        
    i=str(random.randint(1,len(q)))         
    l=i+":"+p
    return l



def jouerMilieu (c,q):                                      
    p=int(c[0])-1                                           
    premiere=q[p][0]
    derniere=q[p][1]
    moyenne=int((q[p][1]+premiere)//2)

    if derniere-premiere==0 or derniere-premiere==1 :       
        q.remove(q[p])
    elif derniere-premiere==2:                              
        q[p]=[premiere,premiere]
    else :                                                  
        q[p]=[premiere,moyenne-1]
        q.insert(p+1,[moyenne+2,derniere])
    return(q)


def jouerCotés (c,q):                     
    p=int(c[0])-1                         
    premiere=q[p][0]
    derniere=q[p][1]

    if premiere==derniere :               
        q.remove (q[p])
    elif c[2]=="G":                       
        q[p]=[premiere+1,derniere]
        
    elif c[2]=="D":                       
        q[p]=[premiere,derniere-1]
    return q



def jouer(c,q):
    p=int(c[0])-1                        
    premiere=q[p][0]
    derniere=q[p][1]
    
    if c[2]=="G" or c[2]=="D" :          
        q=jouerCotés(c,q)
    else :                               
        q=jouerMilieu(c,q)
    return q
