#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`compare` module
:author: FIL - FST - Univ. Lille <http://portail.fil.univ-lille1.fr>_
:date: 2016, january
:dernière révision: février 2018

Fonction de comparaison 
pour l'analyse des algos de recherche et de tri

"""

def compare(x, y):
    """
    :param x, y: (quelconque) deux données de mêmes types
    :return: (int) 
      - -1 si x < y
      - 0 si x == y
      - 1 si x > y
    :CU: x et y doivent être d'un type pour lequel les opérateurs de comparaison <, <=, == 
         peuvent s'appliquer
    :Exemples:

    >>> compare(1, 3)
    -1
    >>> compare(3, 1)
    1
    >>> compare(3, 3)
    0
    """
    if x < y:
        return -1
    elif x > y:
        return 1
    else:
        return 0



if __name__ == '__main__':
    import doctest
    doctest.testmod()

    
