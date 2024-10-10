from tkinter import *
import os

#PROGRAMME PRINCIPAL LIGNE 27 ///////////////////////////////

#========================================================================================================
#FONCTION DU BOUTTON 1V1

def V1():
     root.destroy()
     os.system("Triominos.py")

#========================================================================================================
#FONCTION DU BOUTTON IA
     
def IA():
     root.destroy()
     os.system("Triominos_IA.py")

#========================================================================================================
#FONCTION DU BOUTTON FERMER
     
def fermer():
     root.destroy()
         

#PROGRAMME MAIN ///////////////////////////////

root = Tk()
root.title("Jeu Triominos")
root.attributes("-fullscreen",True)
root.configure(bg="DodgerBlue4")
root.geometry("650x250")
width,height=800,500


a=canvas= Canvas(root,width=970,height=300,bg="black")
a.pack(pady=110)

imag=PhotoImage(file="images/Accueil.png")
img=a.create_image(0,0,image=imag,anchor=NW)

c=canvas= Canvas(root,width=225,height=100,bg="black")
c.pack()

#le boutton piocher
b1=Button(c,text="Jouer en 1V1",command=V1).pack(side=LEFT,padx=7,pady=10)
#le boutton Fermer
b3=Button(c,text="Fermer",command=fermer).pack(side=RIGHT,padx=7,pady=10)
#le boutton recommencer
b2=Button(c,text="Jouer avec IA",command=IA).pack(side=RIGHT,padx=7,pady=10)



root.mainloop()
