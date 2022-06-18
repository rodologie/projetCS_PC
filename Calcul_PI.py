"""
    30/05/2022j,
    Rodolphe Lajugie
    Vale,tin Barriquand
    Calcul de PI grâce à la méthode de monté carlo et calcul du temps
    Returns:
        float: estimation de PI
"""

import multiprocessing as mp
import random, time 

if __name__ == '__main__':
    #On utilise ici la mthode de monté-carlo
    temps_debut = time.time() #releve du temps au démarrage du script

    def frequence_de_hits_pour_n_essais(mutex, nb, itérations):
        
        nb = 0 #variable locale contenant le nombre hits pour ce quart
        for i in range(itérations):
            x = random.random() 
            y = random.random()
            if x*x + y*y <= 1: #On regarde si le point est dans le cercle unité
                nb += 1
            
        mutex.acquire() #On bloque l'acces à valeur
        valeur.value += nb #On ajoute le nombre d'essais
        mutex.release()
        return nb 


    mutex = mp.Lock() #On crée un verrou
    nb_total_iteration = 1000000
    nb_process = 4 #On choisit d'utiliser 4 process
    mes_process = [0 for i in range(nb_process)] #on crée une liste de process
    valeur = mp.Value("i", 0) #On crée une variable globale

    for i in range(nb_process): #on boucle pour chaque process
        mes_process[i] = mp.Process(target = frequence_de_hits_pour_n_essais, args = (mutex, valeur, int(nb_total_iteration/nb_process),)) 
        #on crée des process en leur donnant comme cible la fonction défini au début du script et comme argument
        mes_process[i].start() #lancement des process
        
    for i in range(nb_process):
        mes_process[i].join() #on attend que chaque process soit finit



    print("Pi :", 4*valeur.value/nb_total_iteration)
    print("Temps d'éxécution", time.time() - temps_debut) #différence temps actuel moins temps au démarage 