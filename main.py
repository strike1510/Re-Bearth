'''
■■■                    ■■■■
▋  ▋   ■■■           ▋   ▋   ■■■     ■■■■    ▋  ■■    ▋    ▋
▋■■    ▋   ▋        ▋   ▋  ▋   ▋       ▋  ▋▋  ▋  ■■■■  ▋
▋■■     ■■■■    ■■■■  ■■■■     ■■■■     ■■■■    ▋        ▋    ▋■■■
▋  ▋  ▋             ▋   ▋  ▋       ▋   ▋  ▋        ▋    ▋  ▋
▋  ▋   ■■■■          ■■■■      ■■■■    ■■■■■   ▋         ▋   ▋  ▋
'''

#Bibliothèque :#

import pygame, menu.menu, jeu.game

#Code :#
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Re-Bearth")

test = menu.menu.GrandMenu(screen)

if test == True:
    jeu.game.LancementJeu(screen)

pygame.quit()
