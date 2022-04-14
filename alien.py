# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 19:42:55 2022

@author: Hank
"""

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""
    
    def __init__(self, cftw_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = cftw_game.screen
        
        # Load the alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp').convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        
        # Start each new alien at the origin (0,0)
        self.rect.x = self.rect.width / 2
        self.rect.y = self.rect.height / 4
        
        # Store the alien's exact horizontal pos
        self.x = float(self.rect.x)