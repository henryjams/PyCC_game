# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 16:11:58 2022

@author: Hank
"""

import pygame

class Rocket:
    """This class will manage the rocket"""
    
    def __init__(self, RR_game):
        self.screen = RR_game.screen
        self.settings = RR_game.settings
        self.screen_rect = RR_game.screen.get_rect()
        
        # Load the rocket and get its rect
        self.image = pygame.image.load('images/rocket.jpg').convert()
        #self.image.set_colorkey((230, 230, 230)) # Colorkey out the background
        self.rect = self.image.get_rect()
        
        # Start each new rocket at the starting point
        self.rect.center = self.screen_rect.center
        
        # Store a decimal value for the rocket's horizontal pos
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        # Movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        """Update the rocket's position based on the movement flag"""
        # Update the rocket's x value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed_horizontal
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed_horizontal
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed_vertical
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed_vertical
        
        # Update rect object from self.x
        self.rect.x = self.x
        self.rect.y = self.y
        
    def blitme(self):
        """draw the rocket at its current location"""
        self.screen.blit(self.image, self.rect)