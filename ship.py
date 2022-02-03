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
        self.screen_rect = cftw_game.screen.get_rect()
        
        # Load the ship and get its rect
        self.image = pygame.image.load('images/ship2.bmp')
        self.rect = self.image.get_rect()
        
        # Start each new ship at the starting point
        self.rect.midbottom = self.screen_rect.midbottom
        
    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
        