import pygame, sys
def LancementJeu(screen):
    
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    background = pygame.image.load("jeu\\image\\background.jpg")

    player = pygame.Rect((500, 500, 50, 50))

    def draw_text(text, font, color, surface, x, y):
        text_obj = font.render(text, True, color)
        text_rect = text_obj.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_obj, text_rect)

    running = True
    while running:
        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, (255, 0, 0), player)
        key = pygame.key.get_pressed()
        if key[pygame.K_q] == True:
            if player.x > 190:
                player.move_ip(-1, 0)
        if key[pygame.K_d] == True:
            if player.x < 1680:
                player.move_ip(1, 0)
        if key[pygame.K_z] == True:
            if player.y > 105:
                player.move_ip(0, -1)
        if key[pygame.K_s] == True:
            if player.y < 925:
                player.move_ip(0, 1)
        if key[pygame.K_ESCAPE] == True:
            running = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        pygame.display.flip()
        pygame.display.update()