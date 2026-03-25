import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self,ai_settings,screen):
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        

        #create alien 
        self.img = pygame.image.load('./images/alien.png')
        self.img = pygame.transform.scale(self.img, (150, 140))
        self.rect = self.img.get_rect()
        self.screen_rect = screen.get_rect()

        #Start each new alien near the top left of screen

        # Start each new alien near the top-left of screen
        self.rect.x = self.rect.width  -150    # Left edge with offset
        self.rect.y = self.rect.height -140    # Top edge with offset


        # Store the position of alien in float
        self.centerx = float(self.rect.centerx)

    def blitme(self):
        self.screen.blit(self.img,self.rect)