# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 13:44:48 2022

@author: Hank
"""

import sys
import pygame

from settings import Settings

class Keys:
    
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Key displayer")
        
    def run(self):
        while True:
            self._check_events()
            self._update_screen()
            
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                    
    def _check_keydown_events(self, event):
        print(event.key)
        if event.key == pygame.K_q:
            pygame.display.quit()
            sys.exit()
    
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        pygame.display.flip()
        
if __name__ == '__main__':
    keys = Keys()
    keys.run()