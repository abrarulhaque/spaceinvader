import pygame.font
from pygame.sprite import Group
from ship import Ship
class Scoreboard():
    """a class for reporting scoring information"""
    def __init__(self,ai_settings,screen,stats):
        """initialize scoring attributes"""

        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.ai_settings=ai_settings
        self.stats=stats

        #font setting for scoring information
        self.text_colour=(0,0,255)
        self.font=pygame.font.SysFont(None,48)
        self.high_score_text_colour=(0,255,0)
        self.level_text_colour=(30,30,30)
        #prepare the initial score image
        self.prep_score()
        self.prep_highscore()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """turn the score in rendered image"""
        score_str=str(self.stats.score)
        score_str="{:,}".format(self.stats.score)
        self.score_image=self.font.render(score_str,True,self.text_colour,self.ai_settings.screenbackground_colour)

        #display the score at the top right of the screen
        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.screen_rect.right-20
        self.score_rect.top=self.screen_rect.top

    def prep_highscore(self):
        high_score_str=str(self.stats.high_score)
        high_score_str="{:,}".format(self.stats.high_score)
        self.high_score_image=self.font.render(high_score_str,True,self.high_score_text_colour,self.ai_settings.screenbackground_colour)
        #display the high score at the top center of the screen
        self.high_score_rect=self.high_score_image.get_rect()
        self.high_score_rect.centerx=self.screen_rect.centerx
        self.high_score_rect.top=self.screen_rect.top
    def prep_level(self):
        """turn the level in rendered image"""
        level_str=str(self.stats.level)
        self.level_image=self.font.render(level_str,True,self.level_text_colour,self.ai_settings.screenbackground_colour)
        #display the level under the score
        self.level_rect=self.level_image.get_rect()
        self.level_rect.right=self.score_rect.right
        self.level_rect.top=self.score_rect.bottom+10

    def prep_ships(self):
        """show how many ships are left"""
        self.ships=Group()
        for ship_number in range(self.stats.ships_left+1):
            ship=Ship(self.ai_settings,self.screen)
            ship.rect.x=3+ship_number*ship.rect.width
            ship.rect.y=2
            self.ships.add(ship)

    def show_score(self):
        """Draw the score on screen"""
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.ships.draw(self.screen)
