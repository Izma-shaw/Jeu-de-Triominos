from tkinter import *
import os
import random
from Classes import Pion
from Classes import Player
from Classes import Game

#PROGRAMME PRINCIPAL LIGNE 623 /////////////////////////////// 



#========================================================================================================
#FONCTION INTELLIGENCE ARTIFICIELLE
def IA():
    resultats=[] #liste à 2 dimensions contenant les pieces que l'IA peut poser, la position ou l'on peut les poser et les points donnent
    coup_initial=""
    meilleur_coup=""
    meilleur_position=[]
    meilleur_score=0 #Pour les points que rapporte le meilleur coup
    
    
    for y in range(len(jeu.tableau)) : #On parcours le tableau a la recherche de cases ou l'on peut poser la piece
        for x in range(len(jeu.tableau[0])) :
            if(jeu.tableau[y][x]=="place"): #Si l'on tombe sur une case ou l'on peut poser la piece
                #print(x,",",y)
                for piece in list_de_mes_pions2: #On on teste une par une toutes les pieces de l'IA
                    
                    pion_selectionne.setName(piece)

              
                    for i in range(6): #Nombre de rotations a faire
                        
                                                
                        if(pion_selectionne.name[0]!="x"): #Si la piece n'est pas inversé
                            #print([pion_selectionne.name,[x,y],int(pion_selectionne.name[0])+int(pion_selectionne.name[2])+int(pion_selectionne.name[4])])
                            jeu.isPosableNormal(pion_selectionne.name,x,y)

                            if(jeu.isPosable==True): #Si la piece est posable
                                resultats.append([piece,pion_selectionne.name,[x,y],int(pion_selectionne.name[0])+int(pion_selectionne.name[2])+int(pion_selectionne.name[4])])
                                                 
                        else: #Si la piece est à l'envers
                            #print([pion_selectionne.name,[x,y],int(pion_selectionne.name[1])+int(pion_selectionne.name[3])+int(pion_selectionne.name[5])])
                            jeu.isPosableInverse(pion_selectionne.name,x,y)

                            if(jeu.isPosable==True): #Si la piece est posable
                                resultats.append([piece,pion_selectionne.name,[x,y],int(pion_selectionne.name[1])+int(pion_selectionne.name[3])+int(pion_selectionne.name[5])])

                        
                        pion_selectionne.Rotate(pion_selectionne.name)
                        
            else:
                 pass

    print ("resultats: ",len(resultats),resultats)

    #Recherche du meilleur coup (celui qui donne le plus de points)
    if(len(resultats)!=0): #Si on eu des resultats
        for i in range(len(resultats)):
            if (meilleur_score <= resultats[i][3]):
                
                coup_initial=resultats[i][0]
                meilleur_coup=resultats[i][1]
                meilleur_position=resultats[i][2]
                meilleur_score=resultats[i][3]

        #print ("Meilleur coup: ",meilleur_coup)
        #print ("Meilleur score: ",meilleur_score)
        #print ("Meilleur position: ",meilleur_position)

    else: #Si l'IA ne trouve n'a pas des pieces que l'on peut poser
        piocher()
        if(jeu.joueur_courant== "Joueur 2"):
            IA()
        
        

    
        
                
    if (meilleur_coup!="" and meilleur_coup[0]!="x"):
        #Calcule des autres points du triangle normal a partir d'un seul point 
        centerX=((meilleur_position[0]*50)+(meilleur_position[0]*50+50)+(meilleur_position[0]*50+100))//3
        centerY=((meilleur_position[1]*50+50)+(meilleur_position[1]*50)+(meilleur_position[1]*50+50))//3
        pion_selectionne.setName(meilleur_coup)
        #mise a jour du tableau //////////
        jeu.updateTab(meilleur_position[0],meilleur_position[1],pion_selectionne.name)
        #On disssine l'image de la piece sur le plateau
        pion_selectionne.chargeImage(meilleur_coup)
        img=c.create_image(centerX+2.5,centerY-4.8,image=pion_selectionne.image,state="disable",anchor="center")
        #On retire la piece pose dans la baque de pieces de l'IA
        index_pion=list_de_mes_pions2.index(coup_initial)
        list_de_mes_pions2.pop(index_pion)
        print(list_de_mes_pions2)
        #Mise a jour du score
        joueur2.score+=meilleur_score
        iScoreJoueur2.config(text="Score IA: "+str(joueur2.score))
        #Mise a jour de la piece active
        pion_selectionne.setName("aucun")
        iPionSelectionne.config(text="Pion Selectionné: aucun") #Pour mettre le nom du Pion 
        #Recreation du plateau de jeu       
        c.delete("normal")
        gamePlate(800,500)
        
        #Mise à jour du joueur courant
        jeu.changeJoueur()

    elif(meilleur_coup!="" and meilleur_coup[0]=="x"):
        #Calcule des autres points du triangle inverse a partir d'un seul point 
        centerX=((meilleur_position[0]*50)+(meilleur_position[0]*50+50)+(meilleur_position[0]*50+100))//3
        centerY=((meilleur_position[1]*50)+(meilleur_position[1]*50+50)+(meilleur_position[1]*50))//3
        pion_selectionne.setName(meilleur_coup)
        #mise a jour du tableau //////////
        jeu.updateTab(meilleur_position[0],meilleur_position[1],pion_selectionne.name)
        #On disssine l'image de la piece sur le plateau
        pion_selectionne.chargeImage(meilleur_coup)
        img=c.create_image(centerX+2.5,centerY-5.5,image=pion_selectionne.image,state="disable",anchor="center")
        #On retire la piece pose dans la baque de pieces de l'IA
        index_pion=list_de_mes_pions2.index(coup_initial)
        list_de_mes_pions2.pop(index_pion)
        print(list_de_mes_pions2)
        #Mise a jour du score
        joueur2.score+=meilleur_score
        iScoreJoueur2.config(text="Score IA: "+str(joueur2.score))
        #Mise a jour de la piece active
        pion_selectionne.setName("aucun")
        iPionSelectionne.config(text="Pion Selectionné: aucun") #Pour mettre le nom du Pion 
        #Recreation du plateau de jeu       
        c.delete("inverse")
        gamePlate(800,500)
        
        #Mise à jour du joueur courant
        jeu.changeJoueur()


    #print("IA Poins: ",list_de_mes_pions2)
        

        
        
                
                
                

