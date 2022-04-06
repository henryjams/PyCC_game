# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 16:11:48 2022

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