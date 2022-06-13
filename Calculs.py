from ast import arg
import os,time,array,sys
from struct import calcsize
import multiprocessing as mp
import random as rd


lstOpe=[]

if len(sys.argv)<2:
    print('Pas assez dargument')
elif len(sys.argv[1:])< int(sys.argv[1]) :
    print('Pas assez de calcul')
else :
    lstOpe.append(sys.argv[1:])


def demande(id): #nbc = nombre de calcule a faire

    for i in range(int(sys.argv[int(id)+2])):
        a = rd.randint(1,10)
        b = rd.randint(1,10)
        opp = rd.choice(['+','/','-','*'])
        calc = str(a) + opp + str(b)
        demande = str(id) + calc
        print('Je suis le demandeur '+str(id)+' et je veux calculer :'+calc)
        entree.put(demande)
        time.sleep(1)
    
        fils = mp.Process(target=calculateur,args=(id))
        fils.start()
        fils.join()

        res = sortie.get()
        if res[0] == str(id) :
            print('-'*60)
            print('Jai calculer la demande de ' + id + ' Je trouve ' + res[1:])
            print('-'*60)
        else:
            sortie.put(res)

def calculateur(id):
    verrou.acquire()
    calc1 = entree.get()
    fin_calc = str(id) + ' et je trouve ça : ' +  str(eval(calc1[1:]))
    
    #print('Je calcule la demande de ' ,fin_calc)
    
    sortie.put(fin_calc)
    verrou.release()

if __name__ == '__main__':
    
    entree = mp.Queue()
    sortie = mp.Queue()
    verrou = mp.Lock()
    dem = []

    for i in range(int(sys.argv[1])):
        dem.append(mp.Process(target = demande,args=(str(i))))
    for proc in dem :
        proc.start()
    for proc in dem :
        proc.join()
    