#========================================================================================================
#FONCTION DU BOUTTON RECOMMENCER 

def recommencer():
     root.destroy()
     os.system("Triominos_IA.py")
     
#========================================================================================================
#FONCTION DU BOUTTON QUITTER
     
def quitter():
     root.destroy()
     os.system("Jeu_Triominos.py")
         
       

#========================================================================================================
#FONCTION DU BOUTTON PIOCHER

def piocher():
     if jeu.joueur_courant=="Joueur 1" and len(list_de_mes_pions)<12 and len(liste_des_pions)!=0:

          #Mise à jour du score du joueur moins 5 a chaque fois que l'on pioche
          jeu.nombre_pioche+=1
          joueur1.score-=5
          iScoreJoueur1.config(text="Score Joueur 1: "+str(joueur1.score))
          
          
          nb_aleatoire=random.randint(0,len(liste_des_pions)-1)
          list_de_mes_pions.append(liste_des_pions[nb_aleatoire])
          list_images_pions.append(PhotoImage(file="pions/"+liste_des_pions[nb_aleatoire]+".png"))
          c1.delete("all")
          mesPions(225,300,list_de_mes_pions,list_images_pions,c1,jeu.joueur_courant)
          liste_des_pions.pop(nb_aleatoire)
          
          iPionSelectionne.config(text="Pion Selectionné: "+list_de_mes_pions[-1]) #Pour mettre le nom du Pion pioché
          pion_selectionne.setName(list_de_mes_pions[-1])

          #moins 10 points de plus si le jouer pioche jusqu'à 3 fois
          if(jeu.nombre_pioche==3):
               joueur1.score-=10
               iScoreJoueur1.config(text="Score Joueur 1: "+str(joueur1.score))
               jeu.nombre_pioche=0 #On remet à 0
               pion_selectionne.setName("aucun")
               iPionSelectionne.config(text="Pion Selectionné: aucun") #Pour mettre le nom du Pion pioché
               #Mise à jour du joueur courant
               jeu.changeJoueur()
               gagnant()
               IA()
          
          
          #Message d'erreur
          iErreur.config(text="")
          #print(liste_des_pions)
          
     elif jeu.joueur_courant=="Joueur 2" and len(list_de_mes_pions2)<12 and len(liste_des_pions)!=0:

          #Mise à jour du score du joueur moins 5 a chaque fois que l'on pioche
          jeu.nombre_pioche+=1
          joueur2.score-=5
          iScoreJoueur2.config(text="Score IA: "+str(joueur2.score))
          

               
          
          nb_aleatoire=random.randint(0,len(liste_des_pions)-1)
          list_de_mes_pions2.append(liste_des_pions[nb_aleatoire])

          liste_des_pions.pop(nb_aleatoire)
          
          iPionSelectionne.config(text="Pion Selectionné: "+list_de_mes_pions2[-1]) #Pour mettre le nom du Pion pioché
          pion_selectionne.setName(list_de_mes_pions2[-1])

          #mois 10 points de plus si le jouer pioche jusqu'à 3 fois
          if(jeu.nombre_pioche==3):
               joueur2.score-=10
               iScoreJoueur2.config(text="Score IA: "+str(joueur2.score))
               jeu.nombre_pioche=0 #On remet à 0
               pion_selectionne.setName("aucun")
               iPionSelectionne.config(text="Pion Selectionné: aucun") #Pour mettre le nom du Pion pioché
               #Mise à jour du joueur courant
               jeu.changeJoueur()
               gagnant()
          
          
          #Message d'erreur
          iErreur.config(text="")
          #print(liste_des_pions)

     if jeu.joueur_courant=="Joueur 1" and (len(list_de_mes_pions)==12 or len(liste_des_pions)==0):
          pion_selectionne.setName("aucun")
          jeu.nombre_pioche=0 #On remet à 0
          #Mise à jour du joueur courant
          c1.delete("all")
          mesPions(225,300,list_de_mes_pions,list_images_pions,c1,jeu.joueur_courant)
          
          

          iPionSelectionne.config(text="Pion Selectionné: aucun") #Pour mettre le nom du Pion pioché
          
          jeu.changeJoueur()
          gagnant()

     elif jeu.joueur_courant=="Joueur 2" and (len(list_de_mes_pions2)==12 or len(liste_des_pions)==0):
          pion_selectionne.setName("aucun")
          jeu.nombre_pioche=0 #On remet à 0
          #Mise à jour du joueur courant
          

          iPionSelectionne.config(text="Pion Selectionné: aucun") #Pour mettre le nom du Pion pioché
          
          jeu.changeJoueur()
          gagnant()



