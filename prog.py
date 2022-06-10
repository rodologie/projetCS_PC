import sys, os


fct = input('Quel fichier voulez-vous executer ?')
lst=[fct,'.py']
file = ''.join(lst)

print("vous executer l'exercice %s" %file)
pid=os.fork()
if pid == 0:
    os.execlp('python3', 'python3', file )
else:
    os.wait()
    sys.exit(1)
