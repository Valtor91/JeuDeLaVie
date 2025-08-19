import customtkinter
import sys


customtkinter.set_appearance_mode("dark")  # "light" ou "dark"
customtkinter.set_default_color_theme("blue")  # "blue", "green", "dark-blue"

largeur, hauteur = 900, 600
app = customtkinter.CTk()
app.geometry(f"{largeur}x{hauteur}")
app.title("Jeu de la Vie — Cellules en action")

blanc = (255, 255, 255)
noir = (0, 0, 0)

intervale = 10
celluleAffiche = {}
cellule = []
vosine = 0


A = [
  (-10,-10),
  (00,-10),
  (10,-10),
  (-10,0),
  (10,0),
  (-10,10),
  (0,10),
  (10,10),
]

frame_gauche = customtkinter.CTkFrame(app, width=10)

frame_gauche.pack(side="bottom", pady=20)


canvas = customtkinter.CTkCanvas(app, width=700, height=hauteur, bg="white", highlightthickness=0)
canvas.pack(pady=0, padx=(0, 0))




def grille():
    for x in range(0,hauteur,intervale):
        for y in range(0, 700, intervale):
            canvas.create_line(0, x, largeur, x, fill="black", width=1)
            canvas.create_line(y, 0, y,largeur , fill="black", width=1)

def clic(event):
    x = event.x
    y = event.y




    cellu_x = (x // intervale) * intervale
    cellu_y = (y // intervale) * intervale

    if (cellu_x,cellu_y) in celluleAffiche:
        celluleAffiche.pop((cellu_x,cellu_y), None)
    else:


        celluleAffiche[(cellu_x, cellu_y)] = True


#
#
def InLife():
    global vosine
    CellASuprimer = []
    vosinePotentiel = {}
    for i in celluleAffiche:

        vosine = 0
        for g in A:

            if (i[0]+g[0],i[1]+g[1]) in celluleAffiche:
                vosine +=1
        if vosine < 2 or vosine > 3:
            CellASuprimer.append(i)



    for i in celluleAffiche:
        for g in A:
            voisin = (i[0] + g[0], i[1] + g[1])
            if voisin not in celluleAffiche:
                vosinePotentiel[voisin] = vosinePotentiel.get(voisin, 0) + 1

    for f in vosinePotentiel.items():
        if f[1] == 3:
            celluleAffiche[f[0]] = True

    for c in CellASuprimer:
        celluleAffiche.pop(c, None)

#
#

bouton = customtkinter.CTkButton(frame_gauche, text="       ▶️", command=InLife)

bouton.pack(side="bottom", pady=20)
label = customtkinter.CTkLabel(frame_gauche, text=f"cellule: {len(celluleAffiche)}", font=("Arial", 18))
label.pack(pady=0)
grille()

def boucle():
    canvas.delete("cellule")
    canvas.bind("<Button-1>", clic)

    for (x, y) in celluleAffiche:
        canvas.create_rectangle(x, y, x+intervale, y+intervale, fill="red", outline="black", width=2,tags="cellule")

    label.configure(text=f"cellule: {len(celluleAffiche)}")


    app.after(20, boucle)





boucle()
app.mainloop()
