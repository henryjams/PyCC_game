# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 08:38:08 2022

@author: Hank
"""

import pygame

class Ship:
    """This class will manage the ship"""
    
    def __init__(self, cftw_game):
        self.screen = cftw_game.screen
        self.settings = cftw_game.settings
        self.screen_rect = cftw_game.screen.get_rect()
        
        # Load the ship and get its rect
        self.image = pygame.image.load('images/ship.bmp').convert()
        self.image.set_colorkey((230, 230, 230)) # Colorkey out the background
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
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
        