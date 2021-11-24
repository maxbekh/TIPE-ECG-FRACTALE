## Biblioteques
import csv
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.stats import linregress
import time

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
        if L[i][1] == "-":
            a= (float(L[i-1][1])+float(L[i+1][1]))/2
            y.append(a)
        else:
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


def create_box(x,y,n,N):

    if N%n != 0:
        return "taille incompatible"
    coupesec = []
    coupeamp = []
    for i in range(int(N/n)) :
        coupesec.append(x[i*n:(i+1)*n])
        coupeamp.append(y[i*n:(i+1)*n])
    return coupesec,coupeamp




sec, amp = liste("/Users/maxence/csvfiles/samples.csv")
ampmoy = sum(amp)/len(amp)

def yfin(t):
    sol=0
    for i in range(1,t+1):
        sol+=amp[i]-ampmoy
    return sol

def yleast(x,y):
    a, b, r, p_value, std_err = linregress(x, y)
    return a,b

def fluctuation(n,x,y):
    N=len(x)
    coupesec,coupeamp = create_box(sec,amp,n,N)
    somme = 0
    ylist = []
    for i in range(len(coupesec)):
        ylist.append(yleast(coupesec[i],coupeamp[i]))
    for i in range(1,N):
        boite=i%n
        xboite,yboite = coupesec[boite],coupeamp[boite]
        a,b = ylist[boite][0],ylist[boite][1]
        somme+= (yfin(i)-(a*i+b))**2
    return np.sqrt(somme/N)


a=time.time()
findeur = fluctuation(130,sec,amp)
findeur2= fluctuation(91,sec,amp)
print(time.time()-a)

test = (log(findeur)/log(130))-(log(findeur2)/log(91))
##
test = (np.log(findeur2)-np.log(findeur))/(np.log(91)-np.log(130))