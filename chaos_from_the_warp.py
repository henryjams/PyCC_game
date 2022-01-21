# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 21:25:44 2022

@author: Hank
"""

import sys

import pygame

class WarpInvasion:
    """General class that manages game assets and behavior"""
    
    def __init__(self):
        """Initialize the game and allocate game resources"""
        pygame.init()
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Chaos from the Warp")
        
    def run_game(self):
        """Main loop for the game"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            pygame.display.flip()
            
if __name__ == '__main__':
    # Make a game instance and run the game
    cftw = WarpInvasion()
    cftw.run_game()