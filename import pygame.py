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

# Initialiser Pygame
pygame.init()

# Définir la taille de la fenêtre
screen_width = 800
screen_height = 600

#Savoir le nombre d'écran
num_screens = pygame.display.get_num_displays()

# Choisir l'écran cible (index 1 dans cet exemple)
screen = pygame.display.set_mode((screen_width, screen_height), 0, display=0)

# ...
