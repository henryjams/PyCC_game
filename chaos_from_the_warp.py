# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 21:25:44 2022

@author: Hank
"""

import sys
import pygame

from settings import Settings
from ship import Ship

class WarpInvasion:
    """General class that manages game assets and behavior"""
    
    def __init__(self):
        """Initialize the game and allocate game resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
        (self.settings.screen_width, self.settings.screen_height))
        
        pygame.display.set_caption("Chaos from the Warp")
                
        self.ship = Ship(self) 
        
    def run_game(self):
        """Main loop for the game"""
        while True:
            self._check_events()
            self._update_screen()
            
    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()           

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip() # Make the screen visible

if __name__ == '__main__':
    # Make a game instance and run the game
    cftw = WarpInvasion()
    cftw.run_game()