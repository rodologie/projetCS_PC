from ast import arg
import os,time,array,sys
from struct import calcsize
import multiprocessing as mp
import random as rd


lstOpe=[]

lstArg = []
lstArg.append(int(input('Combien de demandeur ? : ')))

for i in range(lstArg[0]):
    cbcalc = int(input('Combien de calcul pour le demandeur '+str(i+1)+' : '))
    lstArg.append(cbcalc)
    
def demande(id): 
    """Créer aléatoirement un calcul et l'envoie au calculateur pour enfin le recevoir et afficher le résultat

    Args:
        id (str): L'id du demandeur, son numéro
    """

    for i in range(lstArg[int(id)+1]):
        a = rd.randint(1,10)
        b = rd.randint(1,10)
        opp = rd.choice(['+','/','-','*'])
        calc = str(a) + opp + str(b)
        demande = str(id) + calc
        print('*'*60)
        print('     Je suis le demandeur '+str(int(id)+1)+' et je veux calculer :'+calc)
        print('*'*60)
        entree.put(demande)
        time.sleep(1)
    
        fils = mp.Process(target=calculateur,args=(id))
        fils.start()
        fils.join()

        res = sortie.get()
        if res[0] == str(id) :
            print('-'*60)
            print('Jai calculer la demande de ' + str(int(id)+1) + res[1:])
            print('-'*60)
        else:
            sortie.put(res)

def calculateur(id):
    """Fait le calcul qui lui à été envoyé

    Args:
        id (str): L'id du demandeur afin de la renvoyer dans le résultat pour identifier celui-ci avec la demande
    """
    
    verrou.acquire()
    calc1 = entree.get()
    fin_calc = str(id) + ' et je trouve ça : ' +  str(eval(calc1[1:]))
    sortie.put(fin_calc)
    verrou.release()

if __name__ == '__main__':
    """Création des Queue et du verrou ainsi que lancement des processus
    """
    
    entree = mp.Queue()
    sortie = mp.Queue()
    verrou = mp.Lock()
    dem = []

    for i in range(lstArg[0]):
        dem.append(mp.Process(target = demande,args=(str(i))))
    for proc in dem :
        proc.start()
    for proc in dem :
        proc.join()
    
