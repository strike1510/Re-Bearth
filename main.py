'''
■■■                    ■■■■
▋  ▋   ■■■           ▋   ▋   ■■■     ■■■■    ▋  ■■    ▋    ▋
▋■■    ▋   ▋        ▋   ▋  ▋   ▋       ▋  ▋▋  ▋  ■■■■  ▋
▋■■     ■■■■    ■■■■  ■■■■     ■■■■     ■■■■    ▋        ▋    ▋■■■
▋  ▋  ▋             ▋   ▋  ▋       ▋   ▋  ▋        ▋    ▋  ▋
▋  ▋   ■■■■          ■■■■      ■■■■    ■■■■■   ▋         ▋   ▋  ▋
'''

# Bibliothèques :
import pygame
import menu.menu
import menu.pause
import jeu.fonction
import jeu.game
import jeu.room1,jeu.room2,jeu.room3,jeu.room4,jeu.room5, jeu.room6, jeu.room7


from pygame.locals import *

# Ecran :
pygame.init()
screen = pygame.display.set_mode((0, 0), FULLSCREEN)
pygame.display.set_caption("Re-Bearth")
icone = pygame.image.load("menu\\image\\icone.png")
pygame.display.set_icon(icone)


pygame.mixer.init()


# Variables :
screen_info = pygame.display.Info()
LARGEUR = screen_info.current_w
HAUTEUR = screen_info.current_h
VITESSE = 8

# Code :

test = menu.menu.GrandMenu(screen, HAUTEUR, LARGEUR)

#test de zone en récupérant ID de zone par texte dans doc ( "ID de Zone:" )
#puis il y aura l'ID de la zone et les coo en x et y

with open('donnee\\sauvegarde.txt', 'r') as file:
    stocke = []
    for line in file:
        stocke.append(line.replace("\n",""))

for i in range(len(stocke)):
    if stocke[i] == "ID de Zone:":
        ZONE_ID = stocke[i+1].split(";")

if test:
    pygame.mixer.music.load("jeu\\sons\\jeu33.mp3")
    pygame.mixer.music.play(-1)
    if ZONE_ID[0] == "-1":
        jeu.room1.Jeuroom1(screen, 1100*LARGEUR/1920, 485*HAUTEUR/1080, VITESSE, HAUTEUR, LARGEUR)
    elif ZONE_ID[0] == "0":
        jeu.room1.Jeuroom1(screen, int(ZONE_ID[1]), int(ZONE_ID[2]), VITESSE, HAUTEUR, LARGEUR)
    elif ZONE_ID[0] == "1":
        jeu.game.LancementJeu(screen, int(ZONE_ID[1]), int(ZONE_ID[2]), VITESSE, HAUTEUR, LARGEUR)
    elif ZONE_ID[0] == "2":
        jeu.room2.Jeuroom2(screen, int(ZONE_ID[1]), int(ZONE_ID[2]), VITESSE, HAUTEUR, LARGEUR)
    elif ZONE_ID[0] == "3":
        jeu.room3.Jeuroom3(screen, int(ZONE_ID[1]), int(ZONE_ID[2]), VITESSE, HAUTEUR, LARGEUR)
    elif ZONE_ID[0] == "4":
        jeu.room4.Jeuroom4(screen, int(ZONE_ID[1]), int(ZONE_ID[2]), VITESSE, HAUTEUR, LARGEUR)
    elif ZONE_ID[0] == "5":
        jeu.room5.Jeuroom5(screen, int(ZONE_ID[1]), int(ZONE_ID[2]), VITESSE, HAUTEUR, LARGEUR)
    elif ZONE_ID[0] == "6":
        jeu.room6.Jeuroom6(screen, int(ZONE_ID[1]), int(ZONE_ID[2]), VITESSE, HAUTEUR, LARGEUR)
    elif ZONE_ID[0] == "7":
        jeu.room7.Jeuroom7(screen, int(ZONE_ID[1]), int(ZONE_ID[2]), VITESSE, HAUTEUR, LARGEUR)
    elif ZONE_ID[0] == "8":
        jeu.room8.Jeuroom8(screen, int(ZONE_ID[1]), int(ZONE_ID[2]), VITESSE, HAUTEUR, LARGEUR)

pygame.quit()