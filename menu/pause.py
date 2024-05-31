import pygame, sys, time, menu.options, jeu.fonction
WHITE = (255, 255, 255)
TRANSPARENT = (255, 255, 255, 20)
BLACK = (0, 0, 0)

def Pause(zone,posx,posy,screen,HAUTEUR,LARGEUR):
    pause = True
    test = False

    PauseFond = pygame.Surface((LARGEUR, HAUTEUR), pygame.SRCALPHA)
    PauseFond.fill(TRANSPARENT)
    imagePauseFond = jeu.fonction.redimensionner_image('menu\\image\\pause.png', LARGEUR, HAUTEUR)
    imagepausesaved = jeu.fonction.redimensionner_image('menu\\image\\pauses.png', LARGEUR, HAUTEUR)

    pygame.mixer.music.pause()
    while pause == True:
        pygame.display.flip()
        key = pygame.key.get_pressed()
        pygame.draw.rect(PauseFond, (0, 0, 255), PauseFond.get_rect(), 3) 
        screen.blit(imagePauseFond, (0,0))
        if key[pygame.K_ESCAPE] == True:
            if test == True:
                pause = False
                pygame.mixer.music.unpause()
                return True
        else:
            test = True
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if 795*LARGEUR/1920 <= x <= 1125*LARGEUR/1920 and 680*HAUTEUR/1080 <= y <= 780*HAUTEUR/1080:
                        return False
                    elif 795*LARGEUR/1920 <= x <= 1125*LARGEUR/1920 and 550*HAUTEUR/1080 <= y <= 650*HAUTEUR/1080:
                        pause = False
                        pygame.mixer.music.unpause()
                        menu.options.parametre(screen,HAUTEUR,LARGEUR)
                        return True
                    elif 793*LARGEUR/1920 <= x <= 1125*LARGEUR/1920 and 298*HAUTEUR/1080 <= y <= 398*HAUTEUR/1080:
                        pause = False
                        pygame.mixer.music.unpause()
                        return True
                    elif 795*LARGEUR/1920 <= x <= 1125*LARGEUR/1920 and 425*HAUTEUR/1080 <= y <= 525*HAUTEUR/1080:
                        imagePauseFond = imagepausesaved
                        jeu.fonction.save(zone,posx,posy,"0:0:0:0:0")
                        