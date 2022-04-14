# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 21:48:47 2022

@author: Hank
"""

import pygame

class Settings:
    """A class for storing all game settings"""
    
    def __init__(self):
        """Initialize the game settings"""
        # Screen settings
        self.screen_width = 1600
        self.screen_height = 1200
        self.bg_color = (10, 10, 10)
        self.bg_img = pygame.image.load('images/background3.jpg')
        
        # Bullet settings
        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (250, 10, 5)
        self.bullets_allowed = 5
        
        # Ship settings
        self.ship_speed = 1