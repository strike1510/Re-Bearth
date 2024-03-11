import pygame, sys, time
WHITE = (255, 255, 255)
TRANSPARENT = (255, 255, 255, 20)
BLACK = (0, 0, 0)

def Pause(screen):
    pause = True
    test = False

    PauseFond = pygame.Surface((440, 540), pygame.SRCALPHA)
    PauseFond.fill(TRANSPARENT)
    PauseFond_rect = PauseFond.get_rect(center=(960, 500))
    image_PauseFond = pygame.image.load('menu\\image\\pause.png')

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
        pygame.draw.rect(screen, BLACK, (885, 610, 150, 50))
        draw_text("Quitter", pygame.font.Font(None, 36), WHITE, screen, 960, 635)
        if key[pygame.K_ESCAPE] == True:
            if test == True:
                pause = False
                return True
        else:
            test = True
        
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    if 885 <= x <= 1035 and 610 <= y <= 660:
                        return False