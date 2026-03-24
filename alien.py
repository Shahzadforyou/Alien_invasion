import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self,ai_settings,screen,my_ship):
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        

        #create alien 
        self.img = pygame.image.load('OIP (1).jpg')
        self.rect = self.img.get_rect()

        #Start each new alien near the top left of screen

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the position of alien in float

        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.img,self.rect)