import jeu.game
import pygame, sys , jeu.game , menu.pause , math , jeu.fonction
def Jeuroom6(screen,pos_player_x,pos_player_y,VITESSE, HAUTEUR,LARGEUR):
    testpause = False
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    TRANSPARENT = (0, 0, 0, 0)
    dimmension_perso = 64
    
    background = pygame.image.load("jeu\\image\\room6\\map_05.png")
    colision_background = pygame.image.load("jeu\\image\\room6\\map_05col.png")
    imagesvagues = [pygame.image.load(f"jeu\\image\\room6\\map_05_V{i}.png") for i in range(1, 4)]
    clock = pygame.time.Clock()

    #TEST 
    rect_x = LARGEUR // 2
    rect_y = HAUTEUR // 2
    screen_x = 0
    screen_y = 0
    #background = pygame.image.load("jeu\\image\\background.jpg")
    background = pygame.transform.scale(background, (LARGEUR, HAUTEUR))
    largeur_cible, hauteur_cible = background.get_size()
    colision_background = pygame.transform.scale(colision_background, (largeur_cible, hauteur_cible))

    player = pygame.Surface((dimmension_perso, dimmension_perso), pygame.SRCALPHA)
    player.fill(TRANSPARENT)
    player_rect = player.get_rect(center=(pos_player_x,pos_player_y))

    #Image joueur :
    imagesbas = pygame.image.load("jeu\\image\\player\\devant.png")
    imageplayer = imagesbas
    

    def draw_text(text, font, color, surface, x, y):
        text_obj = font.render(text, True, color)
        text_rect = text_obj.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_obj, text_rect)

    running = True
    last = "z"
    index_image = 0
    index_vague_image = 0
    rep_image = 0
    
    while running:
        key = pygame.key.get_pressed()
            
        screen_x = rect_x - LARGEUR / 2
        screen_y = rect_y - HAUTEUR / 2
        screen.blit(background, (screen_x, screen_y))
        screen.blit(imagesvagues[index_vague_image], (screen_x, screen_y))
        pygame.draw.rect(player, (0, 0, 255), player.get_rect(), 3)  
        screen.blit(imageplayer, player_rect)
        
        #print(player_rect.x, player_rect.y)

        rep_image = rep_image + 1
        if rep_image > 120:
            rep_image =0
        elif rep_image > 90:
            index_vague_image = 1
        elif rep_image > 60:
            index_vague_image = 0
        elif rep_image > 30:
            index_vague_image = 1
        elif rep_image > 0:
            index_vague_image = 2
        
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        pressed_keys_indices = [i for i, v in enumerate(keys) if v]
        if len(pressed_keys_indices) > 0:
            binary_values = [bin(key_index) for key_index in pressed_keys_indices]
        else:
            binary_values = ['0']
        depinfo = jeu.fonction.deplacement(binary_values,key, player_rect, VITESSE, 0, colision_background, HAUTEUR, LARGEUR, last, index_image)
        imageplayer = depinfo[0]
        last = depinfo[1]
        index_image = depinfo[2]
        
        #   Code pour pause :
        if key[pygame.K_ESCAPE] == True:
            if testpause == False:
                testquit = menu.pause.Pause(6,player_rect.x,player_rect.y,screen,HAUTEUR,LARGEUR)
                testpause = True
                if testquit == False:
                    running = False
        else:
            testpause = False
        if 975 < player_rect.x < 1025 and 0 < player_rect.y < 60:
            jeu.game.LancementJeu(screen,990*LARGEUR/1920,950*HAUTEUR/1080,VITESSE, HAUTEUR,LARGEUR)
            running = False
        
        clock.tick(30)
        

        
        pygame.display.flip()
        pygame.display.update()