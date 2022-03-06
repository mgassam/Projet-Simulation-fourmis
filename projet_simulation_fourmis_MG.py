# -*- coding: utf-8 -*-
"""
Created on Mon Feb 28 00:27:45 2022

@author: Thank you God
"""

import random

# Les coordonnées minimal et maximal de la grille
mini = 1
maxi = 20
# nombre de points de vie
nbcouples = 15
# On definit les coord de depart des points de nourriture
def ma_fonction(mini, maxi, nbcouples):
    coordx = []
    coordy = []
    return coordx, coordy
coordx, coordy = ma_fonction(mini, maxi, nbcouples)

# On initialise les coordonnées initial
foodx = []
foody = []
# On importe le modue fct_fourmis
import fct_fourmis

# On place les points de nourriture en appelant la fonction setFood du module fct_fourmis
foodx, foody =fct_fourmis.setFood(mini, maxi, nbcouples)

# On importe le module ant_animate
import ant_animate

# On crée un dictionnaire des fourmis en definissant leurs positions et reserve énergétique
ants_dict =  {
    0: {
        'x': [13, 11, 17, 19, 15, 10, 17, 17, 10, 17],
        'y': [4, 4, 3, 3, 4, 5, 5, 5, 5, 6],
        'pv': [20, 18, 16, 14, 12, 10, 8, 7.0, 6.0, 4.0]},
    1: {
        'x': [10, 9, 9, 8, 9, 9, 9, 10, 10, 10],
        'y': [11, 11, 10, 10, 10, 9, 10, 10, 10, 10],
        'pv': [20, 18, 16, 14, 12, 10, 8, 7.0, 6.0, 5.0]},
    2: {
        'x': [13, 13, 14, 14, 14, 14, 14, 14, 15, 16],
        'y': [6, 5, 5, 6, 5, 6, 7, 7, 7, 7],
        'pv': [20, 18, 16, 14, 12, 10, 8, 7.0, 5.0, 3.0]},
    3: {
        'x': [5, 5, 5, 5, 6, 6, 6, 6, 7, 7],
        'y': [4, 3, 4, 5, 5, 4, 3, 4, 4, 5],
        'pv': [20, 18, 16, 14, 12, 20, 18, 20, 18, 16.0]},
    4: {
        'x' : [12, 3, 20, 12, 9, 20, 4, 15, 6, 10],
        'y' : [1, 5, 9, 4, 1, 8, 20, 16, 7, 2],
        'pv' : [20, 20, 12, 5, 12, 20, 15, 8, 12, 1]},
    5 : {
        'x' : [1, 3, 7, 17, 17, 16, 1, 9, 15, 12],
        'y' : [20, 20, 1, 7, 16, 15, 8, 2, 14, 4],
        'pv' : [15, 3, 7, 17, 20 ,13, 2, 10, 1, 9]}
    }
# On appelle l'application visual_app du module ant_animate pour afficher le graphique en definissant le parametrage de l'affichache et la valeur énergétique
ant_app = ant_animate.Visual_App(ants_dict, foodx, foody, pv= 20, delay= 750)

# On lance l'application ant_app.run du module ant_animate
ant_app.run()











