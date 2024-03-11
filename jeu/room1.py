import pygame, sys , jeu.game , menu.pause
def Jeuroom1(screen,pos_player_x,pos_player_y):
    testpause = False
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    TRANSPARENT = (0, 0, 0, 0)
    background = pygame.image.load("jeu\\image\\room.jpg")

    #porte = pygame.Rect((500, 500, 64, 64))
    porte = pygame.Surface((64, 64), pygame.SRCALPHA)
    porte.fill(TRANSPARENT)
    porte_rect = porte.get_rect(center=(250, 1080 // 2))

    player = pygame.Surface((64, 64), pygame.SRCALPHA)
    player.fill(TRANSPARENT)
    player_rect = player.get_rect(center=(pos_player_x,pos_player_y))
    
    image = pygame.image.load('jeu\\image\\devant.png')
    image_porte_close = pygame.image.load('jeu\\image\\porte_close.png')
    image_porte_open = pygame.image.load('jeu\\image\\porte.png')
    image_porte = image_porte_close

    def draw_text(text, font, color, surface, x, y):
        text_obj = font.render(text, True, color)
        text_rect = text_obj.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_obj, text_rect)

    running = True
    while running:
        screen.blit(background, (0, 0))
        #pygame.draw.rect(screen, (255, 0, 0), player)
        pygame.draw.rect(porte, (0, 0, 255), porte.get_rect(), 3) 
        screen.blit(image_porte, porte_rect)
        pygame.draw.rect(player, (0, 0, 255), player.get_rect(), 3)  
        screen.blit(image, player_rect)

        key = pygame.key.get_pressed()

        if player_rect.x > 190:
            if player_rect.x < 235:
                if player_rect.y < 550:
                    if player_rect.y > 480:
                        image_porte = image_porte_open
                        if key[pygame.K_SPACE] == True:
                            running = False
                            jeu.game.LancementJeu(screen,1550,1080 // 2)
                    else:
                        image_porte = image_porte_close
                else:
                    image_porte = image_porte_close
            else:
                image_porte = image_porte_close
        else:
            image_porte = image_porte_close
        
        if key[pygame.K_q] == True:
            if player_rect.x > 190:
                player_rect.move_ip(-1, 0)
                image = pygame.image.load('jeu\\image\\gauche.png')
        if key[pygame.K_d] == True:
            if player_rect.x < 1680:
                player_rect.move_ip(1, 0)
                image = pygame.image.load('jeu\\image\\droite.png')
        if key[pygame.K_z] == True:
            if player_rect.y > 105:
                player_rect.move_ip(0, -1)
                image = pygame.image.load('jeu\\image\\derriere.png')
        if key[pygame.K_s] == True:
            if player_rect.y < 925:
                player_rect.move_ip(0, 1)
                image = pygame.image.load('jeu\\image\\devant.png')

        #   Code pour pause :
        if key[pygame.K_ESCAPE] == True:
            if testpause == False:
                testquit = menu.pause.Pause(screen)
                testpause = True
                if testquit == False:
                    running = False
        else:
            testpause = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        pygame.display.flip()
        pygame.display.update()