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
WINDOWWIDTH=900


class Okno():
    """ Inicjalizuje obiekt okna gry """
    def __init__(self,window_width,window_height):
        pygame.init()
        self.elements_surf=[]
        self.elements_re=[]
        self.window_width=window_width
        self.window_height=window_height
        self.screen=pygame.display.set_mode((self.window_width,self.window_height),0,32)
        pygame.display.set_caption('Tankujemy')
        
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
    Tank_own_list=[]
    
    def __init__(self,screen,x=0,y=0,dir=0,speed_bullet=30,direction=0,speed_tank=15,power=1):
       pygame.sprite.Sprite.__init__(self)    
       self.image = pygame.image.load('czolg3.png')
       self.screen=screen
       self.speed_bullet=speed_bullet
       self.speed_tank=speed_tank
       self.rect = self.image.get_rect()
       self.rect = self.rect.move(x,y)
       self.direction = direction
       
       self.image,self.rect,self.direction = rotate_image(self.image,self.rect,self.direction)
       Tank_own.Tank_own_list.append(self)

    def shoot(self):
        Bullet(self.rect.copy(),self.direction,self.screen,self.speed_bullet,True)
        
    def move(self,key,op):
        old_center=self.rect.center
        
        if key == K_UP:
            if self.direction == 0:
                self.rect = self.rect.move(0,-self.speed_tank)
            else:
                # trzeba zaimplementowac odbijanie sie czolgu od scian
                self.image,self.rect,self.direction = rotate_image(self.image,self.rect,0,self.direction)
                self.rect=self.image.get_rect()
                self.rect.center=old_center
           
        elif key == K_RIGHT:
            if self.direction == 1:
                self.rect=self.rect.move(self.speed_tank,0)
            else:
                self.image,self.rect,self.direction = rotate_image(self.image,self.rect,1,self.direction)
                self.rect=self.image.get_rect()
                self.rect.center=old_center

        elif key == K_DOWN:
            if self.direction == 2:
                self.rect=self.rect.move(0,self.speed_tank)
            else:
                self.image,self.rect,self.direction = rotate_image(self.image,self.rect,2,self.direction)
                self.rect=self.image.get_rect()
                self.rect.center=old_center
        elif key == K_LEFT:
            if self.direction == 3:
                self.rect=self.rect.move(-self.speed_tank,0)
            else:
                self.image,self.rect,self.direction = rotate_image(self.image,self.rect,3,self.direction)
                self.rect=self.image.get_rect()
                self.rect.center=old_center
                
    def update(self):
        self.screen.blit(self.image,self.rect)
        
    def update_all():
        for l in range(len(Tank_own.Tank_own_list)-1,-1,-1):
             Tank_own.Tank_own_list[l].update()        
    def kill(self):
        # wyjdz do menu 
        pass
        
            
            
class Tank_enemy(pygame.sprite.Sprite):
    Tank_enemy_list=[]
    
    
    def __init__(self,screen,x=0,y=0,dir=0,speed_bullet=30,direction=0,speed_tank=5,power=1):
       pygame.sprite.Sprite.__init__(self)    
       self.image = pygame.image.load('czolg_wroga.png')
       self.screen=screen
       self.speed_bullet=speed_bullet
       self.speed_tank=speed_tank
       self.rect = self.image.get_rect()
       self.rect = self.rect.move(x,y)
       self.direction = direction
       
       self.image,self.rect,self.direction = rotate_image(self.image,self.rect,self.direction)
       Tank_enemy.Tank_enemy_list.append(self)
       
    def move(self):
        ch=np.random.choice(np.array([0,1,2,3]))
        old_center=self.rect.center
        if np.random.choice(np.array([False,True]),p=np.array([0.8,0.2])):
            self.image,self.rect,self.direction = rotate_image(self.image,self.rect,ch,self.direction)
            self.rect.center=old_center
            if ch == 0:
                self.rect = self.rect.move(0,-self.speed_tank)
            elif ch == 1:
                self.rect = self.rect.move(self.speed_tank,0)
            elif ch == 2:
                self.rect = self.rect.move(0,self.speed_tank)
            elif ch == 3:
                self.rect = self.rect.move(-self.speed_tank,0)
        else:
            if self.direction == 0:
                self.rect = self.rect.move(0,-self.speed_tank)
            elif self.direction == 1:
                self.rect = self.rect.move(self.speed_tank,0)
            elif self.direction == 2:
                self.rect = self.rect.move(0,self.speed_tank)
            elif self.direction == 3:
                self.rect = self.rect.move(-self.speed_tank,0)
            
    def shoot(self):
        Bullet(self.rect.copy(),self.direction,self.screen,self.speed_bullet,False)
            
    def update(self):
        
        self.move()
        if np.random.choice(np.array([False,True]),p=np.array([0.95,0.05])):
            self.shoot()
        self.screen.blit(self.image,self.rect)
    def update_all():
        for l in range(len(Tank_enemy.Tank_enemy_list)-1,-1,-1):
             Tank_enemy.Tank_enemy_list[l].update()        
    def kill(self):
        # jakis dzwiek
        # jakas grafika wybuchu moze
