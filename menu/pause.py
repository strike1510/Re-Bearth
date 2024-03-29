import pygame, sys, time, menu.options
WHITE = (255, 255, 255)
TRANSPARENT = (255, 255, 255, 20)
BLACK = (0, 0, 0)

def Pause(screen,HAUTEUR,LARGEUR):
    pause = True
    test = False

    PauseFond = pygame.Surface((440*LARGEUR/1920, 540*HAUTEUR/1080), pygame.SRCALPHA)
    PauseFond.fill(TRANSPARENT)
    PauseFond_rect = PauseFond.get_rect(center=(960*LARGEUR/1920, 500*HAUTEUR/1080))
    imagePauseFond = pygame.image.load('menu\\image\\pause.png')
    image_PauseFond = pygame.transform.scale(imagePauseFond, (440*LARGEUR/1920, 540*HAUTEUR/1080))

    pygame.mixer.music.pause()

    def draw_text(text, font, color, surface, x, y):
        text_obj = font.render(text, True, color)
        text_rect = text_obj.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_obj, text_rect)
    while pause == True:
        pygame.display.flip()
        key = pygame.key.get_pressed()
        pygame.draw.rect(PauseFond, (0, 0, 255), PauseFond.get_rect(), 3) 
        screen.blit(image_PauseFond, PauseFond_rect)
        '''
        #   Quitter :
        pygame.draw.rect(screen, BLACK, (885, 610, 150, 50))
        draw_text("Quitter", pygame.font.Font(None, 36), WHITE, screen, 960, 635)

        # Options :
        pygame.draw.rect(screen, BLACK, (885, 510, 150, 50))
        draw_text("Options", pygame.font.Font(None, 36), WHITE, screen, 960, 535)

        # Sauvegarder :
        pygame.draw.rect(screen, BLACK, (880, 410, 160, 50))
        draw_text("Sauvegarder", pygame.font.Font(None, 36), WHITE, screen, 960, 435)

        # Continuer :
        pygame.draw.rect(screen, BLACK, (885, 310, 150, 50))
        draw_text("Continuer", pygame.font.Font(None, 36), WHITE, screen, 960, 335)
        '''
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
                    if 900*LARGEUR/1920 <= x <= 1020*LARGEUR/1920 and 610*HAUTEUR/1080 <= y <= 650*HAUTEUR/1080:
                        return False
                    if 900*LARGEUR/1920 <= x <= 1020*LARGEUR/1920 and 430*HAUTEUR/900 <= y <= 470*HAUTEUR/900:
                        pause = False
                        pygame.mixer.music.unpause()
                        menu.options.parametre(screen,HAUTEUR,LARGEUR)
                        return True
                    if 900*LARGEUR/1920 <= x <= 1020*LARGEUR/1920 and 350*HAUTEUR/1080 <= y <= 390*HAUTEUR/1080:
                        pause = False
                        pygame.mixer.music.unpause()
                        return True