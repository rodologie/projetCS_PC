import multiprocessing as mp
import random, time
import numpy as np
import Course_Hippique_basique as ch




class Jeu():
    """
    classe qui gere la grille.
    chaque casse de la grille est une élélment de classe cellule
    """
    def __init__(self, Hauteur, Largeur):
        self.__hauteurGrille = Hauteur
        self.__largeurGrille = Largeur
        self.__grilleUsr = []
        self.__grille = []
        self.__ferme = mp.Lock()
    
    
    def Grille(self):
        """
        fonction qui met affiche la grille de eju
        """
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
        """
        fonction qui met à jour la grille de facon interne 
        """
        ch.effacer_ecran()
        ch.curseur_invisible()
        pos = 8
        for i in self.__grilleUsr:
            with self.__ferme:
                ch.move_to(pos, 43)
                ch.erase_line_from_beg_to_curs()
                print(''.join(i))
            pos += 1
        ch.move_to(pos + 8, 1)
        
        
    
    def UpdateGrillleUsr(self, cellule, posLigne, posColonne):
        
        """
        fonction qui met à jour la grille de l'utilisateur
        """
        
        if cellule.getEtat():
            self.__grilleUsr[posLigne][posColonne] = "0"
        else:
            self.__grilleUsr[posLigne][posColonne] = "x"
            
    def getVoisins(self, posLigne, posColonne):
        """
        fonction qui recupere le nombre de voisins vivant de chaque case afin de savoir si celui-ci
            - vit toujours
            - meurt
            - revit
        on utilise la méthode try/Except pour éviter le probleme du type IndexError lorsque l'on est sur les cellule au bord du tableau

        Args:
            posLigne (int): position de sa ligne
            posColonne (_type_): position de sa colonne 
        """
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
        """
        fonction qui met à jour la grille utilisateur en recuperant la grille stocké en interne
        """
        for posLigne, ligne in enumerate(self.__grille):
            for posColonne, colonne in enumerate(ligne):
                colonne.update(self.getVoisins(posLigne, posColonne))
            for posLigne, ligne in enumerate(self.__grille):
                for posColonne, colonne in enumerate(ligne):
                    colonne.prstVersFutur()
                    self.UpdateGrillleUsr(colonne, posLigne, posColonne)
            self.updateGrille()
                    

class Cellule():
    """
    classe qui gère chaque cellule de la grille
    """
    
    def __init__(self, bool):
        """
        chaque cellule est de type booléenne: vivante ou morte

        Args:
            bool (booleen): vivant / mort
        """
        self.__actuel = bool
        self.__etatSuivant = bool
    
    def celluleTuee(self):
        """
        on tu ela cellule
        """
        self.__etatSuivant = False
        
    def celluleCreee(self):
        """
        on fait revivre la cellule
        """
        self.__etatSuivant = True
    
    def getEtat(self):
        
        """
        getteur qui permet de savoir si la cellule est vivante ou décédée

        Returns:
            booleen : vivant / mort
        """
        return self.__actuel
    
    def update(self, voisins):
        """
        Pour chaque cellule, cette fonction va déterminer sur sur la prochaine grille la cellule sera toujours vivante ou non

        Args:
            voisins (liste): contient les voisins de la cellule testée
        """
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
        """
        actualise la cellule en récupérant l'état de la cellule dans la mémoire
        """
        self.__actuel = self.__etatSuivant

tHauteur = int(input('quelle hauteur voulez-vous?'))
tLargeur = int(input('quelle largeur voulez-vous?'))
partie = Jeu(tHauteur,tLargeur)
partie.Grille()

while True:
    partie.presentVersFutur()
    time.sleep(0.5)