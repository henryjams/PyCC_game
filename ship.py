# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 08:38:08 2022

@author: Hank
"""

import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """This class will manage the ship"""
    
    def __init__(self, cftw_game):
        """Initialize the ship and set its starting position"""
        super().__init__()
        self.screen = cftw_game.screen
        self.settings = cftw_game.settings
        self.screen_rect = cftw_game.screen.get_rect()
        
        # Load the ship and resize it to a standard ship size
        self.image = pygame.transform.scale(
            pygame.image.load('images/ship.bmp').convert(), (45, 115))
        # Colorkey out the background
        self.image.set_colorkey((255, 255, 255)) 
        self.rect = self.image.get_rect()
        
        # Start each new ship at the starting point
        self.rect.midbottom = self.screen_rect.midbottom
        
        # Store a decimal value for the ship's horizontal pos
        self.x = float(self.rect.x)
        
        # Movement flag
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Update the ship's position based on the movement flag"""
        # Update the ship's x value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        # Update rect object from self.x
        self.rect.x = self.x
        
    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
        
    def center_ship(self):
        """Centers the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        