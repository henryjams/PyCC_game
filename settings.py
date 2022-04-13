# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 21:48:47 2022

@author: Hank
"""

class Settings:
    """A class for storing all game settings"""
    
    def __init__(self):
        """Initialize the game settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (10, 10, 10)
        
        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (250, 10, 5)
        self.bullets_allowed = 3
        
        # Ship settings
        self.ship_speed = .3