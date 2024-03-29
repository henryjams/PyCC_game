# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 16:10:48 2022

@author: Hank
"""

import sys
import pygame

from settings import Settings
from rocket import Rocket

class RocketRoger:
    """Main class of the game"""
    
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
        (self.settings.screen_width, self.settings.screen_height))
        
        pygame.display.set_caption("Rocket Roger")
        
        self.rocket = Rocket(self)
    
    def run_game(self):
        """Main loop for the game"""
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()
            print(self.rocket.rect.x, self.rocket.rect.y)
            print(self.rocket.screen_rect.bottom)
            
    def _check_events(self):
        """Respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                
    def _check_keydown_events(self, event):
        """Respond to a key being pressed"""
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_q:
            pygame.display.quit()
            sys.exit()
    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = False

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()

        pygame.display.flip() # Make the screen visible

if __name__ == '__main__':
    # Make a game instance and run the game
    RR = RocketRoger()
    RR.run_game()    