#        SCORE +=1
        pass
        
        
        
        
class Bullet(pygame.sprite.Sprite):
    bullet_list=[]
    SCORE=0
    
    def __init__(self,rect,direction,screen,speed_bullet,is_own):
        # Pamietac, ze self self wezmie pierwszego selfa, dlatego copy
        self.direction = direction
        self.screen=screen
        self.speed_bullet=speed_bullet
        self.is_own = is_own
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
        
        Bullet.bullet_list.append(self)
    
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
    def update_all():
        p=set()
        for l in range(len(Bullet.bullet_list)-1,-1,-1):
            x, y = Bullet.bullet_list[l].update()
            if x>WINDOWWIDTH or x<0 or y>WINDOWHEIGHT or y<0:
                p.add(l)
            for z in range(len(Tank_enemy.Tank_enemy_list)-1,-1,-1):
                if Tank_enemy.Tank_enemy_list[z].rect.left<=x<=Tank_enemy.Tank_enemy_list[z].rect.right and Tank_enemy.Tank_enemy_list[z].rect.top<=y<=Tank_enemy.Tank_enemy_list[z].rect.bottom:
                    p.add(l)
                    Tank_enemy.Tank_enemy_list[z].kill()
                    del Tank_enemy.Tank_enemy_list[z]
                    if Bullet.bullet_list[l].is_own == True:
                        Bullet.SCORE +=1
            for z in range(len(Tank_own.Tank_own_list)-1,-1,-1):
                if Tank_own.Tank_own_list[z].rect.left<=x<=Tank_own.Tank_own_list[z].rect.right and Tank_own.Tank_own_list[z].rect.top<=y<=Tank_own.Tank_own_list[z].rect.bottom:
                    p.add(l)
                    Tank_own.Tank_own_list[z].kill()
                    del Tank_own.Tank_own_list[z]
#            for z in range(len(Bullet.bullet_list)-1,-1,-1):
            for z in range(len(Bullet.bullet_list)):
                if z!=l:
                    if Bullet.bullet_list[z].rect.left<=x<=Bullet.bullet_list[z].rect.right and Bullet.bullet_list[z].rect.top<=y<=Bullet.bullet_list[z].rect.bottom:
                        p.add(z)
                        p.add(l)
        p = list(p)
        p.sort()
        p.reverse()
        for pe in p:
            del Bullet.bullet_list[pe]
                
def random_position():
    return (np.random.randint(0, WINDOWWIDTH - 99),np.random.randint(0, WINDOWHEIGHT - 99))

            
           
            
            
        
    

window=Okno(WINDOWWIDTH,WINDOWHEIGHT)
window.screen.fill((100,100,100))
mainloop=True
k=Tank_own(window.screen,direction=2,x=350,y=350)
rand_pos=random_position()
enemy=Tank_enemy(window.screen,direction=1,x=rand_pos[0],y=rand_pos[1])
Tank_own.update_all()
Tank_enemy.update_all()
#window.screen.blit(k.image,k.rect)
licznik=0
pygame.display.flip()
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
            elif event.key == K_SPACE:
                k.shoot()

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
    while (len(Tank_enemy.Tank_enemy_list)<5 or licznik<10):
        licznik+=1
        rand_pos=random_position()
        enemy=Tank_enemy(window.screen,direction=1,x=rand_pos[0],y=rand_pos[1])
        
        
    Bullet.update_all()
    Tank_enemy.update_all()
    Tank_own.update_all()
    pygame.display.flip()
    time.sleep(0.08)
    if len(Tank_own.Tank_own_list)==0:
        mainloop=False
print('what')
window.screen.fill((100,100,100))
print('yolo')
font = pygame.font.Font(None, 36)
text = font.render('Uzyskałeś wynik: {}'.format(Bullet.SCORE),1,(0,0,0))
#text = font.render('Uzyskałeś wynik: '+str(Bullet.SCORE),1,(0,0,0))
textpos = text.get_rect()
textpos.centerx = window.screen.get_rect().centerx
textpos.centery=window.screen.get_rect().centery
window.screen.blit(text, textpos)  
pygame.display.flip()
time.sleep(3)

pygame.quit()


#time.sleep(3)
#pygame.quit()
#        