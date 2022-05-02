# -*- coding: utf-8 -*-
"""
Created on Sun May  1 22:28:53 2022

@author: Hank
"""

import pygame.font

class Scoreboard:
    """A class to report scoring information"""
    
    def __init__(self, cftw_game):
        """Initialize scorekeeping attributes"""
        self.screen = cftw_game.screen
        self.screen_rect = self.screen.get_rekt
        self.settings = cftw_game.settings
        self.stats = cftw_game.stats
        
        # Font settings for scoring information
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        
        # Prepare the initial score image
        self.prep_score()