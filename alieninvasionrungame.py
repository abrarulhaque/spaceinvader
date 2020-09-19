import sys
import pygame
from pygame.sprite import Group
from pygame import mixer
from settings import Settings
from ship import Ship
from game_stats import Gamestats
from button import Button
from scoreboard import Scoreboard
import gamefunctions as gft
is_paused= False
def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings=Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    #background music
    #mixer.music.load('backgroundwave.aiff')
    #mixer.music.play(-1)
    #create an instance for storing statistics and a score board
    stats=Gamestats(ai_settings)
    sb=Scoreboard(ai_settings,screen,stats)
    #make play_button
    play_button=Button(ai_settings,screen,'PLAY!')
    #make a ship
    ship=Ship(ai_settings,screen)
    #make a group to store bullets in
    bullets=Group()
    #make a alien group
    aliens=Group()
    #create the fleet of alien
    gft.create_fleet(ai_settings,screen,ship,aliens)
    # Start the main loop for the game.
    while True:
        if not is_paused:
            # Watch for keyboard and mouse events.
            gft.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
            if stats.game_active:
                ship.update()
                gft.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
                #redraw the screen during each pass through the loop
                gft.update_aliens(ai_settings,stats,sb,screen,ship,aliens,bullets)
            gft.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button)
run_game()
