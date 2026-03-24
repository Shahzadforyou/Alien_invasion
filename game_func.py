import pygame
import sys
from bullet import Bullet
def check_keydown_events(event,ai_settings,screen,my_ship,bullets):
    if event.key == pygame.K_RIGHT:
        my_ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        my_ship.moving_left = True
    elif event.key == pygame.K_UP:
        my_ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        my_ship.moving_down = True
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_SPACE:
        fire_bullets(ai_settings,screen,my_ship,bullets)
#function for firing bullets
def fire_bullets(ai_settings,screen,my_ship,bullets):
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings,screen,my_ship)
        bullets.add(new_bullet)
    
def check_keyup_events(event,my_ship):
    if event.key == pygame.K_RIGHT:
        my_ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        my_ship.moving_left = False
    elif event.key == pygame.K_UP:
        my_ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        my_ship.moving_down = False
    


def check_events(ai_settings,screen,my_ship,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,my_ship,bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,my_ship)

#function for removing bullets
def update_bullets(bullets):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        

def update_screen(ai_settings,screen,my_ship,alien,bullets):
    # screen.fill(ai_settings.bg_color)
    screen.fill(ai_settings.gradient_bottom)

    #Redraw all bullet behind ships and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    my_ship.blitme()
    alien.blitme()
    pygame.display.flip()