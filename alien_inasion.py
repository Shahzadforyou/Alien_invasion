import sys
import pygame
from setting import Setting
from ship import Ship
import game_func as gf

def run_game():
    pygame.init()   
    ai_settings = Setting()   
                                                                            #initilizing gaming environment and screen
    screen = pygame.display.set_mode((ai_settings.width,ai_settings.length))
    pygame.display.set_caption("Alien Invasion")
    #make a ship
    my_ship = Ship(screen)        
        #settin background color
                                                                           #main loop for game
    while True:
        gf.check_events()                                                             #checking for event from screen
        screen.fill(ai_settings.bg_color)
        my_ship.blitme()
        pygame.display.flip()
run_game()