#========================================================================================================
#CALLBACK DES TRIANGLES NON INVERSES
          
def callback(event):
     
     x = event.x
     y = event.y
     triangle = c.find_closest(x,y)[0]
     
     coords=c.coords(triangle)
     if(jeu.premier==False): #Pour savoir si il est le premier a jouer ou pas
          centerX=(coords[0]+coords[2]+coords[4])/3
          centerY=(coords[1]+coords[3]+coords[5])/3
     else:
          centerX=((7*50)+(7*50+50)+(7*50+100))//3
          centerY=((5*50+50)+(5*50)+(5*50+50))//3

     jeu.isPosableNormal(pion_selectionne.name,int(coords[0]/50),int((coords[1]-50)/50))
     if (jeu.tableau[int((coords[1]-50)/50)][int(coords[0]/50)]=="aucun" or jeu.tableau[int((coords[1]-50)/50)][int(coords[0]/50)]=="place") and pion_selectionne.name[0]!="x" and jeu.isPosable==True:
          iErreur.config(text="")#Pour supprimer le message d'erreur
          if(pion_selectionne.name != "aucun" and jeu.joueur_courant== "Joueur 1"):

                 #Effacer le Message d'erreur
                 iErreur.config(text="")
                 
                 jeu.nombre_pioche=0 #On remet à 0
                  
                 #Mise à jour du score du joueur
                 joueur1.score+=jeu.score
                 iScoreJoueur1.config(text="Score Joueur 1: "+str(joueur1.score))
                 
                 if(jeu.premier==False): #Pour savoir si il est le premier a jouer ou pas
                      #mise a jour du tableau /////////
                      jeu.updateTab(int(coords[0]/50),int((coords[1]-50)/50),pion_selectionne.name)
                      #for i in range(len(jeu.tableau)):
                           #print(jeu.tableau[i])

                 else:
                     jeu.premier=False
                     jeu.updateTab(7,5,pion_selectionne.name)
                     #Definition des cases ou l'on peut deposer des pieces
                     jeu.tableau[5][7-1]="place"
                     jeu.tableau[5][7+1]="place"
                     jeu.tableau[5+1][7]="place"
                    
                 
                 #pion=PhotoImage(file="pions/"+pion_selectionne.name+".png")

                 #Poser la piece sur le plateau
                 pion_selectionne.chargeImage(pion_selectionne.name)
                 img=c.create_image(centerX+2.5,centerY-4.8,image=pion_selectionne.image,state="disable",anchor="center")
                       
                      

                 #retirer l'image de la liste d'image
                 list_images_pions.pop(list_de_mes_pions.index(pion_selectionne.name))
                 list_de_mes_pions.remove(pion_selectionne.name)
                 
                 print(pion_selectionne.name)
                 pion_selectionne.setName("aucun")
                 iPionSelectionne.config(text="Pion Selectionné: aucun") #Pour mettre le nom du Pion 
                 
                 c.delete("normal")
                 gamePlate(800,500)
                 c1.delete("all")
                  
                 mesPions(225,300,list_de_mes_pions,list_images_pions,c1,jeu.joueur_courant)
                 
                 #Mise à jour du joueur courant
                 jeu.changeJoueur()
                
                 gagnant()
                 IA()

     else:
         #Message d'erreur
         iErreur.config(text="Vous ne pouvez pas placer le pion ici ou Vous n'avez pas sectionné de pion")
                 
                 
     


