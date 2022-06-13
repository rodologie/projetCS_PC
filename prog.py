import sys, os

lst_FCT=['Calcul_PI.py','Course_Hippique_basique.py']
print('Les fonctions disponibles sont:', lst_FCT)
fct = input('Quel fichier voulez-vous executer (sans le .py)?')


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
