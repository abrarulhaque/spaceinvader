import sys
import pygame
from pygame import mixer
import time
from alien import Alien
from bullet import Bullet
from ship import Ship
from pygame.locals import *
import msvcrt
def check_keydown_events(event,ai_settings,stats,screen,ship,bullets):

    """Respond to keypresses"""
    if event.key==pygame.K_RIGHT or event.key==pygame.K_d:
         #move the ship to right
         ship.moving_right=True
    elif event.key==pygame.MOUSEBUTTONDOWN or event.key==pygame.K_SPACE:
        fire_bullet(ai_settings,screen,ship,bullets)
    elif event.key==pygame.K_LEFT or event.key==pygame.K_a:
         #moving the ship to left
         ship.moving_left=True
    elif event.key==pygame.K_UP or event.key==pygame.K_w:
        ship.moving_up=True
    elif event.key==pygame.K_DOWN or event.key==pygame.K_s:
        ship.moving_down=True
    elif event.key==pygame.K_q:
        highscore=str(stats.high_score)
        file=open("alltimehighscore.txt",'w')
        file.write(highscore)
        sys.exit()
    elif event.key==pygame.K_p:
        stats.game_active=False
        pygame.mouse.set_visible(True)
    elif event.key==pygame.K_r:
        stats.game_active=True

def check_keyup_events(event,ship):
     """Respond to keyreleases"""
     if event.key==pygame.K_RIGHT or event.key==pygame.K_d:
            ship.moving_right=False
     elif event.key==pygame.K_LEFT or event.key==pygame.K_a:
            ship.moving_left=False
     elif event.key==pygame.K_UP or event.key==pygame.K_w:
         ship.moving_up=False
     elif event.key==pygame.K_DOWN or event.key==pygame.K_s:
         ship.moving_down=False
def check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            highscore=str(stats.high_score)
            file=open("alltimehighscore.txt",'w')
            file.write(highscore)
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,stats,screen,ship,bullets)
        elif event.type==pygame.KEYUP:
            check_keyup_events(event,ship)
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            #ship.shooting=True
            fire_bullet(ai_settings,screen,ship,bullets)
            check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y)
def check_high_score(stats, sb):
    """Check to see if there's a new high score."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_highscore()
def check_play_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    """start a new game when the player clicks 'PLAY!'"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if not stats.game_active and button_clicked:
        #reset settings
        ai_settings.initialize_dynamic_settings()
        #hide the mouse cursor
        pygame.mouse.set_visible(False)
        #reset game_stats
        stats.reset_stats()
        stats.game_active=True
        #reset the score board images
        sb.prep_score()
        sb.prep_highscore()
        sb.prep_level()
        sb.prep_ships()
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
def check_help_button(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    help_button_clicked=play_button.help_rect.collidepoint(mouse_x,mouse_y)
    if help_button_clicked:
        play_button.draw_help()

def get_number_alien_x(ai_settings,alien_width):
    avaliable_space_x=ai_settings.screen_width-(2*alien_width)
    number_of_aliens_in_a_row=int(avaliable_space_x/(2*alien_width))
    return number_of_aliens_in_a_row
def get_number_rows(ai_settings,ship_height,alien_height):
    avaliable_space_y=(ai_settings.screen_height-(16*alien_height)-ship_height)
    number_rows=int(avaliable_space_y/(2*alien_height))
    return number_rows
def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    alien=Alien(ai_settings,screen)
    alien_width=alien.rect.width
    alien.x=alien_width+2*alien_width*alien_number
    alien.rect.x=alien.x
    alien.rect.y=alien.rect.height+2*alien.rect.height*row_number+50
    aliens.add(alien)
def create_fleet(ai_settings,screen,ship,aliens):
    """create a full fleet of aliens"""
    #create an alien and find the number of aliens in a row
    #space between two alins is a alien's width
    alien=Alien(ai_settings,screen)
    alien_width=alien.rect.width
    number_of_aliens_in_a_row=get_number_alien_x(ai_settings,alien.rect.width)
    number_rows=get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
    #create first row of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_of_aliens_in_a_row):
            #create an alien and place it in the row
            create_alien(ai_settings,screen,aliens,alien_number,row_number)
def check_fleet_edges(ai_settings, aliens):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break
def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.alien_drop_speed
    ai_settings.fleet_direction *= -1
def update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button):
    screen.fill(ai_settings.screenbackground_colour)#filling the screen with background colour
    #redraw all bullets behind aliens and ship
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)
    #draw score board
    sb.show_score()
    #draw the play_button if the game is inactive
    if not stats.game_active:
        play_button.draw_button()
    # Make the most recently drawn screen visible
    pygame.display.flip()
def update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets):
    """update the positions of bullets and get rid of old bullets"""
    #update the position of bullets
    bullets.update()
    # removing old bullets from acopy of the bullets group
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings,screen,stats,sb,ship,aliens,bullets)
def check_bullet_alien_collisions(ai_settings, screen,stats,sb, ship, aliens, bullets):
    """Respond to bullet-alien collisions."""
    # Remove any bullets and aliens that have collided.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        explosion_sound=mixer.Sound('sounds/Explosion_02.wav')
        explosion_sound.play()
        for aliens in collisions.values():
            stats.score+=ai_settings.alien_score*len(aliens)
            sb.prep_score()
            check_high_score(stats,sb)
    if len(aliens)==0:
        bullets.empty()
        ai_settings.increase_speed()
        #increase level
        stats.level+=1
        sb.prep_level()
        ship.center_ship()
        create_fleet(ai_settings,screen,ship,aliens)
def fire_bullet(ai_settings,screen,ship,bullets):
        """fire a bullet if the limit has not reached"""
        #create new bullet and add it to the bullets group
        if len(bullets)<ai_settings.bullets_allowed:
            bullet_sound=mixer.Sound('sounds/laser1.wav')
            bullet_sound.play()
            new_bullet=Bullet(ai_settings,screen,ship)
            bullets.add(new_bullet)
def ship_hit(ai_settings,stats,sb,screen,ship,aliens,bullets):
    """respond to ship being hit"""
    if stats.ships_left>0:
        explosion_sound=mixer.Sound('sounds/Explosion_02.wav')
        explosion_sound.play()
        #decrement ship
        stats.ships_left-=1
        #update the score board
        sb.prep_ships()
        #empty the list of alins and bullets
        aliens.empty()
        bullets.empty()
        #create new fleet and ship
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship()
        #ai_settings.ship_speed_factor+=0.25
        #ai_settings.alien_speed_factor+=0.1
        #ai_settings.bullet_speed_factor+=0.1
        #pause
        sleep(0.5)
    else:
        stats.game_active=False
        pygame.mouse.set_visible(True)
def check_alien_hit_bottom(ai_settings,stats,sb,screen,ship,aliens,bullets):
    """check if any alien has hit the bottom of the screen"""
    screen_rect=screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom>=screen_rect.bottom:
            #treat it like ship been hit
            ship_hit(ai_settings,stats,sb,screen,ship,aliens,bullets)
            break
def update_aliens(ai_settings,stats,sb,screen,ship,aliens,bullets):
    check_fleet_edges(ai_settings,aliens)
    aliens.update()
    #look for the alien-ship collision
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,sb,screen,ship,aliens,bullets)
    #look for alien hitting the bottom of the screen
    check_alien_hit_bottom(ai_settings,stats,sb,screen,ship,aliens,bullets)
