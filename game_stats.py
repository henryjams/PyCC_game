# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 11:49:19 2022

@author: Hank
"""

import json

class GameStats:
    """Track gameplay statistics for ~Chaos from the Warp~"""
    
    def __init__(self, cftw_game):
        """Initialize statistics"""
        self.settings = cftw_game.settings
        self.reset_stats()
        
        # Start cftw in an inactive state
        self.game_active = False
        
        # High score should never be reset
        self.high_score = self.get_saved_high_score()
    
    def get_saved_high_score(self):
        """Get high score from file, if it exists"""
        try:
            with open('high_score.json') as file:
                return json.load(file)
        except FileNotFoundError:
            return 0    
    
    def reset_stats(self):
        """Initialize statistics taht can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1