#========================================================================================================
#CALLBACK DES TRIANGLES INVERSES
     
def callback2(event):
     
     x = event.x
     y = event.y
     triangle = c.find_closest(x,y)[0]
     
     coords=c.coords(triangle)
     if(jeu.premier==False): #Pour savoir si il est le premier a jouer ou pas
          centerX=(coords[0]+coords[2]+coords[4])/3
          centerY=(coords[1]+coords[3]+coords[5])/3
     else:
          centerX=((7*50)+(7*50+50)+(7*50+100))//3
          centerY=((6*50)+(6*50+50)+(6*50))//3

     
     jeu.isPosableInverse(pion_selectionne.name,int(coords[0]/50),int((coords[3]-50)/50))
     if (jeu.tableau[int((coords[3]-50)/50)][int(coords[0]/50)]=="aucun" or jeu.tableau[int((coords[3]-50)/50)][int(coords[0]/50)]=="place") and pion_selectionne.name[0]=="x" and jeu.isPosable==True:
          iErreur.config(text="")#Pour supprimer le message d'erreur
          if(pion_selectionne.name != "aucun" and jeu.joueur_courant== "Joueur 1"):

                 #Effacer le Message d'erreur
                 iErreur.config(text="")

                 jeu.nombre_pioche=0 #On remet à 0

                 #Mise à jour du score du joueur
                 joueur1.score+=jeu.score
                 iScoreJoueur1.config(text="Score Joueur 1: "+str(joueur1.score))
                 
                 #mise a jour du tableau
                 if(jeu.premier==False): #Pour savoir si il est le premier a jouer ou pas
                      #mise a jour du tableau
                      jeu.updateTab(int(coords[0]/50),int((coords[3]-50)/50),pion_selectionne.name)
                      #for i in range(len(jeu.tableau)):
                           #print(jeu.tableau[i])

                 else:
                      jeu.premier==False
                      jeu.updateTab(7,6,pion_selectionne.name)
                      #Definition des cases ou l'on peut deposer des pieces
                      jeu.tableau[6][7-1]="place"
                      jeu.tableau[6][7+1]="place"
                      jeu.tableau[6-1][7]="place"
                      #for i in range(len(jeu.tableau)):
                           #print(jeu.tableau[i])
               
                 #pion=PhotoImage(file="pions/"+pion_selectionne.name+".png")

                 #Poser la piece sur le plateau
                 pion_selectionne.chargeImage(pion_selectionne.name)
                 img=c.create_image(centerX+2.5,centerY-5.5,image=pion_selectionne.image,state="disable",anchor="center")
                       
                 
          
                 #retirer l'image de la liste d'image
                 list_images_pions.pop(list_de_mes_pions.index(pion_selectionne.name)) 
                 list_de_mes_pions.remove(pion_selectionne.name)
                 
                 print(pion_selectionne.name)
                 pion_selectionne.setName("aucun")
                 iPionSelectionne.config(text="Pion Selectionné: aucun") #Pour mettre le nom du Pion
                 
                 c.delete("inverse")
                 gamePlate(800,500)
                 c1.delete("all")

                 mesPions(225,300,list_de_mes_pions,list_images_pions,c1,jeu.joueur_courant)
                 
                 #Mise à jour du joueur courant
                 jeu.changeJoueur()
                 
                 gagnant()
                 IA()

     else:
        #Message d'erreur
        iErreur.config(text="Vous ne pouvez pas placer le pion ici ou Vous n'avez pas sectionné de pion")

          


