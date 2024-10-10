from tkinter import *
import os
import random





class Game:
     
     def __init__(self,width,height):

          self.nombre_pioche=0 #Pour le nombre de fois que le joueur pioche

          self.premier=True #Pour savoir si il est le premier a jouer ou pas
          self.joueur_courant="Joueur 1"
          self.tableau=[]
          for i in range(height//50):
               self.ligne=[]
               for j in range(width//50):
                    self.ligne.append("aucun")
                    
               self.tableau.append(self.ligne)
               
          
     def changeJoueur(self):
          if self.joueur_courant=="Joueur 1":
               self.joueur_courant="Joueur 2"
          else:
               self.joueur_courant="Joueur 1"


     def updateTab(self,posx,posy,pion_selectionne):
          self.tableau[posy][posx]=pion_selectionne

     def isPosableNormal(self,pion,posx,posy):
          self.isPosable=False
          self.score=0
          
          self.gauche=False
          self.droite=False
          self.haut=False
          self.bas=False

          self.pont=False

          
          if(posx!=0 and self.tableau[posy][posx-1]!="place" and self.tableau[posy][posx-1]!="aucun"):
                 self.gauche=True
               
     
          if(posx!=len(self.tableau[posy])-1 and self.tableau[posy][posx+1]!="place" and self.tableau[posy][posx+1]!="aucun"):
               self.droite=True

               
          if(posy!=0 and self.tableau[posy-1][posx]!="place" and self.tableau[posy-1][posx]!="aucun"):
               self.haut=True
               
     
          if(posy!=len(self.tableau)-1 and self.tableau[posy+1][posx]!="place" and self.tableau[posy+1][posx]!="aucun"):
               self.bas=True

          #il doit pas y avoir de pion a gauche de celle posee, il doit y en avoir a droite deux pour un pont // PONT
          if(posx >= 3 and posx!=len(self.tableau[posy])-1 and posy!=0 and self.tableau[posy][posx-1]=="place" and self.tableau[posy][posx-2]!="place"
             and self.tableau[posy][posx-3]!="place" and self.tableau[posy][posx+1]!="place" and self.tableau[posy-1][posx]!="place"
             and self.tableau[posy-1][posx-1]!="place" and self.tableau[posy-1][posx-2]!="place" and self.tableau[posy-1][posx-3]!="place"
             and self.tableau[posy-1][posx+1]!="place" and
             self.tableau[posy][posx-1]=="aucun" and self.tableau[posy][posx-2]!="aucun"
             and self.tableau[posy][posx-3]!="aucun" and self.tableau[posy][posx+1]!="aucun" and self.tableau[posy-1][posx]!="aucun"
             and self.tableau[posy-1][posx-1]!="aucun" and self.tableau[posy-1][posx-2]!="aucun" and self.tableau[posy-1][posx-3]!="aucun"
             and self.tableau[posy-1][posx+1]!="aucun"):
               self.pont=True

          ####Verification de faisabilite s'il y'a un pion a gauche (un pion possede 3 caracteres x pour les rotations et 3 chiffres)
          #Avec le pion gauche
          if(pion!="place" and pion!="aucun" and self.gauche==True and self.bas==False and self.droite==False and pion[0]==(self.tableau[posy][posx-1])[5] and pion[2]==(self.tableau[posy][posx-1])[3]):
               self.isPosable=True
               self.score+=int(pion[0])+int(pion[2])+int(pion[4])
               

               #Definition des cases ou l'on peut deposer des pieces
               self.tableau[posy][posx+1]="place"
               self.tableau[posy+1][posx]="place"

               if(self.pont==True):
                    #+40 pour un pont realise
                    self.score+=40
          
          #Avec le pion bas
          elif(pion!="place" and pion!="aucun" and self.gauche==False and self.bas==True and self.droite==False and pion[0]==(self.tableau[posy+1][posx])[1] and pion[4]==(self.tableau[posy+1][posx])[3]):
               self.isPosable=True
               self.score+=int(pion[0])+int(pion[2])+int(pion[4])
              

               #Definition des cases ou l'on peut deposer des pieces
               self.tableau[posy][posx-1]="place"
               self.tableau[posy][posx+1]="place"
               

               if(self.pont==True):
                    #+40 pour un pont realise
                    self.score+=40
                    
          #Avec le pion droit
          elif(pion!="place" and pion!="aucun" and self.gauche==False and self.bas==False and self.droite==True and pion[4]==(self.tableau[posy][posx+1])[5] and pion[2]==(self.tableau[posy][posx+1])[1]):
               self.isPosable=True
               self.score+=int(pion[0])+int(pion[2])+int(pion[4])
               

               #Definition des cases ou l'on peut deposer des pieces
               self.tableau[posy][posx-1]="place"
               self.tableau[posy+1][posx]="place"

               if(self.pont==True):
                    #+40 pour un pont realise
                    self.score+=40
               
          #Avec les pions gauche et bas
          elif(pion!="place" and pion!="aucun" and self.gauche==True and self.bas==True and self.droite==False and pion[0]==(self.tableau[posy][posx-1])[5] and pion[2]==(self.tableau[posy][posx-1])[3]
               and pion[0]==(self.tableau[posy+1][posx])[1] and pion[4]==(self.tableau[posy+1][posx])[3]):
               self.isPosable=True
               self.score+=int(pion[0])+int(pion[2])+int(pion[4])
               

               #Definition des cases ou l'on peut deposer des pieces
               self.tableau[posy][posx+1]="place"
               

               if(self.pont==True):
                    #+40 pour un pont realise
                    self.score+=40
          
          #Avec les pions droit et bas
          elif(pion!="place" and pion!="aucun" and self.gauche==False and self.bas==True and self.droite==True and pion[4]==(self.tableau[posy][posx+1])[5] and pion[2]==(self.tableau[posy][posx+1])[1]
               and pion[0]==(self.tableau[posy+1][posx])[1] and pion[4]==(self.tableau[posy+1][posx])[3]):
               self.isPosable=True
               self.score+=int(pion[0])+int(pion[2])+int(pion[4])
               
               
               #Definition des cases ou l'on peut deposer des pieces
               self.tableau[posy][posx-1]="place"
               

               if(self.pont==True):
                    #+40 pour un pont realise
                    self.score+=40

          #Avec les pions gauche et droit
          elif(pion!="place" and pion!="aucun" and self.gauche==True and self.bas==False and self.droite==True and pion[0]==(self.tableau[posy][posx-1])[5] and pion[2]==(self.tableau[posy][posx-1])[3]
               and pion[4]==(self.tableau[posy][posx+1])[5] and pion[2]==(self.tableau[posy][posx+1])[1]):
               self.isPosable=True
               self.score+=int(pion[0])+int(pion[2])+int(pion[4])
               

               #Definition des cases ou l'on peut deposer des pieces
               self.tableau[posy+1][posx]="place"

               if(self.pont==True):
                    #+40 pour un pont realise
                    self.score+=40

          #Avec les pions gauche, droit et bas
          elif(pion!="place" and pion!="aucun" and self.gauche==True and self.bas==False and self.droite==True and pion[0]==(self.tableau[posy][posx-1])[5] and pion[2]==(self.tableau[posy][posx-1])[3]
               and pion[4]==(self.tableau[posy][posx+1])[5] and pion[2]==(self.tableau[posy][posx+1])[1]
               and pion[0]==(self.tableau[posy+1][posx])[1] and pion[4]==(self.tableau[posy+1][posx])[3]):
               
               self.isPosable=True
               self.score+=int(pion[0])+int(pion[2])+int(pion[4])
               

               if(self.pont==True):
                    #+40 pour un pont realise
                    self.score+=40

          #Avec aucun pion autour
          elif(self.gauche==False and self.bas==False and self.droite==False and self.premier==True and pion!="place" and pion!="aucun"):
               
               
               self.isPosable=True
               self.score+=int(pion[0])+int(pion[2])+int(pion[4])

               
          

          #print(self.gauche)
          #print(self.bas)
          #print(self.droite)
          #print(self.haut)
          #print("pont: ",self.pont)
          

     #################################################################################
     #Pour la case de triangle a l'envers #########################################################################################################################
     def isPosableInverse(self,pion,posx,posy):
          self.isPosable=False
          self.score=0
          #Un pion a l'enverse n'a jamais besoin de verification vers le pas car il ya son sommet
          self.gauche=False
          self.droite=False
          self.haut=False

          self.hexagone=False
          self.doubleHexagone=False
          

          
          if(posx!=0 and self.tableau[posy][posx-1]!="place" and self.tableau[posy][posx-1]!="aucun"):
                 self.gauche=True
               
     
          if(posx!=len(self.tableau[posy])-1 and self.tableau[posy][posx+1]!="place" and self.tableau[posy][posx+1]!="aucun"):
               self.droite=True

               
          if(posy!=0 and self.tableau[posy-1][posx]!="place" and self.tableau[posy-1][posx]!="aucun"):
               self.haut=True

          #il doit pas y avoir de pion a gauche de celle posee, il doit u en avoir a droite deux  // HEXAGONE
          if(posx >= 3 and posx!=len(self.tableau[posy])-1 and posy!=0 and self.tableau[posy][posx-1]!="place" and self.tableau[posy][posx-2]!="place"
             and self.tableau[posy-1][posx]!="place" and self.tableau[posy-1][posx-1]!="place" and self.tableau[posy-1][posx-2]!="place"
             and self.tableau[posy-1][posx-3]!="place" and self.tableau[posy-1][posx+1]!="place" and
             self.tableau[posy][posx-1]!="aucun" and self.tableau[posy][posx-2]!="aucun"
             and self.tableau[posy-1][posx]!="aucun" and self.tableau[posy-1][posx-1]!="aucun" and self.tableau[posy-1][posx-2]!="aucun"
             and self.tableau[posy-1][posx-3]!="aucun" and self.tableau[posy-1][posx+1]!="aucun"):
               self.hexagone=True

          #il doit pas y avoir de pion a gauche de celle posee, il doit u en avoir a droite deux // DOUBLE HEXAGONE
          if(posx >= 2 and posx<=len(self.tableau[posy])-3 and posy!=0 and self.tableau[posy][posx-1]!="place" and self.tableau[posy][posx-2]!="place"
             and self.tableau[posy][posx+1]!="place" and self.tableau[posy][posx+2]!="place" and self.tableau[posy-1][posx]!="place"
             and self.tableau[posy-1][posx-1]!="place" and self.tableau[posy-1][posx-2]!="place" and self.tableau[posy-1][posx+1]!="place"
             and self.tableau[posy-1][posx+2]!="place" and
             self.tableau[posy][posx-1]!="aucun" and self.tableau[posy][posx-2]!="aucun"
             and self.tableau[posy][posx+1]!="aucun" and self.tableau[posy][posx+2]!="aucun" and self.tableau[posy-1][posx]!="aucun"
             and self.tableau[posy-1][posx-1]!="aucun" and self.tableau[posy-1][posx-2]!="aucun" and self.tableau[posy-1][posx+1]!="aucun"
             and self.tableau[posy-1][posx+2]!="aucun"):
               self.doubleHexagone=True


          ####Verification de faisabilite s'il y'aun pion a gauche (un pion possede 3 caracteres x pour les rotations et 3 chiffres)
          #Avec le pion gauche
          if(pion!="place" and pion!="aucun" and self.gauche==True and self.haut==False and self.droite==False and pion[5]==(self.tableau[posy][posx-1])[4] and pion[1]==(self.tableau[posy][posx-1])[2]):
               self.isPosable=True
               self.score+=int(pion[1])+int(pion[3])+int(pion[5])
              

               #Definition des cases ou l'on peut deposer des pieces
               self.tableau[posy][posx+1]="place"
               self.tableau[posy-1][posx]="place"

               if(self.hexagone==True):
                    #+50 pour un hexagone realise
                    self.score+=50
               elif(self.doubleHexagone==True):
                    #+60 pour un double hexagone realise
                    self.score+=60
          
          #Avec le pion haut
          elif(pion!="place" and pion!="aucun" and self.gauche==False and self.haut==True and self.droite==False and pion[1]==(self.tableau[posy-1][posx])[0] and pion[3]==(self.tableau[posy-1][posx])[4]):
               self.isPosable=True
               self.score+=int(pion[1])+int(pion[3])+int(pion[5])
               

               #Definition des cases ou l'on peut deposer des pieces
               self.tableau[posy][posx+1]="place"
               self.tableau[posy][posx-1]="place"

               if(self.hexagone==True):
                    #+50 pour un hexagone realise
                    self.score+=50
               elif(self.doubleHexagone==True):
                    #+60 pour un double hexagone realise
                    self.score+=60
                    
          #Avec le pion droit
          elif(pion!="place" and pion!="aucun" and self.gauche==False and self.haut==False and self.droite==True and pion[5]==(self.tableau[posy][posx+1])[0] and pion[3]==(self.tableau[posy][posx+1])[2]):
               self.isPosable=True
               self.score+=int(pion[1])+int(pion[3])+int(pion[5])
              

               #Definition des cases ou l'on peut deposer des pieces
               self.tableau[posy][posx-1]="place"
               self.tableau[posy-1][posx]="place"

               if(self.hexagone==True):
                    #+50 pour un hexagone realise
                    self.score+=50
               elif(self.doubleHexagone==True):
                    #+60 pour un double hexagone realise
                    self.score+=60
               
          #Avec les pions gauche et haut
          elif(pion!="place" and pion!="aucun" and self.gauche==True and self.haut==True and self.droite==False and pion[5]==(self.tableau[posy][posx-1])[4] and pion[1]==(self.tableau[posy][posx-1])[2]
               and pion[1]==(self.tableau[posy-1][posx])[0] and pion[3]==(self.tableau[posy-1][posx])[4]):
               self.isPosable=True
               self.score+=int(pion[1])+int(pion[3])+int(pion[5])
               

               #Definition des cases ou l'on peut deposer des pieces
               self.tableau[posy][posx+1]="place"


               if(self.hexagone==True):
                    #+50 pour un hexagone realise
                    self.score+=50
               elif(self.doubleHexagone==True):
                    #+60 pour un double hexagone realise
                    self.score+=60
          
          #Avec les pions droit et haut
          elif(pion!="place" and pion!="aucun" and self.gauche==False and self.haut==True and self.droite==True and pion[5]==(self.tableau[posy][posx+1])[0] and pion[3]==(self.tableau[posy][posx+1])[2]
               and pion[1]==(self.tableau[posy-1][posx])[0] and pion[3]==(self.tableau[posy-1][posx])[4]):
               self.isPosable=True
               self.score+=int(pion[1])+int(pion[3])+int(pion[5])
               

               #Definition des cases ou l'on peut deposer des pieces
               self.tableau[posy][posx-1]="place"
     

               if(self.hexagone==True):
                    #+50 pour un hexagone realise
                    self.score+=50
               elif(self.doubleHexagone==True):
                    #+60 pour un double hexagone realise
                    self.score+=60

          #Avec les pions gauche et droit
          elif(pion!="place" and pion!="aucun" and self.gauche==True and self.haut==False and self.droite==True and pion[5]==(self.tableau[posy][posx-1])[4] and pion[1]==(self.tableau[posy][posx-1])[2]
               and pion[5]==(self.tableau[posy][posx+1])[0] and pion[3]==(self.tableau[posy][posx+1])[2]):
               self.isPosable=True
               self.score+=int(pion[1])+int(pion[3])+int(pion[5])
               

               #Definition des cases ou l'on peut deposer des pieces
               self.tableau[posy-1][posx]="place"

               if(self.hexagone==True):
                    #+50 pour un hexagone realise
                    self.score+=50
               elif(self.doubleHexagone==True):
                    #+60 pour un double hexagone realise
                    self.score+=60

          #Avec les pions gauche, droit et haut
          elif(pion!="place" and pion!="aucun" and self.gauche==True and self.haut==False and self.droite==True and pion[5]==(self.tableau[posy][posx-1])[4] and pion[1]==(self.tableau[posy][posx-1])[2]
               and pion[5]==(self.tableau[posy][posx+1])[0] and pion[3]==(self.tableau[posy][posx+1])[2]
               and pion[1]==(self.tableau[posy-1][posx])[0] and pion[3]==(self.tableau[posy-1][posx])[4]):
               
               self.isPosable=True
               self.score+=int(pion[1])+int(pion[3])+int(pion[5])
               

               if(self.hexagone==True):
                    #+50 pour un hexagone realise
                    self.score+=50
               elif(self.doubleHexagone==True):
                    #+60 pour un double hexagone realise
                    self.score+=60

          #Avec aucun pion autour
          elif(self.gauche==False and self.haut==False and self.droite==False and self.premier==True and pion!="place" and pion!="aucun"):

               
               self.isPosable=True
               self.score+=int(pion[1])+int(pion[3])+int(pion[5])

               
               
               

          #print(self.gauche)
          #print(self.haut)
          #print(self.droite)
          #print("Hexagone: ",self.hexagone)
          #print("Double Hexagone: ",self.doubleHexagone)
         
