from tkinter import *
import os
import random




class Player :

     def __init__(self,liste_des_pions):
           #self.name=name
           self.score=0
           self.pions=[] #la liste des 7 pions aleatoirement choisi dans la liste de l'ensemble des 56 pions
           for i in range(7):
                self.aleatoire=random.randint(0,len(liste_des_pions)-1)
                self.pions.append(liste_des_pions[self.aleatoire])
                liste_des_pions.pop(self.aleatoire)
