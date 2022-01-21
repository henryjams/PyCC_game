# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 21:25:44 2022

@author: Hank
"""

import sys
import pygame

from settings import Settings

class WarpInvasion:
    """General class that manages game assets and behavior"""
    
    def __init__(self):
        """Initialize the game and allocate game resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Chaos from the Warp")

    def run_game(self):
        """Main loop for the game"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.bg_color)
            pygame.display.flip() # Make the screen visible
            
if __name__ == '__main__':
    # Make a game instance and run the game
    cftw = WarpInvasion()
    cftw.run_game()