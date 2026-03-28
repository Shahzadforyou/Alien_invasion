import pygame
import sys
from bullet import Bullet
from alien import Alien
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
def update_bullets(bullets,aliens,ai_settings,screen,my_ship):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    #check for any bullet that hit aliens
    #if so get rid of the bullet and the alien
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
def get_alien_number_x(ai_settings,alien_width):
    #find number of alien that fit in a row
    #spacing between each alien is equal to one alien width
    available_space_x = ai_settings.width - 2 * alien_width
    number_alien_x = int(available_space_x/(2 * alien_width))
    return number_alien_x
def get_number_rows(ai_settings,ship_height,alien_height):
    #find the number of rows
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2*alien_height))
    return number_rows
def create_alien(ai_settings,screen,alien_number,row_number,aliens):
    #create alien and place it in row
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number

    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 *alien.rect.height * row_number
    aliens.add(alien)
    
def create_fleet(ai_settings,screen,my_ship,aliens):
    #create a full fleet of aliens
    #create a alien and find the number of aliens in row
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    ship_height = my_ship.rect.height
    number_alien_x = get_alien_number_x(ai_settings,alien_width)
    number_rows = get_number_rows(ai_settings,ship_height,alien_height)
    #create the fleet of aliens
    for row_number in range(number_rows):
        
       for alien_number in range(number_alien_x):
        #create alien and place it in row
           create_alien(ai_settings,screen,alien_number,row_number,aliens)
def change_fleet_direction(ai_settings,aliens):
    #Drop the entire fleet and change the fleets direction
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
    
def check_fleet_edges(ai_settings,aliens):
    #Respond appropriately if any aliens have reached an edge
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break
#check the sides of alien from alem.py
def update_alien(ai_settings,aliens):
    #check if the fleet is at an edge and update the position of all aliens in fleet
    check_fleet_edges(ai_settings,aliens)
    aliens.update()

def update_screen(ai_settings,screen,my_ship,aliens,bullets):
    # screen.fill(ai_settings.bg_color)
    screen.fill(ai_settings.gradient_bottom)

    #Redraw all bullet behind ships and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    for alien in aliens.sprites():
        alien.blitme()
        
    my_ship.blitme()
    pygame.display.flip()