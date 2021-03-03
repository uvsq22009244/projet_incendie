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


################################################
# constantes
HAUTEUR = 400
LARGEUR = 400
COULEUR_FOND = "red"


################################################
# variables globales


################################################
# fonctions


################################################
# programme principale

racine = tk.Tk()
racine.title("Incendie")

# création des widgets
canvas = tk.Canvas(racine, width = HAUTEUR, height = LARGEUR, bg = COULEUR_FOND)

# placement des widgets
canvas.grid(row=0)

# liaison des événements

racine.mainloop()
