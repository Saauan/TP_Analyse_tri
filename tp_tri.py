# Pour construire une liste des entiers de 0 à n-1: [i for i in range(n)]
from random import shuffle
import os
import timeit
import tris

TAILLE_MAX = 100 # Taille maximale des listes lors du timing des tris
NUMBER_ITERATIONS = 500 # Nombre d'itérations des timeit.timeit

def liste_alea(n):
    """
    Renvoie une liste aléatoirement mélangée qui contient tous les entiers de 0 à `n`-1
    
    :param n: (int) the length of the list
    :return: (list) a list containing all integer from 0 to n-1 without any particular order
    :UC: n is positive
    
    Exemples:
    
    >>> l = liste_alea(100)
    >>> len(l) == 100
    True
    >>> set(l) == {i for i in range(100)}
    True
    """
    liste_aleatoire = [i for i in range(n)]
    shuffle(liste_aleatoire)
    return liste_aleatoire

def affiche_n():
    """
    Affiche l'entier `n' pour les valeurs de 0 à 100 sur 4 caractères suivis d'un point virgule suivi de n(n-1)/2 sur 5 caractères
    """
    liste_n = [i for i in range(101)]
    for i in liste_n:
        print("{:4d};{:5d}".format(i, (i*(i-1))//2))
        
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    # TRI PAR SELECTION
    temps_select = []
    print("Timing tri par selection...") # DEBUG
    for taille in range(0, TAILLE_MAX+1): # Je sais que normalement, ce sont les etniers t de 1 à TAILLE_MAX, mais pour uniformiser avec les autres mesures, j'ai pris la liberté de rajouter 0 comme valeur possible de t
        l = liste_alea(taille)
        # Calcul du temps pour trier une liste par sélection `NUMBER_ITERATIONS`fois
        temps = timeit.timeit(stmt='tris.tri_select(l)',
                              setup="import tris; from __main__ import liste_alea, l, taille; from random import shuffle",
                              number=NUMBER_ITERATIONS)
        temps_select.append(temps)
        
    # Writing the times recorded in temps_tri_selec.csv
    with open("temps_tri_selec.csv", "w", encoding="utf-8") as canal_selec:
        canal_selec.write('taille;"tri_selection"\n')
        for taille, temps in enumerate(temps_select):
            canal_selec.write("{:3d} ; {:8f}\n".format(taille,temps))
    print("time tri par selection:", sum(temps_select)) # DEBUG
    os.system('gnuplot --persist temps_tri_selec.gplot') # Displays the graph of the times recorded over the lengths of the lists
    
    # TRI PAR INSERTION
    meil_cas = []
    cas_moy = []
    pire_cas = []
    print("Timing tri par insertion meilleur cas...") # DEBUG
    for taille in range(0, TAILLE_MAX+1):
        l = liste_alea(taille)
        temps_meil_cas = timeit.timeit(stmt='tris.tri_insert(l)',
                                      setup="import tris; from __main__ import liste_alea, l,  taille; from random import shuffle",
                                      number=NUMBER_ITERATIONS)
        meil_cas.append(temps_meil_cas)
    print(sum(meil_cas)) # DEBUG

    print("Timing tri par insertion cas moyen..") # DEBUG
    for taille in range(0, TAILLE_MAX+1):
        l= liste_alea(taille)
        temps_tri_melange = timeit.timeit(stmt='tris.tri_insert(l); shuffle(l)',
                                      setup="import tris; from __main__ import liste_alea, l, taille; from random import shuffle",
                                      number=NUMBER_ITERATIONS)
        temps_melange = timeit.timeit(stmt='shuffle(l)',
                                      setup="import tris; from __main__ import liste_alea, l, taille; from random import shuffle",
                                      number=NUMBER_ITERATIONS)
        cas_moy.append(temps_tri_melange - temps_melange)
    print(sum(cas_moy)) # DEBUG
    
    print("Timing tri par insertion pire cas...") # DEBUG
    for taille in range(0, TAILLE_MAX+1):
        l = sorted(liste_alea(taille), reverse=True)
        temps_tri_reverse = timeit.timeit(stmt='tris.tri_insert(l); l.sort(reverse=True)',
                                          setup="import tris; from __main__ import liste_alea, l, taille; from random import shuffle",
                                          number=NUMBER_ITERATIONS)      
        temps_reverse = timeit.timeit(stmt='l.sort(reverse=True)',
                                          setup="import tris; from __main__ import liste_alea, l, taille; from random import shuffle",
                                          number=NUMBER_ITERATIONS)  
        pire_cas.append(temps_tri_reverse - temps_reverse)
    print(sum(pire_cas)) # DEBUG
    
    # Writing the times recorded in temps_tri_selec.csv
    with open("temps_tri_insertion.csv","w",encoding="utf-8") as canal_insert:
        canal_insert.write('taille;"meilleur cas";"cas moyen";"pire cas"\n')
        for i in range(0, TAILLE_MAX+1):
            canal_insert.write("{:3d} ; {:8f} ; {:8f} ; {:8f}\n".format(i, meil_cas[i], cas_moy[i], pire_cas[i]))
    os.system('gnuplot --persist temps_tri_insertion.gplot') # Displays the graph of the times recorded over the lengths of the lists
        
        
    




