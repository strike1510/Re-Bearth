import pygame, sys

def GrandMenu(screen, HAUTEUR, LARGEUR):

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    TRANSPARENT = (0, 0, 0, 0)
    font = pygame.font.Font(None, 36)

    background = pygame.image.load("menu\\image\\bg.jpg")
    background = pygame.transform.scale(background, (LARGEUR, HAUTEUR))

    #   Bouton jouer :
    button1_text = font.render("Jouer", True, WHITE)
    button1_rect = button1_text.get_rect(center=(960*LARGEUR/1920, 540*HAUTEUR/1080))
    button1_visible = True

    rect_x = 885*LARGEUR/1920
    rect_y = 515*HAUTEUR/1080
    rect_width = 150
    rect_height = 50
    rect_visible = True

    def draw_text(text, font, color, surface, x, y):
        text_obj = font.render(text, True, color)
        text_rect = text_obj.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_obj, text_rect)

    pygame.mixer.music.load("menu\\sons\\menu1.mp3")
    pygame.mixer.music.play(-1)

    running = True
    while running:
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 885*LARGEUR/1920 <= x <= 1035*LARGEUR/1920 and 590*HAUTEUR/1080 <= y <= 640*HAUTEUR/1080:
                    running = False
                    return False
                if 885*LARGEUR/1920 <= x <= 1035*LARGEUR/1920 and 515*HAUTEUR/1080 <= y <= 565*HAUTEUR/1080:
                    button1_visible = False
                    rect_visible = False
                    pygame.mixer.music.stop()
                    running = False
                    return True

        if rect_visible:
            pygame.draw.rect(screen, BLACK, (rect_x, rect_y, rect_width, rect_height))
        if button1_visible:
            pygame.draw.rect(screen, BLACK, button1_rect)
            screen.blit(button1_text, button1_rect)
        
        
        # Bouton Jouer et Options
        #pygame.draw.rect(screen, BLACK, (885, 515, 150, 50))
        #draw_text("Jouer", pygame.font.Font(None, 36), WHITE, screen, 960, 540)

        pygame.draw.rect(screen, BLACK, (LARGEUR*885/1920, HAUTEUR*590/1080, 150, 50))
        draw_text("Quitter", pygame.font.Font(None, 36), WHITE, screen, LARGEUR*960/1920, HAUTEUR*615/1080)
        
        pygame.display.flip()
