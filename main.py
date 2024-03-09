'''
■■■                    ■■■■
▋  ▋   ■■■           ▋   ▋   ■■■     ■■■■    ▋  ■■    ▋    ▋
▋■■    ▋   ▋        ▋   ▋  ▋   ▋       ▋  ▋▋  ▋  ■■■■  ▋
▋■■     ■■■■    ■■■■  ■■■■     ■■■■     ■■■■    ▋        ▋    ▋■■■
▋  ▋  ▋             ▋   ▋  ▋       ▋   ▋  ▋        ▋    ▋  ▋
▋  ▋   ■■■■          ■■■■      ■■■■    ■■■■■   ▋         ▋   ▋  ▋
'''

#Bibliothèque :#

import pygame, menu.menu, jeu.game , jeu.room1

#Variables:
LARGEUR = 1920
LONGUEUR = 1080

#Code :#
pygame.init()
screen = pygame.display.set_mode((LARGEUR, LONGUEUR))
pygame.display.set_caption("Re-Bearth")

test = menu.menu.GrandMenu(screen)

if test == True:
    jeu.game.LancementJeu(screen,LARGEUR // 2, LONGUEUR // 2)
    

pygame.quit()
