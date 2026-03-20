import pygame
import sys

def check_events(my_ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                my_ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                my_ship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                my_ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                my_ship.moving_left = False
        

def update_screen(ai_settings,screen,my_ship):
    screen.fill(ai_settings.bg_color)
    my_ship.blitme()
    pygame.display.flip()