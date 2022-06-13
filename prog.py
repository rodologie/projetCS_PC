import sys, os


fct = input('Quel fichier voulez-vous executer ?')

lst_FCT=['Calcul_PI.py']
lst=[fct,'.py']
file = ''.join(lst)


pid=os.fork()
if pid == 0:
    if file in lst_FCT:
        print("vous executer l'exercice %s" %file)
        os.execlp('python3', 'python3', file )
    else:
        print("Fichiers introuvable, vérifier l'orthographe")
else:
    os.wait()
    sys.exit(0)