#========================================================================================================
#FONCTION VERIFIANT SI LE JEUX EST TERMINE 
     
def gagnant():
     if(len(list_de_mes_pions)==0 or joueur1.score>=400 ):

          jeu.joueur_courant=""
          
          #Si le joueur pose toutes ses pieces
          if(len(list_de_mes_pions)==0):
              joueur1.score+=25
              for i in range(len(list_de_mes_pions2)):
                  if(list_de_mes_pions2[i][0]!="x"):
                      joueur1.score+=int(list_de_mes_pions2[i][0])+int(list_de_mes_pions2[i][2])+int(list_de_mes_pions2[i][4])
                  else:
                      joueur1.score+=int(list_de_mes_pions2[i][1])+int(list_de_mes_pions2[i][3])+int(list_de_mes_pions2[i][5])
                      
          iScoreJoueur1.config(text="Score Joueur 1: "+str(joueur1.score))
                      

                      
          if(joueur1.score>joueur2.score):
               c.delete("all")
               winner=Label(c,text="Fin de la partie - Le Joueur 1 à gagné",fg="black",bg="red",font="Verdana 20 bold")
               winner.pack(padx=2)
               
          elif(joueur1.score<joueur2.score):
               c.delete("all")
               winner=Label(c,text="Fin de la partie - L'IA à gagné",fg="black",bg="red",font="Verdana 20 bold")
               winner.pack(padx=2)
               
          else:
               c.delete("all")
               winner=Label(c,text="Fin de la partie - Vous etes à égalité",fg="black",bg="red",font="Verdana 20 bold")
               winner.pack(padx=2)

     elif(len(list_de_mes_pions2)==0 or joueur2.score>=400 ):

          jeu.joueur_courant=""
         
          #Si le joeur pose toutes ses pieces
          if(len(list_de_mes_pions2)==0):
              joueur2.score+=25
              for i in range(len(list_de_mes_pions)):
                  if(list_de_mes_pions[i][0]!="x"):
                      joueur2.score+=int(list_de_mes_pions[i][0])+int(list_de_mes_pions[i][2])+int(list_de_mes_pions[i][4])
                  else:
                      joueur2.score+=int(list_de_mes_pions[i][1])+int(list_de_mes_pions[i][3])+int(list_de_mes_pions[i][5])

          iScoreJoueur2.config(text="Score IA: "+str(joueur2.score))
                      
          if(joueur1.score>joueur2.score):
               c.delete("all")
               winner=Label(c,text="Fin de la partie - Le Joueur 1 à gagné",fg="black",bg="red",font="Verdana 20 bold")
               winner.pack(padx=2)
               
          elif(joueur1.score<joueur2.score):
               c.delete("all")
               winner=Label(c,text="Fin de la partie - L'IA à gagné",fg="black",bg="red",font="Verdana 20 bold")
               winner.pack(padx=2)
               
          else:
               c.delete("all")
               winner=Label(c,text="Fin de la partie - Vous etes à égalité",fg="black",bg="red",font="Verdana 20 bold")
               winner.pack(padx=2)
          




