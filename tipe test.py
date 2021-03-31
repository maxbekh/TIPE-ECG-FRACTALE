## Biblioteques
import csv
import numpy as np
import matplotlib.pyplot as plt
import os

## Fonctions auxiliaires
def liste(csvname):
    L=[]
    x=[]
    y=[]
    file = open(csvname)
    reader = csv.reader(file)
    for row in reader:
        L.append(row)
    for i in range(2,len(L)):
        y.append(float(L[i][1]))
        x.append(float(L[i][0]))
    return(x,y)
def affiche(name):
    plt.figure("")
    plt.plot(liste(name)[0],liste(name)[1])
    plt.xlabel("Temps (s)")
    plt.ylabel("Amplitudes")
    plt.grid()
    plt.show()


## Noyeau

def graph(name):
    cwd = os.getcwd()
    dir_list = os.listdir(cwd)
    folder = cwd+"/csvfiles"
    if not ("csvfiles" in dir_list):
        os.mkdir(folder)
    dir_list = os.listdir(folder)
    if not (name in dir_list):
        return(print("Erreur: il n'y a pas de",name,"dans le dossier",folder))
    affiche(folder+"/"+name)
