import os,time,sys
import multiprocessing as mp
import random as rd


def travailleur(block,nbb,nbt,m):
    """Fonction qui régis les travailleurs 

    Args:
        block (Lock): Le verrou qui sécurise le fonctionnement
        nbb (int): Nombre de bille que le travailleur a besoin
        nbt (int): Numéro du travailleur
        m (int): Nombre de fois qu'ils doivent travailler (non fonctionnel)
    """
    while True :
        for i in range(m):
            print('     Je suis '+ str(nbt) +' Je necessite '+str(nbb)+' billes')
            demander(block,nbb)
            print('Je suis '+str(nbt)+' et vais travailler')
            time.sleep(3)
            rendre(block,nbb)
            print('     Je suis' + str(nbt) + ' Fini de travailler voici mes billes rendu '+str(nbb))


def demander(block,nbb):
    """Permet de donner les billes s'il y en a asser

    Args:
        block (Lock): Le verrou qui sécurise le fonctionnement
        nbb (int): Nombre de bille nécessaire au travailleur
    """
    block.acquire()
    while billes.value < nbb:
        block.release()
        time.sleep(2)
        block.acquire()
    billes.value -= nbb
    block.release()

def rendre(block,nbb):
    """Permet de rendre les billes dans le 'pot' commun

    Args:
        block (Lock): Le verrou qui sécurise le fonctionnement
        nbb (int): Nombre de bille rendu par le travailleur
    """
    block.acquire()
    billes.value += nbb
    block.release()

def controle(block,bille):
    """Controle qu'il n'y ai pas de problème dans le nombre de bille totale (ps négatif et pas supérieur au nombre max)

    Args:
        block (Lock): Le verrou qui sécurise le fonctionnement
        bille (int): Nombre initiale de bille 
    """
    while True:
        block.acquire()
        if 0<=billes.value<=bille:
            block.release()
            time.sleep(1)
        else:
            print('Pas bon')
            time.sleep(1)


if __name__ == '__main__':
    bille = 8
    m = int(input('Combien de fois vous travailler ?'))
    billes = mp.Value('i',bille)
    block = mp.Lock()
    processL = []

    control = mp.Process(target=controle,args=(block,bille))
    processL.append(control)

    for i in range(3) :
        k = rd.randint(1,4)
        processL.append(mp.Process(target=travailleur,args=(block,k,i,m)))

    for proc in processL:
        proc.start()
    for proc in processL:
        proc.join()