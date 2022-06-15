import multiprocessing as mp
import random, time
import numpy as np
import Course_Hippique_basique as ch




class Jeu():
    def __init__(self, Hauteur, Largeur):
        self.__hauteurGrille = Hauteur
        self.__largeurGrille = Largeur
        self.__grilleUsr = []
        self.__grille = []
        self.__ferme = mp.Lock()
    
    
    def Grille(self):
        for ligne in range(self.__hauteurGrille):
            lstLignePhoto = []
            lstLigne = []
            for colonnes in range(self.__largeurGrille):
                proba = random.randint(0,4)
                if proba > 1:
                    lstLignePhoto.append(Cellule(False))
                    lstLigne.append("x")
                else:
                    lstLignePhoto.append(Cellule(True))
                    lstLigne.append("0")
            self.__grille.append(lstLignePhoto)
            self.__grilleUsr.append(lstLigne)
    
    def updateGrille(self):
        ch.effacer_ecran()
        ch.curseur_invisible()
        pos = 5
        for i in self.__grilleUsr:
            with self.__ferme:
                ch.move_to(pos, 1)
                ch.erase_line_from_beg_to_curs()
                print(''.join(i))
            pos += 1
        ch.move_to(pos + 5, 1)
        
        
    
    def UpdateGrillleUsr(self, cellule, posLigne, posColonne):
        if cellule.getEtat():
            self.__grilleUsr[posLigne][posColonne] = "0"
        else:
            self.__grilleUsr[posLigne][posColonne] = "x"
            
    def getVoisins(self, posLigne, posColonne):
        voisins = []
        try:
            voisins.append(self.__grille[posLigne-1][posColonne-1])
        except IndexError:
            None
        
        try:
            voisins.append(self.__grille[posLigne-1][posColonne])
        except IndexError:
            None
        
        try:
            voisins.append(self.__grille[posLigne-1][posColonne+1])
        except IndexError:
            None
        
        try:
            voisins.append(self.__grille[posLigne][posColonne-1])
        except IndexError:
            None
        
        try:
            voisins.append(self.__grille[posLigne][posColonne+1])
        except IndexError:
            None
        
        try:
            voisins.append(self.__grille[posLigne+1][posColonne-1])
        except IndexError:
            None
        
        try:
            voisins.append(self.__grille[posLigne+1][posColonne])
        except IndexError:
            None
        
        try:
            voisins.append(self.__grille[posLigne+1][posColonne-1])
        except IndexError:
            None
        
        return voisins
    
    def presentVersFutur(self):
        for posLigne, ligne in enumerate(self.__grille):
            for posColonne, colonne in enumerate(ligne):
                colonne.update(self.getVoisins(posLigne, posColonne))
            for posLigne, ligne in enumerate(self.__grille):
                for posColonne, colonne in enumerate(ligne):
                    colonne.prstVersFutur()
                    self.UpdateGrillleUsr(colonne, posLigne, posColonne)
            self.updateGrille()
                    

class Cellule():
    
    def __init__(self, bool):
            self.__actuel = bool
            self.__etatSuivant = bool
    
    def celluleTuee(self):
        self.__etatSuivant = False
        
    def celluleCreee(self):
        self.__etatSuivant = True
    
    def getEtat(self):
        return self.__actuel
    
    def update(self, voisins):
        cellEnVie = 0
        for cellule in voisins:
            if cellule.getEtat() == True:
                cellEnVie += 1
                
        if self.__actuel == True :
            if cellEnVie < 2:
                self.celluleTuee()
            elif cellEnVie > 3:
                self.celluleTuee()
        else:
            if cellEnVie == 3:
                self.celluleCreee()
    
    def prstVersFutur(self):
        self.__actuel = self.__etatSuivant

tHauteur = int(input('quelle hauteur voulez-vous?'))
tLargeur = int(input('quelle largeur voulez-vous?'))
partie = Jeu(tHauteur,tLargeur)
partie.Grille()

while True:
    partie.presentVersFutur()
    time.sleep(2)