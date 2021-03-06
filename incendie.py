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
import random as rd

################################################
# constantes
HAUTEUR = 400
LARGEUR = 400


COULEUR_FOND = "red"
COTE = 100
COULEUR_QUADR = "grey20"

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

def xy_to_cl(x, y):
    """Retourne la colonne et la ligne correspondant au point du canevas de coordonnées (x,y)"""
    pass


def change_carre(event):
    """Change la couleur du carre à la position (event.x, event.y)"""
    pass

################################################
# programme principale

racine = tk.Tk()
racine.title("Incendie")

# création des widgets
boutton_TERRAIN = tk.Button(racine, text = "TERRAIN", bg="grey", fg="blue", font=("Times", "20"))
canvas = tk.Canvas(racine, width = HAUTEUR, height = LARGEUR, bg = COULEUR_FOND)

# placement des widgets
canvas.grid(row=0)
boutton_TERRAIN.grid(row=1)
quadrillage()

# liaison des événements
canvas.bind("<Button-1>", change_carre)


racine.mainloop()