#=======================================================================================================
#CREATION DU PLATEAU 

#Creation des triangles

def trianglesBlock(posx,posy):
    
    A= [0+posx,50+posy, 50+posx,0+posy, 100+posx,50+posy]
    B= [0+posx,50+posy, 50+posx,100+posy, 100+posx,50+posy]
    C= [50+posx,100+posy, 100+posx,50+posy, 150+posx,100+posy]
    D= [50+posx,0+posy, 100+posx,50+posy, 150+posx,0+posy]
    t=c.create_polygon(A,fill="",outline="black",tags="normal")
    
    t1=c.create_polygon(B,fill="",outline="black",tags="inverse")
    t2=c.create_polygon(C,fill="",outline="black",tags="normal")
    t3=c.create_polygon(D,fill="",outline="black",tags="inverse")
    #c.create_image(posx-1,posy-10,image=pion,state="disabled",anchor="nw")
    #c.create_image(posx-51,posy-10,image=pion,state="disabled",anchor="nw")
    c.tag_bind("normal","<Button-1>", callback)
    c.tag_bind("inverse","<Button-1>", callback2)

    

#Creation du plateau
    
def gamePlate(width,height):
    nbColumns=width//100
    nbRows=height//100
    posx,posy=0,0

    for i in range(nbRows):
        for j in range(nbColumns):
            trianglesBlock(posx,posy)
            
            posx+=100
            
        posy+=100
        posx=0

#=======================================================================================================
#CREATION DES PIONS DE CHAQUE JOUEURS

#Creation des triangles
        
