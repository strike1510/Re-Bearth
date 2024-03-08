import pygame, sys

def GrandMenu(screen):

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    font = pygame.font.Font(None, 36)

    #   Bouton jouer :
    button1_text = font.render("Jouer", True, WHITE)
    button1_rect = button1_text.get_rect(center=(960, 540))
    button1_visible = True

    rect_x = 885
    rect_y = 515
    rect_width = 150
    rect_height = 50
    rect_visible = True

    def draw_text(text, font, color, surface, x, y):
        text_obj = font.render(text, True, color)
        text_rect = text_obj.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_obj, text_rect)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                # Vérifiez les coordonnées du clic et faire des actions 
                if 885 <= x <= 1035 and 590 <= y <= 640:
                    running = False
                    return False
                #if button1_visible and button1_rect.collidepoint(event.pos):
                if 885 <= x <= 1035 and 515 <= y <= 565:
                    # Cacher le bouton 1
                    button1_visible = False
                    rect_visible = False
                    running = False
                    return True

        screen.fill(WHITE)
        if rect_visible:
            pygame.draw.rect(screen, BLACK, (rect_x, rect_y, rect_width, rect_height))
        if button1_visible:
            pygame.draw.rect(screen, BLACK, button1_rect)
            screen.blit(button1_text, button1_rect)
        
        
        # Bouton Jouer et Options
        #pygame.draw.rect(screen, BLACK, (885, 515, 150, 50))
        #draw_text("Jouer", pygame.font.Font(None, 36), WHITE, screen, 960, 540)

        pygame.draw.rect(screen, BLACK, (885, 590, 150, 50))
        draw_text("Quitter", pygame.font.Font(None, 36), WHITE, screen, 960, 615)
        
        pygame.display.flip()