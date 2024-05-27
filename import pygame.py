import pygame

# Définir la résolution de référence
REFERENCE_WIDTH = 1600
REFERENCE_HEIGHT = 1024

# Initialiser Pygame
pygame.init()

# Créer la fenêtre avec la résolution de référence
screen = pygame.display.set_mode((REFERENCE_WIDTH, REFERENCE_HEIGHT))
pygame.display.set_caption("Jeu 2D")

# Récupérer la taille de la fenêtre
window_width, window_height = screen.get_size()

# Calculer le facteur d'échelle
scale_x = window_width / REFERENCE_WIDTH
scale_y = window_height / REFERENCE_HEIGHT

# Boucle principale du jeu
running = True
while running:
    # Gérer les événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Effacer l'écran
    screen.fill((0, 0, 0))

    # Dessiner les éléments du jeu en utilisant les coordonnées normalisées
    # et le facteur d'échelle pour les adapter à la taille de la fenêtre
    x = 0.25
    y = 0.5
    width = 0.1
    height = 0.2
    pygame.draw.rect(screen, (255, 0, 0),
                    (x * window_width, y * window_height,
                     width * window_width, height * window_height))

    # Mettre à jour l'affichage
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
