# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 16:02:17 2022

@author: Hank
"""

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """This class will manage bullets fired from the ship"""
    
    def __init__(self, cftw_game):
        """Create a bullet object at the ship's current pos"""
        super().__init__()
        self.screen = cftw_game.screen
        self.settings = cftw_game.settings
        self.color = self.settings.bullet_color
        
        # Create a bullet at (0, 0) then set correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = cftw_game.ship.rect.midtop
        
        # Store the bullet's pos as a float
        self.y = float(self.rect.y)
        
    def update(self):
        """Move the bullet up the screen"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
        
    def draw_bullet(self):
        """Draw the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)