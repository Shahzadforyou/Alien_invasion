import sys
import pygame
from setting import Setting

def run_game():
    pygame.init()   
    ai_settings = Setting()           
                                                                            #initilizing gaming environment and screen
    screen = pygame.display.set_mode(ai_settings.width,ai_settings.length)
    pygame.display.set_caption("Alien Invasion")
        #settin background color
                                                                           #main loop for game
    while True:
                                                                           #checking for event from screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        screen.fill(ai_settings.bg_color)
        pygame.display.flip()
run_game()