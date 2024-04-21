'''
with open('donnee\\sauvegarde.txt', 'r') as file:
    stocke = []
    for line in file:
        stocke.append(line.replace("\n",""))

print(stocke[0])

with open('donnee\\sauvegarde.txt', 'w') as file:
    for i in range (len(stocke)):
        file.write(stocke[i])


with open('donnee\\sauvegarde.txt', 'w') as file:
    file.write("Pseudo:\n")
    file.write("\n")
    file.write("LvL:\n")
    file.write("\n")
    file.write("Money:")
    file.write("\n")

    

pygame.mixer.init()

# Charger les fichiers audio
son1 = pygame.mixer.Sound('son1.wav')
son2 = pygame.mixer.Sound('son2.wav')

# Jouer les deux sons simultanément
son1.play()
son2.play()

import pygame
import os

pygame.init()

# Définition de la taille de la fenêtre
largeur = 800
hauteur = 600
taille_fenetre = (largeur, hauteur)

# Création de la fenêtre
fenetre = pygame.display.set_mode(taille_fenetre)

# icône
chemin_icone = os.path.join("menu", "image", "icone.ico")  
icone = pygame.image.load(chemin_icone)
pygame.display.set_icon(icone)


en_cours = True
while en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False


pygame.quit()
'''
import pygame

# Initialisation de Pygame
pygame.init()

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Initialisation de la fenêtre
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Bouton avec texte")

# Initialisation de la police
font = pygame.font.Font(None, 36)

# Texte initial
text_value = "Cliquez ici"

# Position et taille du bouton
button_rect = pygame.Rect(100, 100, 200, 50)

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                # Changer la valeur du texte lors du clic
                text_value = "Nouvelle valeur"

    # Affichage du bouton
    screen.fill(WHITE)
    pygame.draw.rect(screen, GRAY, button_rect)
    text = font.render(text_value, True, BLACK)
    text_rect = text.get_rect(center=button_rect.center)
    screen.blit(text, text_rect)

    pygame.display.flip()

pygame.quit()