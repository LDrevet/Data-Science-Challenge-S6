# -*- coding: utf-8 -*-
"""
Created on Sat May  9 11:43:02 2020

@author: utilisateur
"""

import math
import csv
fichier_csv = open(r'data.csv','r')
ligne=csv.reader(fichier_csv, delimiter=";")
Fichier_final=list(ligne)
for i in range(len(Fichier_final)):
    for j in range(4):
        Fichier_final[i][j]=float(Fichier_final[i][j])
fichier_csv2 = open(r'finalTest.csv','r')
ligne2=csv.reader(fichier_csv2, delimiter=";")
Fichier_final2=list(ligne2)
for i in range(len(Fichier_final2)):
    for j in range(4):
        Fichier_final2[i][j]=float(Fichier_final2[i][j])


def distance(x,y):
    somme=0
    p = 1.1
    for i in range(len(x)-1):
        somme+=math.pow(abs(x[i]-y[i]),p)
    return somme**(1/p)

    
def knn(x,k):
    listedistance=[]
    for i in range(len(Fichier_final)):
        if x!=Fichier_final[i]:
            listedistance.append([Fichier_final[i],distance(x,Fichier_final[i])])
    for l in range(1,len(listedistance)):
        temp=listedistance[l]
        temp1=listedistance[l][1]
        j=l
        while j>0 and temp1<listedistance[j-1][1]:
            listedistance[j]=listedistance[j-1]
            j-=1
        listedistance[j]=temp
    listekvoisins=[]
    for i in range(0,k):
        listekvoisins.append(listedistance[i][0][4])
    return listekvoisins
    
def predire_classe(x,k):
    liste_kvoisins=knn(x,k)
    etiquettes = ['A','B','C','D','E','F','G','H','I','J']
    cpt = [0,0,0,0,0,0,0,0,0,0]
    for i in range(len(liste_kvoisins)):
        for j in range(10):
            if i>=0 and i<=6 and liste_kvoisins[i] == etiquettes[j]: 
                cpt[j] += 10
            if i>=7 and i<=13 and liste_kvoisins[i] == etiquettes[j]: 
                cpt[j] += 5
            if i>=14 and i<=20 and liste_kvoisins[i] == etiquettes[j]: 
                cpt[j] += 2
            if i>=21  and liste_kvoisins[i] == etiquettes[j]: 
                cpt[j] += 1
    cpt_max=cpt[0]
    z = 0
    for i in range (1,10):
        if cpt[i] > cpt_max:
            cpt_max = cpt[i]
            z = i
    return etiquettes[z]

Fichier_test=[]
#marge_precision=len(Fichier_final2)
for i in range(len(Fichier_final2)):
    Fichier_test.append(predire_classe(Fichier_final2[i],32))
#    if Fichier_test[i]!=Fichier_final2[i][4]:
#        marge_precision-=1
#marge_precision=(marge_precision*100)/len(Fichier_final2)
Nouveau=open(r'labels.txt','w')
for i in Fichier_test:
    Nouveau.write(i+"\n")
Nouveau.close()
print(Fichier_test)
#print(marge_precision)


    
