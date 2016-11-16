#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 16:50:39 2016

@author: maciej
"""
import pygame, sys, time
from pygame.locals import *
import Klocek

class Okno():
    """ Inicjalizuje obiekt okna gry """
    def __init__(self,window_width,window_height):
        pygame.init()
        self.window_width=window_width
        self.window_height=window_height
        self.screen=pygame.display.set_mode((self.window_width,self.window_height),0,32)
        pygame.display.set_caption('TETRIS - nowa rewelacyjna rozgrywka!!!')
        
    def draw_on_me(self,surf,pos=(0,0)):
        self.screen.blit(surf,pos)
        


        
    def intro(self,screen):
        kl1=Klocek.Klocek_1()
        kl1.make_T()
        
        
        
if __name__ == "__main__":
    sc=Okno(300,300)
    
        
        
        