import sys
import pygame

def run_game():
    pygame.init()              
                                                                            #initilizing gaming environment and screen
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")
                                                                           #main loop for game
    while True:
                                                                           #checking for event from screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        pygame.display.flip()
run_game()