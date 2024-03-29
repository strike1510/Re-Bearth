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
import jeu.room1


from pygame.locals import *

# Ecran :
pygame.init()
screen = pygame.display.set_mode((0, 0), FULLSCREEN)
pygame.display.set_caption("Re-Bearth")


# Variables :
screen_info = pygame.display.Info()
LARGEUR = screen_info.current_w
HAUTEUR = screen_info.current_h
VITESSE = 8

# Code :

test = menu.menu.GrandMenu(screen, HAUTEUR, LARGEUR)

if test:
    pygame.mixer.music.load("jeu\\sons\\jeu33.mp3")
    pygame.mixer.music.play(-1)
    jeu.game.LancementJeu(screen, LARGEUR/2, HAUTEUR/2, VITESSE, HAUTEUR, LARGEUR)

pygame.quit()