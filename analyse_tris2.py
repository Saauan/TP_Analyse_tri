#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`analyse_tris` module
:author: FIL - Faculté des Sciences et Technologies - Univ. Lille <http://portail.fil.univ-lille1.fr>_
:date: janvier 2017
:dernière révision: février 2018

Analyse empirique des tris

"""
from random import shuffle
from compare import compare
from tris import *
import os
from functools import cmp_to_key

################################################
#  ANALYSE EMPIRIQUE DES TRIS                  #
################################################

def gen_compteur_compare(comp):
    """
    :param comp: (fonction) une fonction de comparaison. 
    :return: (fonction) une fonction de comparaison identique à ``comp``,
          mais dotée d'un paramètre optionnel permettant d'obtenir le
          nombre d'appels qui a été fait à cette fonction.
    :CU: aucune
    :Exemples:

    >>> comp1 = gen_compteur_compare(compare)
    >>> comp1(1, 2)
    -1
    >>> comp1(1, 1)
    0
    >>> comp1(1, 0)
    1
    >>> comp1(nb=True)
    3
    >>> comp2 = gen_compteur_compare (compare)
    >>> comp2(1, 2)
    -1
    >>> comp2(nb=True)
    1
    >>> comp1(nb=True)
    3
    >>> comp1(reset=True)
    >>> comp1(nb=True)
    0
    """
    cpt = {'nb' : 0}
    def f(x=0, y=0, nb=False, reset=False):
        if nb:
            return cpt['nb']
        elif reset:
            cpt['nb'] = 0
        else:
            cpt['nb'] += 1
            return comp(x,y)
    return f

def analyser_tri(tri, n, t):
    """
    :param tri: (fonction) fonction de tri
    :param n: (int) nombre de listes aléatoires à trier
    :param t: (int) taille des listes à trier
    :return: (int) le nombre moyen de comparaisons effectués par l'algo tri
         pour trier des listes de taille t, la moyenne étant calculée
         sur n listes aléatoires.
    :CU: n > 0, t >= 0
    """
    res = 0
    comp = gen_compteur_compare(compare)
    for i in range(n):
        comp(reset=True)
        l = [k for k in range(t)]
        shuffle(l)
        tri(l, comp=comp)
        res += comp(nb=True)
    return res / n

def fausse(l, comp):
    return sorted(l, key=cmp_to_key(comp))  

if __name__ == '__main__':
    import doctest, os
    doctest.testmod()
    
    
    # Calcul de nombres moyens de comparaison pour des listes
    # de tailles comprises entre 0 et TAILLE_MAX
    NB_ESSAIS = 50
    TAILLE_MAX = 100
    c_select = [0] * (TAILLE_MAX + 1)
    c_insert = [0] * (TAILLE_MAX + 1)
    c_sorted = [0] * (TAILLE_MAX + 1)
    
    for t in range(TAILLE_MAX + 1):
        c_select[t] = analyser_tri(tri_select, 1, t)
        # inutile de moyenner pour le tri par sélection
        c_insert[t] = analyser_tri(tri_insert, NB_ESSAIS, t)
        c_sorted[t] = analyser_tri(fausse, NB_ESSAIS, t)

    # Sauvegarde des données calculées dans un fichier au format CSV
    with open('analyse_tris.csv', 'w', encoding='utf8') as sortie:
        sortie.write('taille;"tri séléction";"tri insertion";"tri sort"\n')
        for t in range(TAILLE_MAX + 1):
            sortie.write('{:3d};{:8.2f};{:8.2f};{:8.2f}\n'.format(t,
                                                          c_select[t],
                                                          c_insert[t],
                                                          c_sorted[t]))
    os.system('gnuplot --persist analyse_tris.gplot')
