#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 13:26:00 2022

@author: Jeanne_Claret

Programme : "The Game of life"
classes
"""

import multiprocessing as mp
 
import os, time,math, random, sys, ctypes, signal

# Définition de qq fonctions de gestion de l'écran
#def effacer_ecran() : print(CLEARSCR,end='')
def erase_line_from_beg_to_curs() : print("\033[1K",end='')
#def curseur_invisible() : print(CURSOFF,end='')
#def curseur_visible() : print(CURSON,end='')
def move_too(lig, col) : print("\033[" + str(lig) + ";" + str(col) + "f",end='')

def en_couleur(Coul) : print(Coul,end='')



class Cellules: 
 
    def __init__(self,dim):
        
        self.cell_alive_next = "\033[22;32m"  # vert
        self.cell_die_next = "\033[22;31m"      #rouge
        self.cell_dead = "\033[22;35m"          # magenta
        
        #random.randint(3,dim-1) * 2
        self.cell_position_init_ligne = random.randint(0,dim-1)
        self.cell_position_init_colonne = random.randint(0,dim-1)
        self.coordonnees_position_cellules = [self.cell_position_init_ligne,self.cell_position_init_colonne]
        
    def draw(self,l,c) :
        gr = Grille()
        print(self.coordonnees_position_cellules)
        en_couleur(self.cell_alive_next)
        #gr.grid[self.cell_position_init_ligne][self.cell_position_init_colonne] = "#"
        en_couleur("\033[01;37m")

    def status(self) :
        pass 
        

        
class Grille:
    
    def __init__(self,l=0,c=0):
        self.creerGrille(l,c)
        
            
        
    def creerGrille(self,lignes, colonnes): 
            
        self.grid = [[]] * lignes
        for ligne in range(colonnes):
            self.grid[ligne] = [0] * colonnes
        
        #return self.grid
        
    def draw_grille(self) :
        colonne =10
        for i in self.grid :
            #
            move_too(i,colonne) 
            erase_line_from_beg_to_curs()
            print(i)
            
    
    '''
    def position_cells(self,dim) : 
        cell = Cellules(dim)
        
        for i in self.grid :
            for k in range(dim) :
                
                '''
                
                
        
        
        


        
        
        
        
        
        
        