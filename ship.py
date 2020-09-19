import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    def __init__(self,ai_settings,screen):
        """Initialize the ship and set its starting position."""
        super(Ship,self).__init__()
        self.screen=screen
        self.ai_settings=ai_settings
        #load the ship image and get its rect
        self.image=pygame.image.load('images/ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        #star each new ship at the bottom center of the screen
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom
        self.y=self.rect.top
        #movement flag
        self.moving_right=False
        self.moving_left=False
        self.moving_up=False
        self.moving_down=False
        self.shooting=False
    def update(self):
            """Update the ship's position based on the movement flag."""
            #update the ship's center value not the rect
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.rect.centerx+=self.ai_settings.ship_speed_factor
            if self.moving_left and self.rect.left > 0:
                self.rect.centerx-=self.ai_settings.ship_speed_factor
            if self.moving_up and self.y > self.screen_rect.top:
                self.y-=self.ai_settings.ship_speed_factor
            if self.moving_down and self.rect.bottom<self.screen_rect.bottom:
                self.y+=self.ai_settings.ship_speed_factor
            self.rect.top=self.y
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image,self.rect)
    def center_ship(self):
        """center the ship on screen"""
        self.rect.centerx=self.screen_rect.centerx
        self.y=self.screen_rect.bottom-45
