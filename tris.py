#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`tris` module
:author: FIL - Faculté des Sciences et Technologies - Univ. Lille <http://portail.fil.univ-lille1.fr>_
:date: 2015, january
:dernière révision: février 2018


Tris de listes

- tri par sélection
- tri par insertion

Analyse (empirique) en moyenne du nombre de comparaisons

"""

from compare import compare

    
def est_trie(l, comp=compare):
    """
    :param l: (type sequentiel) une séquence 
    :param comp: (fonction) [optionnel] une fonction de comparaison. 
                             Valeur par défaut : compare
    :return: (bool) 
      - True si l est triée selon l'ordre défini par comp
      - False sinon
    :CU: les éléments de l doivent être comparables selon comp
    :Exemples:

    >>> est_trie([1, 2, 3, 4])
    True
    >>> est_trie([1, 2, 4, 3])
    False
    >>> est_trie([])
    True
    """
    i = 0
    res = True
    while res and i < len(l) - 1:
        res = comp(l[i], l[i+1]) <= 0
        i += 1
    return res
    # ou plus simplement
    # return all(comp(l[i], l[i+1]) <= 0 for i in range(len(l) - 1))


################################################
#  TRI PAR SELECTION                           #
################################################

def echanger(l, i, j):
    """
    :param l: (list) une liste 
    :param i, j: (int) deux indices
    :return: (NoneType) aucune
    :Effet de bord: échange les éléments d'indice i et j de l.
    :CU: 0 <= i,j < long(l)
    :Exemples:
    
    >>> l1 =  [3, 1, 4, 9, 5, 1, 2]
    >>> l2 = l1.copy()
    >>> echanger(l2, 3, 5)
    >>> (l1[3], l1[5]) == (l2[5], l2[3])
    True
    """
    l[i], l[j] = l[j], l[i]
    

def select_min(l, a, b, comp=compare):
    """
    :param l: (list) une liste
    :param a, b: (int) deux indices
    :param comp: (fonction) [optionnel] une fonction de comparaison
                   Valeur par défaut compare
    :return: (int) l'indice du minimum dans la tranche l[a:b]
    :CU: 0 <= a < b <= long(l),
         éléments de l comparables avec comp
    :Exemples:
    
    >>> select_min([1, 2, 3, 4, 5, 6, 7, 0], 0, 8)
    7
    >>> select_min([1, 2, 3, 4, 5, 6, 7, 0], 1, 7)
    1
    """
    ind_min = a
    # l'indice du plus petit élément de la tranche l[a:a+1] est ind_min
    for i in range(a + 1, b):
        # supposons que l'indice du plus petit élément de la
        # tranche l[a:i] est ind_min
        if comp(l[i], l[ind_min]) == -1:
            ind_min = i
        # alors l'indice du plus petit élément de la tranche l[a:i+1]
        # est ind_min
    # à l'issue de l'itération l'indice du plus petit élément de la tranche
    # l[a:b] est ind_min
    return ind_min


def tri_select(l, comp=compare):
    """
    :param l: (list) une liste à trier
    :param comp: (fonction) [optionnel] une fonction de comparaison
                             Valeur par défaut : compare
    :return: (NoneType) aucune
    :Effet de bord: modifie la liste l en triant ses éléments selon l'ordre défini par comp
          Algorithme du tri par sélection du minimum
    :CU: l liste homogène d'éléments comparables selon comp
    :Exemples:

    >>> from random import shuffle
    >>> l1 = [k for k in range (10)]
    >>> shuffle(l1)
    >>> l2 = l1.copy()
    >>> tri_select(l2)
    >>> len(l1) == len(l2) and set(l1) == set(l2) and est_trie(l2)
    True
    """
    n = len(l)
    # la tranche l[0:1] est triée
    for i in range(n - 1):
        # supposons la tranche l[0:i+1] triée
        ind_min = select_min(l, i, n, comp=comp)
        echanger(l, i, ind_min)
        # alors la tranche l[0:i+1] est triée
    # à l'issue de l'itération la tranche l[0:n] est triée


################################################
#  TRI PAR INSERTION                           #
################################################

def inserer(l, i, comp=compare):
    """
    :param l: (list) une liste
    :param i: (int) indice de l'élément de l à insérer dans l[0:i+1]
    :param comp: (fonction) [optionnel] une fonction de comparaison
                             Valeur par défaut : compare
    :return: (NoneType) aucune
    :Effet de bord: insère l'élément l[i] à sa place dans la tranche l[0:i+1]
             de sorte que cette tranche soit triée si l[0:i] l'est auparavant
    :CU: 0 <= i < long(l)
         éléments de l comparables par comp
    :Exemples:

    >>> l = [1, 2, 4, 5, 3, 7, 6]
    >>> inserer(l, 4)
    >>> l == [1, 2, 3, 4, 5, 7, 6]
    True
    >>> inserer(l, 5)
    >>> l == [1, 2, 3, 4, 5, 7, 6]
    True
    >>> inserer(l, 6)
    >>> l == [1, 2, 3, 4, 5, 6, 7]
    True
    """
    aux = l[i]
    k = i
    while k >= 1 and comp(aux, l[k - 1]) == -1:
        l[k] = l[k - 1]
        k = k - 1    
    l[k] = aux

def tri_insert(l, comp=compare):
    """
    :param l: (list) une liste à trier
    :param comp: (fonction) [optionnel] une fonction de comparaison
    :return: (NoneType) aucune
    :Effet de bord : modifie la liste l en triant ses éléments selon l'ordre défini par comp
          Algorithme du tri par insertion
    :CU: l liste homogène d'éléments comparables selon comp
    :Exemples:

    >>> from random import shuffle
    >>> l1 = [k for k in range(10)]
    >>> shuffle(l1)
    >>> l2 = l1.copy()
    >>> tri_insert(l2)
    >>> len(l1) == len(l2) and set(l1) == set(l2) and est_trie(l2)
    True
    """
    n = len(l)
    # la tranche l[0:1] est triée
    for i in range(1, n):
        # supposons la tranche l[0:i] triée
        inserer (l, i, comp=comp)
        # alors la tranche l[0:i+1] est triée
    # à l'issue de l'itération la tranche l[0:n] est triée



if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

    
