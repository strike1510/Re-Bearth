import pygame, sys , jeu.room1 , menu.pause , math , jeu.fonction
def battle(screen,pos_player_x,pos_player_y, HAUTEUR,LARGEUR):
    testpause = False
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    TRANSPARENT = (0, 0, 0, 0)
    dimmension_perso = 64
    
    background = pygame.image.load("jeu\\image\\combat\\grille.png")
    clock = pygame.time.Clock()

    #TEST 
    rect_x = LARGEUR // 2
    rect_y = HAUTEUR // 2
    screen_x = 0
    screen_y = 0
    #background = pygame.image.load("jeu\\image\\background.jpg")
    background = pygame.transform.scale(background, (LARGEUR, HAUTEUR))

    player = pygame.Surface((dimmension_perso, dimmension_perso), pygame.SRCALPHA)
    player.fill(TRANSPARENT)
    

    #Image joueur :
    imagesjaune = pygame.image.load("jeu\\image\\combat\\casejaune.png")
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

    coo = [[0 for _ in range(16)] for _ in range(16)]
    for i in range (0 ,16):
        for j in range (0,16):
            coo[i][j] = (512*LARGEUR/1920)+i*60,(92*HAUTEUR/1080)+j*60
    
    cooplayerx = 1
    cooplayery = 1

    tempx , tempy = coo[cooplayerx][cooplayery]
    tempy -= 8*LARGEUR/1920
    player_rect = player.get_rect(center=(tempx, tempy))

    
    while running:
        key = pygame.key.get_pressed()
            
        screen_x = rect_x - LARGEUR / 2
        screen_y = rect_y - HAUTEUR / 2
        screen.blit(background, (screen_x, screen_y))
        pygame.draw.rect(player, (0, 0, 255), player.get_rect(), 3)  
        screen.blit(imageplayer, player_rect)
        
        
        
        #   Code pour pause :
        if key[pygame.K_ESCAPE] == True:
            if testpause == False:
                testquit = menu.pause.Pause(screen,HAUTEUR,LARGEUR)
                testpause = True
                if testquit == False:
                    running = False
        else:
            testpause = False

        
        clock.tick(30)
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                running = False

        
        pygame.display.flip()
        pygame.display.update()