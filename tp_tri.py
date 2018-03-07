# Pour construire une liste des entiers de 0 à n-1: [i for i in range(n)]
from random import shuffle
import os
import analyse_tris



def liste_alea(n):
    """
    """
    liste_aleatoire = [i for i in range(n)]
    shuffle(liste_aleatoire)
    return liste_aleatoire

def affiche_n():
    """
    """
    liste_n = [i for i in range(101)]
    for i in liste_n:
        print("{:4d};{:5d}".format(i, (i*(i-1))//2))
        
affiche_n()