def rectangleBlock(posx,posy,nom_pion,image,plateau_joueur,joueur):
    #pour verifier quel plateau j1 ou j2
    joueur=joueur
    def selection_pion(nom_pion):
         #pion=PhotoImage(file="pions/"+nom_pion+".png")
         if (jeu.joueur_courant==joueur):
             
             iErreur.config(text="")#Pour supprimer le message d'erreur
             iPionSelectionne.config(text="Pion Selectionné: "+nom_pion)
             pion_selectionne.setName(nom_pion)
         
    def rotation_pion(nom_pion):
         if(pion_selectionne.name != "aucun" and jeu.joueur_courant=="Joueur 1" and jeu.joueur_courant==joueur and jeu.premier==False):
              
              iErreur.config(text="")#Pour supprimer le message d'erreur
              #print(list_de_mes_pions)
              position_ancien_pion=list_de_mes_pions.index(nom_pion)
              pion_selectionne.Rotate(nom_pion)
              list_de_mes_pions[position_ancien_pion]=pion_selectionne.name
              #charger l'image
              pion_selectionne.chargeImage(pion_selectionne.name)
              list_images_pions[position_ancien_pion]=pion_selectionne.image
              #On met a jour les infos
              iPionSelectionne.config(text="Pion Selectionné: "+pion_selectionne.name)
              
              #print(list_de_mes_pions)
              plateau_joueur.delete("all")
              mesPions(225,300,list_de_mes_pions,list_images_pions,plateau_joueur,joueur)
              
    

    #pour ne pas duppliquer le dernier pion         
    if (nom_pion != "aucun"):
        if nom_pion[0] != "x":
            plateau_joueur.create_image(posx-12,posy+2.5,image=image,state="disabled",anchor="nw")
        else:
            plateau_joueur.create_image(posx-12,posy-12,image=image,state="disabled",anchor="nw")
        
    A=[0+posx,0+posy,75+posx,0+posy,75+posx,75+posy,0+posx,75+posy]
    t1=plateau_joueur.create_polygon(A,fill="",outline="black",tags="p"+nom_pion)
    plateau_joueur.tag_bind("p"+nom_pion,"<Button-1>", lambda event:selection_pion(nom_pion))
    plateau_joueur.tag_bind("p"+nom_pion,"<Double-Button-1>", lambda event:rotation_pion(nom_pion))
    
    
    
#Creations des banques de pieces des joueurs    

def mesPions(width,height,list_de_mes_pions,list_images_pions,plateau_joueur,joueur):
    image=""
    nbColumns=width//75
    nbRows=height//75
    posx,posy=0,0
    nb_pions=0
    
    for i in range(nbRows):
              
        for j in range(nbColumns):
            #me permet d'attribuer un pion a chaque case creer qui me servira a choisir l'image correspondant
            if (nb_pions < len(list_de_mes_pions)):
              nom_pion=list_de_mes_pions[nb_pions]
              image=list_images_pions[nb_pions]
            else:
              nom_pion="aucun"
              
            rectangleBlock(posx,posy,nom_pion,image,plateau_joueur,joueur)
            posx+=75
            nb_pions+=1
            

            
        posy+=75
        posx=0


        
#================================================================================================================================
#################################################################################################################################
#################################################################################################################################
#################################################################################################################################
#================================================================================================================================



#PROGRAMME MAIN

#Creation de la fenetre
root = Tk()
root.title("Jeu Triominos")
root.attributes("-fullscreen",True)
root.configure(bg="bisque4")
width,height=800,500


#Creation du plateau
plateau=canvas=Canvas(root,width=width+50,height=height+1000,bg="bisque4")
plateau.pack(side=LEFT,padx=70)

info=canvas= Canvas(plateau,width=500,height=150,bg="black")
info.pack(side=TOP,pady=10)


#les textes et canevas informatifs (Sccore etc) //////////

iTuto=Label(info,text="(Clic gauche sur le trioninos pour sectionner - Double clic pour faire une rotation - Pas de rotation au debut du jeu)",fg="white",bg="black",font="Verdana 10 bold")
iTuto.pack(padx=2)
iTitre=Label(info,text="Jeu Triominos (Joueur 1 = Jaune - IA = Vert)",fg="white",bg="black",font="Verdana 10 bold")
iTitre.pack()
iJoueurCourant=Label(info,text="Joueur Courant: Joueur 1",fg="yellow",bg="black",font="Verdana 10 bold")
iJoueurCourant.pack()
iScoreJoueur1=Label(info,text="Score Joueur 1: 0",fg="yellow",bg="black",font="Verdana 10 bold")
iScoreJoueur1.pack()
iScoreJoueur2=Label(info,text="Score IA: 0",fg="green",bg="black",font="Verdana 10 bold")
iScoreJoueur2.pack()
iPionSelectionne=Label(info,text="Pion Selectionné: aucun",fg="white",bg="black",font="Verdana 10 bold")
iPionSelectionne.pack()
iErreur=Label(info,text="",fg="red",bg="black",font="Verdana 10 bold")
iErreur.pack(pady=2)


