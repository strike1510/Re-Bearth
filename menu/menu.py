import pygame, menu.options

def GrandMenu(screen, HAUTEUR, LARGEUR):

    background = pygame.transform.scale(pygame.image.load("menu\\image\\bg.jpg"), (LARGEUR, HAUTEUR))

    #Bouton:

    bg_but_play = [pygame.transform.scale(pygame.image.load(f"menu\\image\\bouton_jouer1.png"), (LARGEUR, HAUTEUR)),pygame.transform.scale(pygame.image.load(f"menu\\image\\bouton_jouer2.png"), (LARGEUR, HAUTEUR))]
    bg_but_quit = [pygame.transform.scale(pygame.image.load(f"menu\\image\\bouton_quitter1.png"), (LARGEUR, HAUTEUR)),pygame.transform.scale(pygame.image.load(f"menu\\image\\bouton_quitter2.png"), (LARGEUR, HAUTEUR))]
    bg_but_option = pygame.transform.scale(pygame.image.load(f"menu\\image\\option_menu.png"), (LARGEUR, HAUTEUR))

    pygame.mixer.music.load("menu\\sons\\menu1.mp3")
    pygame.mixer.music.play(-1)

    running = True
    index_play = 0
    index_quit = 0
    while running:
        screen.blit(background, (0, 0))
        screen.blit(bg_but_play[index_play], (0, 0))
        screen.blit(bg_but_quit[index_quit], (0, 0))
        screen.blit(bg_but_option, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            x, y = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if 810*LARGEUR/1920 <= x <= 1110*LARGEUR/1920 and 660*HAUTEUR/1080 <= y <= 800*HAUTEUR/1080:
                    pygame.mixer.music.stop()
                    running = False
                    return True
                if 810*LARGEUR/1920 <= x <= 1110*LARGEUR/1920 and 835*HAUTEUR/1080 <= y <= 970*HAUTEUR/1080:
                    running = False
                    return False
                if 1815*LARGEUR/1920 <= x <= 1895*LARGEUR/1920 and 25*HAUTEUR/1080 <= y <= 100*HAUTEUR/1080:
                    menu.options.parametre(screen,HAUTEUR,LARGEUR)
                    screen.blit(background, (0, 0))
                    screen.blit(bg_but_play[index_play], (0, 0))
                    screen.blit(bg_but_quit[index_quit], (0, 0))
                    screen.blit(bg_but_option, (0, 0))
            if 810*LARGEUR/1920 <= x <= 1110*LARGEUR/1920 and 660*HAUTEUR/1080 <= y <= 800*HAUTEUR/1080:
                index_play = 1
            else:
                index_play = 0
            if 810*LARGEUR/1920 <= x <= 1110*LARGEUR/1920 and 835*HAUTEUR/1080 <= y <= 970*HAUTEUR/1080:
                index_quit = 1
            else:
                index_quit = 0
        
        pygame.display.flip()
