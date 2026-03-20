import pygame
class Ship():
    def __init__(self,screen):
        #starting position
        self.screen = screen
        #loading image of ship
        self.image = pygame.image.load("spaceship.1.png")
        self.image = pygame.transform.scale(self.image, (150, 140))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()


        #starting new ship at the bottom of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #movement flag
        self.moving_right = False
        self.moving_left = False
    def update(self):
        if self.moving_right:
            self.rect.centerx +=1
        if self.moving_left:
            self.rect.centerx -=1
    
    def blitme(self):
        #Draw ship at current location
        self.screen.blit(self.image,self.rect)