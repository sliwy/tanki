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
import numpy as np

WINDOWHEIGHT=900
WINDOWIDTH=1200

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
            
def rotate_image(image,rect,direction,old_direction = 0):
          
    old_center=rect.center
    if old_direction == 0:        
        if direction == 1:
            image = pygame.transform.rotate(image,-90)
        elif direction == 2:
            image = pygame.transform.rotate(image,180)
        elif direction == 3:
            image = pygame.transform.rotate(image,90)
    elif old_direction == 1:        
        if direction == 0:
            image = pygame.transform.rotate(image,90)
        elif direction == 2:
            image = pygame.transform.rotate(image,-90)
        elif direction == 3:
            image = pygame.transform.rotate(image,180)
    elif old_direction == 2:        
        if direction == 0:
            image = pygame.transform.rotate(image,180)
        elif direction == 1:
            image = pygame.transform.rotate(image,90)
        elif direction == 3:
            image = pygame.transform.rotate(image,-90)
    elif old_direction == 3:        
        if direction == 0:
            image = pygame.transform.rotate(image,-90)
        elif direction == 1:
            image = pygame.transform.rotate(image,180)
        elif direction == 2:
            image = pygame.transform.rotate(image,90)
            
        
    rect = image.get_rect()
    rect.center=old_center
    return image, rect, direction
    
            
class Tank_own(pygame.sprite.Sprite):
    
    def __init__(self,screen,width=50,height=70,x=0,y=0,dir=0,speed_bullet=30,direction=0,speed_tank=15):
       pygame.sprite.Sprite.__init__(self)    
       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
#       self.image = pygame.Surface([width, height])
       self.image = pygame.image.load('czolg2.png')
#       self.image.fill((100,100,100))
       self.screen=screen
       self.speed_bullet=speed_bullet
       self.speed_tank=speed_tank
       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()
       self.rect = self.rect.move(x,y)
       self.direction = direction
       
       self.image,self.rect,self.direction = rotate_image(self.image,self.rect,self.direction)

    def shoot(self):
        
        
        return Bullet(self.rect.copy(),self.direction,self.screen,self.speed_bullet)
    def move(self,key,op):
        old_center=self.rect.center
        
        if key == K_UP:
            # trzeba zaimplementowac odbijanie sie czolgu od scian
            self.image,self.rect,self.direction = rotate_image(self.image,self.rect,0,self.direction)
            self.rect=self.image.get_rect()
            self.rect.center=old_center
            self.rect = self.rect.move(0,-self.speed_tank)
           
        elif key == K_RIGHT:
            self.image,self.rect,self.direction = rotate_image(self.image,self.rect,1,self.direction)
            self.rect=self.image.get_rect()
            self.rect.center=old_center
            self.rect=self.rect.move(self.speed_tank,0)
        elif key == K_DOWN:
            self.image,self.rect,self.direction = rotate_image(self.image,self.rect,2,self.direction)
            self.rect=self.image.get_rect()
            self.rect.center=old_center
            self.rect=self.rect.move(0,self.speed_tank)
        elif key == K_LEFT:
            self.image,self.rect,self.direction = rotate_image(self.image,self.rect,3,self.direction)
            self.rect=self.image.get_rect()
            self.rect.center=old_center
            self.rect=self.rect.move(-self.speed_tank,0)
            
            
class Tank_enemy(pygame.sprite.Sprite):
    
    pass

        
        
        
class Bullet(pygame.sprite.Sprite):
    
    def __init__(self,rect,direction,screen,speed_bullet):
        # PAmietac, ze self self wezmie pierwszego selfa, dlatego copy
        self.direction = direction
        self.screen=screen
        self.speed_bullet=speed_bullet
#        self.image=pygame.image.load()
        self.image = pygame.Surface([5,10])
        self.image.fill((255,255,0)) 
        self.rect=rect
        if self.direction == 0:
            self.rect.y-=self.speed_bullet
        elif self.direction == 1:
            self.rect.x+=self.speed_bullet
        elif self.direction == 2:
            self.rect.y+=self.speed_bullet
        elif self.direction == 3:
            self.rect.x-=self.speed_bullet
            
        self.image,self.rect,self.direction = rotate_image(self.image,self.rect,self.direction)
        
    
    def move(self):
        if self.direction == 0:
            self.rect = self.rect.move(0,-self.speed_bullet)
        elif self.direction == 1:
            self.rect = self.rect.move(self.speed_bullet,0)
        elif self.direction == 2:
            self.rect = self.rect.move(0,self.speed_bullet)
        elif self.direction == 3:
            self.rect = self.rect.move(-self.speed_bullet,0)
    def update(self):
            self.move()
            self.screen.blit(self.image,self.rect)
            return self.rect.x,self.rect.y
    def update_all(lista):
        for l in range(len(lista)-1,-1,-1):
            x, y = lista[l].update()
            if x>WINDOWIDTH or x<0 or y>WINDOWHEIGHT or y<0:
                del lista[l]
    

            
           
            
            
        
    

window=Okno(WINDOWIDTH,WINDOWHEIGHT)
#k=Tank_own(window.screen,direction=2)
#d=Tank_own(window.screen,x = 100,y = 200)
#z=pygame.sprite.Group(k,d)
#k_bullet=k.shoot()
#window.screen.blit(k.image,k.rect)
#for e in range(100):
#    window.screen.fill((100,100,100))
#    k.rect=k.rect.move((10,10))
#
#    k_bullet.update()
#
#    window.screen.blit(k.image,k.rect)
#    window.screen.blit(k_bullet.image,k_bullet.rect)
##    z.draw(window.screen)
#    pygame.display.flip()
#    time.sleep(0.1)
window.screen.fill((100,100,100))
mainloop=True
k=Tank_own(window.screen,direction=2,x=350,y=350)
window.screen.blit(k.image,k.rect)
pygame.display.flip()
bullet_list=[]
p=False
while mainloop:
    window.screen.fill((100,100,100))
    # Do not go faster than this framerate.
    for event in pygame.event.get():
        # User presses QUIT-button.
        if event.type == QUIT:
            mainloop = False 
            
        elif event.type == KEYDOWN:
            # User presses ESCAPE-Key
            if event.key == K_ESCAPE:
                mainloop = False
            elif event.key == K_UP or event.key == K_RIGHT or event.key == K_DOWN or event.key == K_LEFT:
                k.move(event.key,1)
                print(k.rect)
            elif event.key == K_SPACE:
                p=True
                bullet_list.append(k.shoot())

    keys = pygame.key.get_pressed()  #checking pressed keys
    if keys[K_UP]:
        k.move(K_UP,1)
    elif keys[K_DOWN]:
        k.move(K_DOWN,1)
    elif keys[K_RIGHT]:
        k.move(K_RIGHT,1)        
    elif keys[K_LEFT]:
        k.move(K_LEFT,1)
#    if keys[K_SPACE]:
#        bullet_list.append(k.shoot())
        
    Bullet.update_all(bullet_list)
    window.screen.blit(k.image,k.rect)
    pygame.display.flip()
    time.sleep(0.08)


pygame.quit()


#time.sleep(3)
#pygame.quit()
#        