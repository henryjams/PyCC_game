# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 21:25:44 2022

@author: Hank
"""

import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class WarpInvasion:
    """General class that manages game assets and behavior"""
    
    def __init__(self):
        """Initialize the game and allocate game resources"""
        pygame.init()
        self.settings = Settings()
        
        # Windowed mode
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        
        # For fullscreen mode, uncomment the following and disable "Windowed.."
        """
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        """
        
        pygame.display.set_caption("Chaos from the Warp")
                
        self.ship = Ship(self) 
        self.bullets = pygame.sprite.Group()
        
    def run_game(self):
        """Main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            
            # Get rid of bullets off the top edge of the screen rect
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
                       
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
                
    def _check_keydown_events(self, event):
        """Respond to a key being pressed"""
        if event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            pygame.display.quit()
            sys.exit()
    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip() # Make the screen visible

if __name__ == '__main__':
    # Make a game instance and run the game
    cftw = WarpInvasion()
    cftw.run_game()