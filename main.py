import pygame
pygame.init()
screen = pygame.display.set_mode((640,480))
launched = True

# --- Charger l'image ---
# image = pygame.image.load("schtroumpfette.png")    # Nom exact de ton fichier
# image = pygame.transform.scale(image, (200, 200))  # (OPTIONNEL) redimensionner

x = 280        # position de départ
y = 200      # hauteur du cercle
speed = 3    # vitesse

while launched:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            launched = False
    
    screen.fill((20, 20, 20)) # Couleur de fond

     # --- Dessiner un cercle ---
    # pygame.draw.circle(surface, couleur(R,G,B), position(x,y), rayon, épaisseur)
    pygame.draw.circle(screen, (0, 200, 255), (x, y), 40)  # cercle plein

 # --- Dessiner un rectangle ---
    # pygame.draw.rect(surface, couleur, (x, y, largeur, hauteur), épaisseur)
    # pygame.draw.rect(screen, (255, 100, 0), (200, 50, 150, 80))  # rectangle

    # --- Dessiner un triangle ---
    # pygame.draw.polygon(surface, couleur, [(x1,y1), (x2,y2), (x3,y3)], épaisseur)
    # pygame.draw.polygon(screen, (0, 255, 100), [(400, 150), (500, 50), (550, 150)])  # triangle

    # --- Afficher l'image ---
    # screen.blit(image, (200, 150))  # position (x, y)

     # --- Animation : mouvement ---
    x += speed

    # Rebond sur les bords
    if x > 640 - 40 or x < 40:
        speed = -speed

    pygame.display.update()  # Met a jour l'ecran
    pygame.time.delay(50)  # ralentit un peu pour voir l'animation