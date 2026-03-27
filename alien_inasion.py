import pygame
from setting import Setting
from ship import Ship
import game_func as gf
from pygame.sprite import Group
from alien import Alien

def run_game():
    pygame.init()   
    ai_settings = Setting()   

    
    screen = pygame.display.set_mode((ai_settings.width,ai_settings.length))
    pygame.display.set_caption("Alien Invasion")
    #make a ship
    my_ship = Ship(ai_settings,screen)        
    #make group to store bullet in
    bullets = Group()
    #make an alien
    aliens = Group()
    ##create the fleet of aliens
    gf.create_fleet(ai_settings,screen,my_ship,aliens)
    while True:
        gf.check_events(ai_settings,screen,my_ship,bullets)     
        my_ship.update()                                                    
        bullets.update()
    
        #getting rid of  bullets
        gf.update_bullets(bullets)
        
        gf.update_screen(ai_settings,screen,my_ship,aliens,bullets)
run_game() 