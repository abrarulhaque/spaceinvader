import pygame.font
class Button():
    def __init__(self,ai_settings,screen,messege):
        """Initialize button attribute"""
        self.screen=screen
        self.screen_rect=screen.get_rect()

        #set the dimension and properties of the button
        self.width,self.height=200,50
        self.button_colour=(0,255,0)
        self.help_button_colour=(255,0,0)
        self.text_colour=(255,255,255)
        self.font=pygame.font.SysFont(None,48)
        #set the button at the center of the screen
        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.centerx=self.screen_rect.centerx
        self.rect.y=self.screen_rect.centery

        #the messege button should be prepped once
        self.prep_messege(messege)

    def prep_messege(self,messege):
        """turn the messege into rendered image and center the text on the button"""
        self.messege_image=self.font.render(messege,True,self.text_colour,self.button_colour)
        self.messege_image_rect=self.messege_image.get_rect()
        self.messege_image_rect.centerx=self.rect.centerx
        self.messege_image_rect.y=self.rect.y+10

    def draw_button(self):
        #draw blank button and then display messege
        self.screen.fill(self.button_colour,self.rect)
        self.screen.blit(self.messege_image,self.messege_image_rect)
