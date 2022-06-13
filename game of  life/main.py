#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 13:26:05 2022

@author: Jeanne_Claret

Programme : "The Game of life"
"""
# Importations des couleurs :
    
CL_BLACK="\033[22;30m"                  #  Noir. NE PAS UTILISER. On verra rien !!
CL_RED="\033[22;31m"                    #  Rouge
CL_GREEN="\033[22;32m"                  #  Vert
CL_BROWN = "\033[22;33m"                #  Brun
CL_BLUE="\033[22;34m"                   #  Bleu
CL_MAGENTA="\033[22;35m"                #  Magenta
CL_CYAN="\033[22;36m"                   #  Cyan
CL_GRAY="\033[22;37m"                   #  Gris
CL_WHITE="\033[01;37m"                  #  Blanc

# Quelques codes d'échappement (tous ne sont pas utilisés)
CLEARSCR="\x1B[2J\x1B[;H"          #  Clear SCreen
CLEAREOS = "\x1B[J"                #  Clear End Of Screen
CLEARELN = "\x1B[2K"               #  Clear Entire LiNe
CLEARCUP = "\x1B[1J"               #  Clear Curseur UP
GOTOYX   = "\x1B[%.2d;%.2dH"       #  ('H' ou 'f') : Goto at (y,x), voir le code

DELAFCURSOR = "\x1B[K"             #  effacer après la position du curseur
CRLF  = "\r\n"                     #  Retour à la ligne

# VT100 : Actions sur le curseur
CURSON   = "\x1B[?25h"             #  Curseur visible
CURSOFF  = "\x1B[?25l"             #  Curseur invisible

# ===================== Main ================================
import multiprocessing as mp
 
import os, time,math, random, sys, ctypes, signal

# Définition de qq fonctions de gestion de l'écran
def effacer_ecran() : print(CLEARSCR,end='')
def erase_line_from_beg_to_curs() : print("\033[1K",end='')
def curseur_invisible() : print(CURSOFF,end='')
def curseur_visible() : print(CURSON,end='')
def move_to(lig, col) : print("\033[" + str(lig) + ";" + str(col) + "f",end='')

def en_couleur(Coul) : print(Coul,end='')
def en_rouge() : print(CL_RED,end='') # Un exemple !




#------------------------------------------------   
def prise_en_compte_signaux(signum, frame) :
    # On vient ici en cas de CTRL-C p. ex.
    move_to(dimension+5, 1)
    print(f"Il y a eu interruption No {signum} au clavier ..., on finit proprement")
    
    for i in range(Nb_process): 
        mes_process[i].terminate() 
    
    move_to(dimension+6, 1)
    curseur_visible()
    en_couleur(CL_WHITE)
    print("Fini")
    sys.exit(0)
# ---------------------------------------------------
from classes import Cellules, Grille

# La partie principale :
if __name__ == "__main__" :
    
    # Une liste de couleurs à affecter aléatoirement aux chevaux
    
    
    dimension = 15
    
    keep_running=mp.Value(ctypes.c_bool, True)

    Nb_process= dimension**2
    mes_process = [0 for i in range(Nb_process)]
    signal.signal(signal.SIGINT , prise_en_compte_signaux)
    signal.signal(signal.SIGQUIT , prise_en_compte_signaux)

    effacer_ecran()
    curseur_invisible()

#============= Formation de la grille ===============
    gr = Grille()
    gr.creerGrille(dimension,dimension)
    gr.draw_grille()
    #gr.position_cells(dimension)
    
 #============= Placements des cellules ===============   

    
    nb_cell_alive_first = 15
    for i in range(nb_cell_alive_first) :
        cells = Cellules(dimension)
        cells.draw(dimension, dimension)
        
    
    
    # for i in range(Nb_process):  # Lancer Nb_process  processus
    #     mes_process[i] = mp.Process(target=un_cheval, args= (i,keep_running,))
    #     mes_process[i].start()

    move_to(dimension+4, 15)
    print("tous lancés, Controle-C pour tout arrêter")


    # On attend la fin de la course
   # for i in range(Nb_process): mes_process[i].join()

    move_to(dimension+6, 1)
    curseur_visible()
    print("Fini")