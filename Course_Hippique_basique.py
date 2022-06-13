# Cours hippique
# Version très basique, sans mutex sur l'écran, sans arbitre, sans annoncer le gagant, ... ...
'''
LAJUGIE Rodolphe
BARRIQUAND Valentin

Course hippique gérée avec multiprocessing
'''


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

# Actions sur les caractères affichables
NORMAL = "\x1B[0m"                  #  Normal
BOLD = "\x1B[1m"                    #  Gras
UNDERLINE = "\x1B[4m"               #  Souligné


# VT100 : Couleurs : "22" pour normal intensity
CL_BLACK="\033[22;30m"                  #  Noir. NE PAS UTILISER. On verra rien !!
CL_RED="\033[22;31m"                    #  Rouge
CL_GREEN="\033[22;32m"                  #  Vert
CL_BROWN = "\033[22;33m"                #  Brun
CL_BLUE="\033[22;34m"                   #  Bleu
CL_MAGENTA="\033[22;35m"                #  Magenta
CL_CYAN="\033[22;36m"                   #  Cyan
CL_GRAY="\033[22;37m"                   #  Gris

# "01" pour quoi ? (bold ?)
CL_DARKGRAY="\033[01;30m"               #  Gris foncé
CL_LIGHTRED="\033[01;31m"               #  Rouge clair
CL_LIGHTGREEN="\033[01;32m"             #  Vert clair
CL_YELLOW="\033[01;33m"                 #  Jaune
CL_LIGHTBLU= "\033[01;34m"              #  Bleu clair
CL_LIGHTMAGENTA="\033[01;35m"           #  Magenta clair
CL_LIGHTCYAN="\033[01;36m"              #  Cyan clair
CL_WHITE="\033[01;37m"                  #  Blanc
#-------------------------------------------------------
import multiprocessing as mp
 
import os, time,math, random, sys, ctypes, signal


verrou = mp.Lock()
# Définition de qq fonctions de gestion de l'écran
def effacer_ecran() : print(CLEARSCR,end='')
def erase_line_from_beg_to_curs() : print("\033[1K",end='')
def curseur_invisible() : print(CURSOFF,end='')
def curseur_visible() : print(CURSON,end='')
def move_to(lig, col) : print("\033[" + str(lig) + ";" + str(col) + "f",end='')

def en_couleur(Coul) : print(Coul,end='')
def en_rouge() : print(CL_RED,end='') # Un exemple !

#-------------------------------------------------------
# La tache d'un cheval
def un_cheval(ma_ligne : int, keep_running) : # ma_ligne commence à 0
    global places
    col=1

    while col < LONGEUR_COURSE and keep_running.value :

        verrou.acquire()

        move_to(ma_ligne+1,col)         # pour effacer toute ma ligne
        erase_line_from_beg_to_curs()
        en_couleur(lyst_colors[ma_ligne%len(lyst_colors)])
        print('['+chr(ord('A')+ma_ligne)+']>>')

        col+=1
        places[i] = col
        verrou.release()
        
        try : # En cas d'interruption
            time.sleep(0.1 * random.randint(1,5))
        finally : 
            pass
#--------------------------------------------------

# L'arbitre fait ça
'''
def arbitre():
    premier = -1
    while keep_running.value and premier !=  LONGEUR_COURSE:
        global places
        local_place = places[:]
        premier = (max(local_place))
        dernier = (min(local_place))
        ligneP = local_place.index(premier)
        ligneD = local_place.index(dernier)
        verrou.acquire()
        move_to(Nb_process+2,0)
        erase_line_from_beg_to_curs()
        print('Le cheval en tête est ', chr(ord('A')+ligneP))
        move_to(Nb_process+3,0)
        erase_line_from_beg_to_curs()
        print('Le cheval en tête en partant de la fin est ', chr(ord('A')+ligneD))
        verrou.release()
'''
def arbitre2():
    premier = -1
    dernier =-1
    global P
    while keep_running.value and dernier != LONGEUR_COURSE :
        global places
        local_place = places[:]
        verrou.acquire()
        if premier !=  LONGEUR_COURSE:
            premier = (max(local_place))
            ligneP = local_place.index(premier)           
            move_to(Nb_process+2,0)
            print('Le cheval en tête est ', chr(ord('A')+ligneP))
            P = chr(ord('A')+ligneP)

        if dernier != LONGEUR_COURSE-1:
            dernier = (min(local_place))
            ligneD = local_place.index(dernier)    
            move_to(Nb_process+3,0)
            print('Le cheval en tête en partant de la fin est ', chr(ord('A')+ligneD))
        verrou.release()

#-----------------------------------------------
# Process de prediction du gagant
def prediction():
    pred = input('Quel canasson va gagner ? (A to J)')
    return pred
    
    
#------------------------------------------------   
def prise_en_compte_signaux(signum, frame) :
    # On vient ici en cas de CTRL-C p. ex.
    move_to(Nb_process+11, 1)
    print(f"Il y a eu interruption No {signum} au clavier ..., on finit proprement")
    
    for i in range(Nb_process): 
        mes_process[i].terminate() 
    
    move_to(Nb_process+12, 1)
    curseur_visible()
    en_couleur(CL_WHITE)
    print("Fini")
    sys.exit(0)
# ---------------------------------------------------
# La partie principale :
if __name__ == "__main__" :
    global P
    # Une liste de couleurs à affecter aléatoirement aux chevaux
    lyst_colors=[CL_WHITE, CL_RED, CL_GREEN, CL_BROWN , CL_BLUE, CL_MAGENTA, CL_CYAN, CL_GRAY,
                CL_DARKGRAY, CL_LIGHTRED, CL_LIGHTGREEN,  CL_LIGHTBLU, CL_YELLOW, CL_LIGHTMAGENTA, CL_LIGHTCYAN]
    
    LONGEUR_COURSE = 50 # Tout le monde aura la même copie (donc no need to have a 'value')
    
    keep_running=mp.Value(ctypes.c_bool, True)

    pre = prediction()

    global places
    Nb_process=10
    
    places = mp.Array('i',Nb_process)
      
    
    mes_process = [0 for i in range(Nb_process)]
    arbitrePro = mp.Process(target = arbitre2, args = ())

     
    arbitrePro.start()
    
    signal.signal(signal.SIGINT , prise_en_compte_signaux)
    signal.signal(signal.SIGQUIT , prise_en_compte_signaux)

    effacer_ecran()
    curseur_invisible()

    for i in range(Nb_process):  # Lancer     Nb_process  processus
        mes_process[i] = mp.Process(target=un_cheval, args= (i,keep_running,))
        mes_process[i].start()

    move_to(Nb_process+10, 1)
    print("Tous lancés, Controle-C pour tout arrêter")

    

    # On attend la fin de la course
    arbitrePro.join()
    for i in range(Nb_process): mes_process[i].join() 
    if pre == P:
        print('Votre Prédiction était bonne vous avez gagné !')
    else :
        print('Votre prédiction était fausse dommage !')   

    move_to(Nb_process+12, 1)
    curseur_visible()
    keep_running.value= False
    print("Fini")
