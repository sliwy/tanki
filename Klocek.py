#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 18:40:13 2016

@author: maciej
"""
import pygame

class Klocek_1():
    def __init__(self,x=0,y=0):
        self.surf=pygame.image.load('klocek_1.png')
        self.re=self.surf.get_rect()
        self.move(x,y)
        
   
        
    def move(self,x,y):
        """Porusza klocek o x i y"""
        self.re=self.re.move(x,y)
        
    def rot_scale(self,angle=0,sc=1):
        """Obraca klocek (surface and rect) o kąt angle"""
        self.surf=pygame.transform.rotozoom(self.surf,angle,sc)
        self.re=self.surf.get_rect()
        
        
    def make_T(self,screen,pos):
        
        while self.re.top!=screen.screen.get_rect().centery:
            screen.screen.fill((255,255,255))
            kl1.move(0,10)
            kl1.rot_scale(5,0.99)
            screen.draw_on_me(kl1.surf,kl1.re)
            pygame.display.flip()
            time.sleep(0.3)            
    
        