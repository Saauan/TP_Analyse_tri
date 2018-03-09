# Pour construire une liste des entiers de 0 à n-1: [i for i in range(n)]
from random import shuffle
import os
import analyse_tris
import timeit
import tris

TAILLE_MAX = 100


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
        
        
def analyse_tri_temps(tri, n, t):
    """
    Renvoie le temps que met l'ordinateur à trier `n` listes de taille `t` avec la fonction `tri`
    """
    for i in range(n):
        l = liste_alea(t)
        tri(l)

temps_select = []
print("test1")
with open("temps_tri_selec.csv", "w", encoding="utf-8") as canal_selec:
    print("test2")
    canal_selec.write('taille;"tri_selection"\n')
    for taille in range(1, TAILLE_MAX+1):
        temps = timeit.timeit(stmt='tris.tri_select(liste_alea(taille))',
                              setup="import tris; from tp_tri import liste_alea, taille; from random import shuffle",
                              number=50)
        temps_select.append(temps)
        canal_selec.write("{:3d} ; {:8f}\n".format(taille,temps))
    print("test3")

##print(temps_select)
print(sum(temps_select))
os.system('gnuplot --persist temps_tri_selec.gplot')




