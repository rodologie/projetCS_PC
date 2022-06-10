import multiprocessing as mp
import random, time, os
import psutil, math

def sommePI(nb_Proc, nb_iteration, integrale):
    pi = 0.0
    for i in range(0,nb_iteration):
        pi += 4/(1+((i+0.5)/nb_iteration)**2)
    integrale.value += (1/nb_iteration)*pi


# MAIN

if __name__ == "__main__" :
    nb_processus=psutil.cpu_count() #8 sur un I7
    nb_total_iteration = 1000000    # Nombre d’essai pour l’estimation
    integrale = mp.Value('f', 0.0)

    debut_Temps = time.time()
    lst_pid = [0 for i in range(nb_processus)]
    for i in range(nb_processus):
        lst_pid[i] = mp.Process(target = sommePI, args = (i+1, nb_total_iteration // nb_processus, integrale))
        lst_pid[i].start()
        
        
    for i in range(nb_processus):
        lst_pid[i].join()
    
    print(f"Valeur estimée Pi par la méthode Arc−Tangente avec {nb_processus} processus: ", integrale.value/ nb_processus)
    print("Temps d’execution : ", time.time() - debut_Temps)
    print("erreur relative: ", math.pi - (integrale.value/ nb_processus))
