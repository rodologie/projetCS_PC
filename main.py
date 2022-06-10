import sys, os

print("vous executer l'exercice %s" %sys.argv[1])

os.execlp('python3', 'python3', sys.argv[1])

