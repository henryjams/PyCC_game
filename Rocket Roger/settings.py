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
        self.bg_color = (240, 240, 240)
        
        # rocket settings
        self.rocket_speed_horizontal = .5
        self.rocket_speed_vertical = 1.25