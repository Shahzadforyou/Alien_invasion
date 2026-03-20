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
    my_ship = Ship(ai_settings,screen)        
        #settin background color
                                                                             #main loop for game
    while True:
        gf.check_events(my_ship)     
        my_ship.update()                                                     #checking for event from screen
        gf.update_screen(ai_settings,screen,my_ship)
run_game()