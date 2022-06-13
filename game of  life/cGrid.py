import os, sys, random
import multiprocessing as mp
import screenProf as sp

sp.effacer_ecran()

class cellule():
    def __init__(self, dim):
        self.__cellVi = 'Ⓥ'
        self.__cellMort = 'Ⓧ'
        nb_cell_viv_dep = random.randint(3,dim)*2
        self.__cellPosLigne = random.randint(0, dim-1)
        self.__cellPosCol = random.randint(0, dim-1)

    def affichage(self, l, c):
        grille = grid(l,c)
        print(self.__cellVi)
        #grille.__grille[self.__cellPosLigne][self.__cellPosCol] = 0

class grid():
    def __init__(self, l = 0, c = 0):
        #self.__creationgrille(l,c)
        self.__grille = []
        pass
    
    def creerGrille(self, lignes, colonnes):
        self.__grille = [[]]*lignes
        for lignes in range(colonnes):
            self.__grille[lignes] = [0]*colonnes
            
    def affichage(self):
        colonnes = 10
        for i in self.__grille:
            sp.move_to(i, colonnes)
            sp.erase_line_from_beg_to_curs()
            print(i)
            colonnes += 1
    