# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 11:49:19 2022

@author: Hank
"""

class GameStats:
    """Track gameplay statistics for ~Chaos from the Warp~"""
    
    def __init__(self, cftw_game):
        """Initialize statistics"""
        self.settings = cftw_game.settings
        self.reset_stats()
        
        # Start cftw in an inactive state
        self.game_active = False
        
        # High score should never be reset
        self.high_score = 0
        
    def reset_stats(self):
        """Initialize statistics taht can change during the game"""
        self.ships_left = self.settings.ship_limit
        self.score = 0