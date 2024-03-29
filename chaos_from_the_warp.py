# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 21:25:44 2022

@author: Hank
"""

import sys
from time import sleep
import json

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

background = pygame.image.load('images/background.jpg')

class WarpInvasion:
    """General class that manages game assets and behavior"""
    
    def __init__(self):
        """Initialize the game and allocate game resources"""
        pygame.init()
        self.settings = Settings()
        
        # Windowed mode
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        
        # Set the caption and load the background image
        pygame.display.set_caption("Chaos from the Warp")
        
        # Create an instance to store game statistics and create a scoreboard
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        
        self.ship = Ship(self) 
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
        self._create_fleet()

        self.play_button = Button(self, "Play")
        
    def run_game(self):
        """Main loop for the game"""
        while True:
            self._check_events()
            
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            
            self._update_screen()
            
    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                
    def _check_play_button(self, mouse_pos):
        """Start a new game is the player clicks on the play button"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self._start_game()
    
    def _start_game(self):
        """Starts the game"""
        # Reset the game settings
        self.settings.initialize_dynamic_settings()
        
        # Reset the game statistics
        self.stats.reset_stats()
        self.stats.game_active = True
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_ships()
        
        # Get rid of any remaining aliens and bullets
        self.aliens.empty()
        self.bullets.empty()
        
        # Create a new fleet and center the ship
        self._create_fleet()
        self.ship.center_ship()
        
        # Hide the mouse cursor
        pygame.mouse.set_visible(False)
        
    def _check_keydown_events(self, event):
        """Respond to a key being pressed"""
        if event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            self._close_game()
        elif event.key == pygame.K_p and not self.stats.game_active:
            self._start_game()
    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            
    def _update_bullets(self):
        """Update the position of bullets and remove old bullets"""
        # Update bullet position
        self.bullets.update()
        
        # Get rid of bullets off the top edge of the screen rect
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        self._check_bullet_alien_collisions()
        
    def _check_bullet_alien_collisions(self):
        """Respond when bullets collide with aliens"""
        # Remove any bullets and aliens that have collided
        collisions = pygame.sprite.groupcollide(
                        self.bullets, self.aliens, True, True)
        
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            # Destroy existing bullets and create a new Fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            
            # Increase level
            self.stats.level += 1
            self.sb.prep_level()
            
    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this scenario the same as if the ship was destroyed
                self._ship_hit()
                break

    def _update_aliens(self):
        """Check if the fleet is at an edge, then 
            Update the positions of the alien fleet"""
        self._check_fleet_edges()
        self.aliens.update()
        
        # Look for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        
        # Look for aliens hitting the bottom of the screen
        self._check_aliens_bottom()
        
    def _ship_hit(self):
        """Respond to the ship being hit during play"""
        if self.stats.ships_left > 0:
            # Decrement ships_left and update scoreboard
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            
            # Get rid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()
            
            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()
            
            # Pause briefly so Player can be ready for the restart
            sleep(1)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
        
    def _create_fleet(self):
        """Create the fleet of aliens"""
        # Create an alien and find the number of aliens that can fit in a row
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size  
        available_space_x = self.settings.screen_width - int(2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        
        # Determine the number of rows that will fit on the screen vertically
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                                 (3 * alien_height) - ship_height)
        number_rows = available_space_y // int(1.5 * alien_height)
        
        # Create the full fleet of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)
            
    def _create_alien(self, alien_number, row_number):
        # Create an alien and place it in the row
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        
        # Offset every other row
        if row_number % 2 == 0:
            offset = 0
        else:
            offset = 0.3 * alien_width
        
        alien.x = alien_width + offset + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height // 3 + (
                            int(1.5 * alien.rect.height) * row_number)
        self.aliens.add(alien)
        
    def _check_fleet_edges(self):
        """Respond when aliens have reached the edge of the screen"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
            
    def _change_fleet_direction(self):
        """Drop the entire fleet and change direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
        
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.blit(self.settings.bg_img, (0, 0))
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        
        # Draw the score information
        self.sb.show_score()
                
        # Draw the play button if the game is inactive
        if not self.stats.game_active:
            self.play_button.draw_button()
        
        pygame.display.flip() # Make the screen visible
        
    def _close_game(self):
        """Save high score and exit"""
        saved_high_score = self.stats.get_saved_high_score()
        if self.stats.high_score > saved_high_score:
            with open('high_score.json', 'w') as file:
                json.dump(self.stats.high_score, file)
                
        pygame.display.quit()
        sys.exit()

if __name__ == '__main__':
    # Make a game instance and run the game
    cftw = WarpInvasion()
    cftw.run_game()