#Creation du plateau ou sera posé les pions /////////////////////////////////
c=canvas= Canvas(plateau,width=width+50,height=height,bg="blue")
c.pack(side=BOTTOM)
gamePlate(width,height) #Creation du plateau de jeu


banque=canvas= Canvas(root,bg="bisque4")
banque.pack(side=RIGHT,pady=10,padx=60)


#canevas joueur 1 /////////////////////
c1=canvas= Canvas(banque,width=225,height=300,bg="yellow")
c1.pack()


#Canvas des bouttons ////////////////////
c3=canvas= Canvas(banque,width=225,height=100,bg="black")
c3.pack()
#le boutton piocher
b1=Button(c3,text="Piocher",command=piocher).pack(side=LEFT,padx=7,pady=10)
#le boutton quitter
b3=Button(c3,text="Quitter",command=quitter).pack(side=RIGHT,padx=7,pady=10)
#le boutton recommencer
b2=Button(c3,text="Recommencer",command=recommencer).pack(side=RIGHT,padx=7,pady=10)



#Variable enregistrant le pion selectionné - aucun est enregistré quand rien n'est selectionné 
pion_selectionne=Pion.Pion("aucun")



#Creation du jeu non visuel (Avec un tableau a 1 demension enregistrant les diffrents coups des joueurs) /////////////////
jeu=Game.Game(width,height)

#Affichage du tabeau
#for i in range(len(jeu.tableau)):
     #print(jeu.tableau[i])


#Pioche et liste contenats tous les pions permettant aux joeurs de jouer //////////////////
     
liste_des_pions=["0x0x0x","1x1x1x","2x2x2x","3x3x3x","4x4x4x","5x5x5x","0x0x1x","1x1x2x","2x2x3x","3x3x4x",
                 "4x4x5x","0x0x2x","1x1x3x","2x2x4x","3x3x5x","4x5x5x","0x0x3x","1x1x4x","2x2x5x","3x4x4x",
                 "0x0x4x","1x1x5x","2x3x3x","3x4x5x","0x0x5x","1x2x2x","2x3x4x","3x5x5x","0x1x1x","1x2x3x",
                 "2x3x5x","0x1x2x","1x2x4x","2x4x4x","0x1x3x","1x2x5x","2x4x5x","0x1x4x","1x3x3x","2x5x5x",
                 "0x1x5x","1x3x4x","0x2x2x","1x3x5x","0x2x3x","1x4x4x","0x2x4x","1x4x5x","0x2x5x","1x5x5x",
                 "0x3x3x","0x3x4x","0x3x5x","0x4x4x","0x4x5x","0x5x5x"]





#AU DEBUT DU JEU ////////////////#####################################################

joueur1=Player.Player(liste_des_pions) #Initialisation du joueur 1
joueur2=Player.Player(liste_des_pions) #Initialisation de l'IA

#elements du joueur1 =========================================================================

list_de_mes_pions=joueur1.pions
list_images_pions=[]

for i in range(len(list_de_mes_pions)):
     #list_images_pions.append(PhotoImage(file="pions/"+list_de_mes_pions[i]+".png").subsample(2))
     list_images_pions.append(PhotoImage(file="pions/"+list_de_mes_pions[i]+".png"))

mesPions(225,300,list_de_mes_pions,list_images_pions,c1,"Joueur 1")

#elements de l'IA =========================================================================

list_de_mes_pions2=joueur2.pions
list_images_pions2=[]



root.mainloop()



          


