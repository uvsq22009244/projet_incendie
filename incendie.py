################################################

# Groupe 1 BI TD1
# Princesse MOMO
# Alexandra SCHMIDT
# Malak LALAMI
# Nolwenn CORIC
# Lilian JOANNET
# Tristan TOLENTINO
# https://github.com/uvsq22009244/projet_incendie

################################################
# import des modules

import tkinter as tk
import random 

################################################
# constantes
HAUTEUR = 400
LARGEUR = 400


COULEUR_FOND = "grey50"
COTE = 100
COULEUR_QUADR = "grey60"
COULEUR_EAU = "blue"
COULEUR_FORET = "green"
COULEUR_PRAIRIE = "yellow"
COULEUR_FEU = "red"

################################################
# variables globales


################################################
# fonctions

def quadrillage():
    """Dessine un quadrillage dans le canevas avec des carrés de côté COTE"""
    y = 0
    while y <= HAUTEUR:
        canvas.create_line((0, y), (LARGEUR, y), fill=COULEUR_QUADR)
        y += COTE
    i = 0
    while i * COTE <= LARGEUR:
        x = i * COTE
        canvas.create_line((x, 0), (x, HAUTEUR), fill=COULEUR_QUADR)
        i += 1

def remplire_carre(l,c,color):
    """On remplit le carrée de coordonée (x, y)"""
    y=l*COTE
    x=c*COTE
    for i in range(x, x+COTE):
        canvas.create_line(i, y, i, y+COTE,fill=color)

def xy_to_cl(x, y):
    """Retourne la colonne et la ligne correspondant au point du canevas de coordonnées (x,y)"""
    pass


def change_carre(event):
    """Change la couleur du carre à la position (event.x, event.y) où on a cliqué"""
    pass

################################################
# programme principale

racine = tk.Tk()
racine.title("Incendie")

# création des widgets
boutton_TERRAIN = tk.Button(racine, text = "TERRAIN", bg="grey", fg="blue", font=("Times", "20"), command =change_carre)
canvas = tk.Canvas(racine, width = HAUTEUR, height = LARGEUR, bg = COULEUR_FOND)
couleur_aleatoire =[COULEUR_EAU, COULEUR_FORET, COULEUR_PRAIRIE] #om met les couleurs des parcelles en liste
lin = int(LARGEUR//COTE) 
col = int(HAUTEUR//COTE)
for ligne in range(lin):
    for colonne in range(col):
        color = couleur_aleatoire[random.randint(0,2)]
        remplire_carre(ligne, colonne,color)
# placement des widgets
canvas.grid(row=0)
boutton_TERRAIN.grid(row=1)
quadrillage()

# liaison des événements
canvas.bind("<Button-1>", change_carre)


racine.mainloop()

