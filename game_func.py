import pygame
import sys

def check_keydown_events(event,my_ship):
    if event.key == pygame.K_RIGHT:
        my_ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        my_ship.moving_left = True
    elif event.key == pygame.K_UP:
        my_ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        my_ship.moving_down = True


def check_keyup_events(event,my_ship):
    if event.key == pygame.K_RIGHT:
        my_ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        my_ship.moving_left = False
    elif event.key == pygame.K_UP:
        my_ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        my_ship.moving_down = False
    


def check_events(my_ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,my_ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,my_ship)
        

def update_screen(ai_settings,screen,my_ship):
    # screen.fill(ai_settings.bg_color)
    screen.fill(ai_settings.gradient_bottom)
    my_ship.blitme()
    pygame.display.flip()