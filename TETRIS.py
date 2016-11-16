#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 18:22:54 2016

@author: maciej
"""
import pygame
import sys
from pygame.locals import *
import time
import copy

SCORE=0
el=[]


class Okno():
    """ Inicjalizuje obiekt okna gry """
    def __init__(self,window_width,window_height):
        pygame.init()
        self.elements_surf=[]
        self.elements_re=[]
        self.window_width=window_width
        self.window_height=window_height
        self.screen=pygame.display.set_mode((self.window_width,self.window_height),0,32)
        pygame.display.set_caption('TETRIS - nowa rewelacyjna rozgrywka!!!')
        
    def draw_on_me(self,surf,pos=(0,0)):
        self.screen.blit(surf,pos)
    def add_element(self,element_surf,element_re):
        self.elements_surf.append(element_surf)
        self.elements_re.append(element_re)
    def del_element(self,element_surf,elment_re):
        self.elements_surf.remove(element_surf)
        self.elements_re.remove(elment_re)
    def draw_all_el(self):
        for i in range(len(self.elements_surf)):
            self.screen.blit(self.elements_surf[i],(self.elements_re[i].left,self.elements_re[i].top))
        
#class okno_gry():
#    def __init__(self,window_width,window_height):
        

        


        

class Klocek_1():
    def __init__(self,x=0,y=0):
        self.surf=pygame.image.load('klocek_1.png')
        self.re=self.surf.get_rect()
        self.move(x,y)
        
   
        
    def move(self,x,y):
        """Porusza klocek o x i y"""
        self.re=self.re.move(x,y)
        
    def rot_scale(self,angle=90,sc=1):
        """Obraca klocek (surface and rect) o kąt angle"""
        oldCenter=self.re.center
        self.surf=pygame.transform.rotozoom(self.surf,angle,sc)
        self.re=self.surf.get_rect()
        self.re.center=oldCenter
        
        
    def make_T(self,screen):
        self.rot_scale(0,0.85)
        kreska=copy.copy(self)
        while self.re.centery<(screen.screen.get_rect().centery):
            screen.screen.fill((255,255,255))
            screen.draw_all_el()
            self.move(0,20)
            
            screen.draw_on_me(self.surf,self.re)
            pygame.display.flip()
            time.sleep(0.04)
        screen.add_element(self.surf,self.re)
        kreska.rot_scale(90,0.85)

        while kreska.re.bottom<(self.re.top):
            screen.screen.fill((255,255,255))
            kreska.move(0,20)
            screen.draw_all_el()
            screen.draw_on_me(kreska.surf,kreska.re)
            pygame.display.flip()
            time.sleep(0.04)
        screen.add_element(kreska.surf,kreska.re)
            
            

    
        
class TETRIS():
    def __init__(self,score=SCORE):
        pygame.init()
        self.screen=Okno(800,800)
        
        self.intro()
        
        
        self.menu()
    
        mainloop=True
        while mainloop:
            # Do not go faster than this framerate.
            for event in pygame.event.get():
                # User presses QUIT-button.
                if event.type == pygame.QUIT:
                    mainloop = False 
                    
                elif event.type == pygame.KEYDOWN:
                    # User presses ESCAPE-Key
                    if event.key == pygame.K_ESCAPE:
                        mainloop = False
                    if event.key == pygame.K_RETURN:
                        self.run()
        pygame.quit()
    def intro(self):
        kl1=Klocek_1(x=70,y=-200)
        kl1.make_T(self.screen)
        kl2=Klocek_1(x=330,y=-200)
        kl2.make_T(self.screen)
        time.sleep(5)
        
    def menu(self):
        menuloop=True
        while menuloop:
            
            self.screen.screen.fill((100,100,100))
                
            myfont = pygame.font.SysFont("Comic Sans MS", 30)
            
            text_surface_NG = myfont.render('Nowa gra', False, (0,0,0))
            text_re_NG=text_surface_NG.get_rect()
            text_surface_LG = myfont.render('Wczytaj grę', False, (0,0,0))
            text_re_LG=text_surface_LG.get_rect()
            
            self.screen.screen.blit(text_surface_NG,(self.screen.screen.get_rect().centerx-100,75))
            self.screen.screen.blit(text_surface_LG,(self.screen.screen.get_rect().centerx-120,150))
            
            text_re_NG=text_re_NG.move(self.screen.screen.get_rect().centerx-100,75)
            text_re_LG=text_re_LG.move(self.screen.screen.get_rect().centerx-100,150)
            
            pygame.display.flip()
            # Do not go faster than this framerate.
            for event in pygame.event.get():

                # User presses QUIT-button.
                if event.type == pygame.QUIT:
                    
                    menuloop = False 
                    pygame.quit()
                    break
                elif event.type == pygame.KEYDOWN:
                    # User presses ESCAPE-Key
                    if event.key == pygame.K_ESCAPE:
                        menuloop = False
                        pygame.quit()
                        break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if text_re_NG.left<=pos[0]<=text_re_NG.right and text_re_NG.top<=pos[1]<=text_re_NG.bottom:
                        self.new_game()
                        
                        self.screen.screen.fill((200,200,200))
                        pygame.display.flip()
                        menuloop=False
                    if text_re_LG.left<=pos[0]<=text_re_LG.right and text_re_LG.top<=pos[1]<=text_re_LG.bottom:
                        self.load_game()
                        
                        self.screen.screen.fill((200,200,200))
                        pygame.display.flip()
                        menuloop=False                        
                        

                        
                        
#        pygame.display.flip()
        
        
        
        
    def run(self):
        """ mainloop"""
        mainloop=True
        while mainloop:
            for event in pygame.event.get():
                # User presses QUIT-button.
                if event.type == pygame.QUIT:
                    mainloop = False 
                elif event.type == pygame.KEYDOWN:
                    # User presses ESCAPE-Key
                    if event.key == pygame.K_ESCAPE:
                        mainloop = False
                        
                        
                        
        pygame.quit()
        
        
    def new_game(self):
        pass
    
    def load_game(self):
        pass
        
            
if __name__ == '__main__':
   TETRIS()
   
   
   
   
   