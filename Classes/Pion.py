from tkinter import *
import os
import random


class Pion:
     #chaque pions est relie a une liste de 3 chiffres qui correspondent aux
     #chiffres sur le pion et qui nous permettra de choisir l'image correspondant
     #ayant comme nom la suite des chiffres
     #une rotation correspondrait ainsi a une permutation des chiffres
     def __init__(self, name):
          self.name=name
          self.ref=[]
          #self.image=PhotoImage(file="pions/"+"".join(self.name)+".png")

     def setName(self, name):
          self.name=name
          #self.image=PhotoImage(file="pions/"+"".join(self.name)+".png")

     def Rotate(self, name):
         self.name="".join([name[5],name[0],name[1],name[2],name[3],name[4]])
         #self.image=PhotoImage(file="pions/"+"".join(self.name)+".png")

     def chargeImage(self, name):
         
         self.image=PhotoImage(file="pions/"+"".join(self.name)+".png")
         self.ref.append(self.image)

     #def RotateLeft():
      #   self.name=[self.name[1],self.name[2],self.name[0]]
         #self.image=PhotoImage(file=",".join(self.name)+".png")
