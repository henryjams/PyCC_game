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
        self.settings = cftw_game.settings
        
        # Load the alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp').convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        
        # Start each new alien at the origin (0,0)
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height / 4
        
        # Store the alien's exact horizontal pos
        self.x = float(self.rect.x)
    
    def check_edges(self):
        """Return True if alien is at the edge of the screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True    
    
    def update(self):
        """Move the alien fleet right or left"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
        
    
        
        