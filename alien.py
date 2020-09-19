import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent single alien in the fleet"""
    def __init__(self,ai_settings,screen):
        """Initialize the alien and set its starting position"""
        super(Alien,self).__init__()
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.ai_settings=ai_settings

        #load the alien image
        self.image=pygame.image.load('images/alien.bmp')
        self.rect=self.image.get_rect()
        self.rect.x=self.screen_rect.width
        self.rect.y=self.screen_rect.top+10
        #store the alien's exact position
        self.x=float(self.rect.x)

    def check_edges(self):
        screen_rect=self.screen.get_rect()
        if self.rect.right>=screen_rect.right:
            return True
        elif self.rect.left<=0:
            return True
    def update(self):
        self.x+=self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction
        self.rect.x=self.x
    def blitme(self):
        """draw the alien at its current position"""
        self.screen.blit(self.image,self.rect)
