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
        nb_cell_alive_first = 15
        self.coordonnees_position_cellules = []
        
        #random.randint(3,dim-1) * 2
        for i in range(nb_cell_alive_first+1) :
            
            self.cell_position_init_ligne = random.randint(0,dim-1)
            self.cell_position_init_colonne = random.randint(0,dim-1)
            coord = [self.cell_position_init_ligne,self.cell_position_init_colonne]
            self.coordonnees_position_cellules.append(coord)
        
    def draw(self,l,c) :
        #gr = Grille()
        
        print(self.coordonnees_position_cellules)
        motif_cell = "#"
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
            
    
    
    def position_cells(self,dim) : 
        cell = Cellules(dim)
        
        for k in cell.coordonnees_position_cellules :
                
           x = k[0]
           y =  k[1]
                
           self.grid[x][y] = 1
           
    def next_state(self,dim) :
        
        for l in range(dim) :
            for c in range(dim) :
                
                if self.grid[l][c] == 1 :
                                         
                    if (l,c) > (1,1) and (l,c) < [dim-1,dim-1] : 
                        # somme pour le carré central 
                        somme = self.grid[l-1][c-1] + self.grid[l-1][c] + self.grid[l-1][c+1] + self.grid[l][c-1] +self.grid[l][c+1]
                    + self.grid[l+1][c-1] + self.grid[l+1][c] + self.grid[l+1][c+1]
                    
                    if l == 1 and 1 < c < dim-1 :
                        # première ligne sans les coins 
                        somme = self.grid[l][c-1] +self.grid[l][c+1]+ self.grid[l+1][c-1] + self.grid[l+1][c] + self.grid[l+1][c+1]
                    
                    if (l,c) == (0,0) :
                        somme = self.grid[l][c+1] + self.grid[l+1][c] + self.grid[l+1][c+1] # coin haut gauche
                        
                    if (l,c) == (dim-1,dim-1) :
                        somme = self.grid[l][c-1] + self.grid[l+1][c-1] + self.grid[l+1][c]  # coin haut droite
                        
                    if l == dim-1 and 1 < c < dim-1 :
                        # dernière ligne sans les coins
                        somme = self.grid[l-1][c-1] + self.grid[l-1][c] + self.grid[l-1][c+1] + self.grid[l][c-1] +self.grid[l][c+1]
                   
                    if (l,c) == (dim-1,dim-1) :
                        somme = self.grid[l-1][c-1] + self.grid[l-1][c]  + self.grid[l][c-1]  # coin bas droit
                    
                    if (l,c) == (dim-1,0) :
                        somme = self.grid[l-1][c] + self.grid[l-1][c+1] +self.grid[l][c+1] # coin bas gauche
                        
                    if c == 0 and 1< l < dim-1  :
                        somme = self.grid[l-1][c] + self.grid[l-1][c+1]  +self.grid[l][c+1] + self.grid[l+1][c] + self.grid[l+1][c+1]
                    
                    if c == dim-1 and 1< l < dim-1 :
                        somme = self.grid[l-1][c-1] + self.grid[l-1][c]  + self.grid[l][c-1] + self.grid[l+1][c-1] + self.grid[l+1][c] 
        
                    if somme > 3 :
                        self.grid[l][c] == 0 
                    
                    if somme < 2 : 
                        self.grid[l][c] == 0 
                        
                if self.grid[l][c] == 0 :
                    somme = self.grid[l-1][c-1] + self.grid[l-1][c] + self.grid[l-1][c+1] + self.grid[l][c-1] +self.grid[l][c+1]
                    + self.grid[l+1][c-1] + self.grid[l+1][c] + self.grid[l+1][c+1]
                    
                    
                    if somme == 3 :
                        self.grid[l][c] == 1
                    
                else :
                    
                    self.grid[l][c] = 0
        
        


        
        
        
        
        
        
        