'''
■■■                    ■■■■
▋  ▋   ■■■           ▋   ▋   ■■■     ■■■■    ▋  ■■    ▋    ▋
▋■■    ▋   ▋        ▋   ▋  ▋   ▋       ▋  ▋▋  ▋  ■■■■  ▋
▋■■     ■■■■    ■■■■  ■■■■     ■■■■     ■■■■    ▋        ▋    ▋■■■
▋  ▋  ▋             ▋   ▋  ▋       ▋   ▋  ▋        ▋    ▋  ▋
▋  ▋   ■■■■          ■■■■      ■■■■    ■■■■■   ▋         ▋   ▋  ▋
'''

#Bibliothèque :#

import pygame, menu.menu, menu.pause , jeu.game , jeu.room1

#Variables:
LONGUEUR = 1920
LARGEUR = 1080

#Code :#
pygame.init()
screen = pygame.display.set_mode((LONGUEUR, LARGEUR))
pygame.display.set_caption("Re-Bearth")

test = menu.menu.GrandMenu(screen)

if test == True:
    jeu.game.LancementJeu(screen,LONGUEUR // 2, LARGEUR // 2)
    

pygame.quit()
