import pygame
class Ship():
    def __init__(self,ai_setting,screen):
        #starting position
        self.screen = screen
        self.ai_settings = ai_setting

        #loading image of ship
        self.image = pygame.image.load("./images/mainspaceship.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #starting new ship at the bottom of screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        #storing value of ship centre
        self.center = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        
        

        
        #movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed

        if self.moving_left and self.rect.left >0:
            self.center -= self.ai_settings.ship_speed

        if self.moving_up and self.rect.top >0:
            self.centery -= self.ai_settings.ship_speed

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed
            
        self.rect.centerx = self.center
        self.rect.centery = self.centery
    
    def blitme(self):
        #Draw ship at current location
        self.screen.blit(self.image,self.rect)