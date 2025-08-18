import pygame
import sys

# Initialisation
pygame.init()

# Taille de la fenêtre
largeur, hauteur = 800, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Dessiner une ligne")

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)
fenetre.fill(blanc)
intervale = 20
celluleAffiche = {}
cellule = []
vosine = 0


A = [
  (-20,-20),
  (00,-20),
  (20,-20),
  (-20,0),
  (20,0),
  (-20,20),
  (0,20),
  (20,20),
]
vie = False


def grille():
    for x in range(0,hauteur,intervale):
        for y in range(0, largeur, intervale):
            pygame.draw.line(fenetre, noir, (0, x), (largeur, x), 2)

            pygame.draw.line(fenetre, noir, (y,0), (y, hauteur), 2)

def clic():
    if event.type == pygame.MOUSEBUTTONDOWN:
        position = pygame.mouse.get_pos()

        cellu_x = (position[0] // intervale) * intervale
        cellu_y = (position[1] // intervale) * intervale

        celluleAffiche[(cellu_x, cellu_y)] = True
        cellule.append((cellu_x, cellu_y))


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



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:


                InLife()


    fenetre.fill(blanc)
    for (x, y) in celluleAffiche:
        pygame.draw.rect(fenetre, (255, 0, 0), pygame.Rect(x, y, intervale, intervale))

    grille()
    clic()




    # Mettre à jour l'affichage
    pygame.display.flip()
