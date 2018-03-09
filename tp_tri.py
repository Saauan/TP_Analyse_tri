# Pour construire une liste des entiers de 0 à n-1: [i for i in range(n)]
from random import shuffle
import os
import analyse_tris
import timeit
import tris

TAILLE_MAX = 100
NUMBER_ITERATIONS = 500

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

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    temps_select = []
    with open("temps_tri_selec.csv", "w", encoding="utf-8") as canal_selec:
        canal_selec.write('taille;"tri_selection"\n')
        
        for taille in range(0, TAILLE_MAX+1): # Je sais que normalement, ce sont les etniers t de 1 à TAILLE_MAX, mais pour uniformiser avec les autres mesures, j'ai pris la liberté de rajouter 0 comme valeur possible de t
            l = liste_alea(taille)
            temps = timeit.timeit(stmt='tris.tri_select(l)',
                                  setup="import tris; from __main__ import liste_alea, l, taille; from random import shuffle",
                                  number=NUMBER_ITERATIONS)
            temps_select.append(temps)
            canal_selec.write("{:3d} ; {:8f}\n".format(taille,temps))
            
    print("temps:", sum(temps_select)) # DEBUG
    os.system('gnuplot --persist temps_tri_selec.gplot')
    
    meil_cas = []
    cas_moy = []
    pire_cas = []
    for taille in range(0, TAILLE_MAX+1):
        l = liste_alea(taille)
        temps_meil_cas = timeit.timeit(stmt='tris.tri_insert(l)',
                                      setup="import tris; from __main__ import liste_alea, l,  taille; from random import shuffle",
                                      number=NUMBER_ITERATIONS)
        meil_cas.append(temps_meil_cas)
    print(sum(meil_cas))

    for taille in range(0, TAILLE_MAX+1):
        l= liste_alea(taille)
        temps_tri_melange = timeit.timeit(stmt='tris.tri_insert(l); shuffle(l)',
                                      setup="import tris; from __main__ import liste_alea, l, taille; from random import shuffle",
                                      number=NUMBER_ITERATIONS)
        temps_melange = timeit.timeit(stmt='shuffle(l)',
                                      setup="import tris; from __main__ import liste_alea, l, taille; from random import shuffle",
                                      number=NUMBER_ITERATIONS)
        cas_moy.append(temps_tri_melange - temps_melange)
    print(sum(cas_moy))
    
    for taille in range(0, TAILLE_MAX+1):
        l = sorted(liste_alea(taille), reverse=True)
        temps_tri_reverse = timeit.timeit(stmt='tris.tri_insert(l); l.sort(reverse=True)',
                                          setup="import tris; from __main__ import liste_alea, l, taille; from random import shuffle",
                                          number=NUMBER_ITERATIONS)      
        temps_reverse = timeit.timeit(stmt='l.sort(reverse=True)',
                                          setup="import tris; from __main__ import liste_alea, l, taille; from random import shuffle",
                                          number=NUMBER_ITERATIONS)  
        pire_cas.append(temps_tri_reverse - temps_reverse)
    print(sum(pire_cas))
    
    with open("temps_tri_insertion.csv","w",encoding="utf-8") as canal_insert:
        canal_insert.write('taille;"meilleur cas";"cas moyen";"pire cas"\n')
        for i in range(TAILLE_MAX+1):
            canal_insert.write("{:3d} ; {:8f} ; {:8f} ; {:8f}\n".format(i, meil_cas[i], cas_moy[i], pire_cas[i]))
    os.system('gnuplot --persist temps_tri_insertion.gplot')
        
        
    




