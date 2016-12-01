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
import pickle

WINDOWHEIGHT=640
WINDOWWIDTH=832


class Okno():
    """ Inicjalizuje obiekt okna gry """
    list_text=[]
    PLAYER_NUMBER=1
    def __init__(self,window_width,window_height):
        WSAD=[K_LSHIFT,K_LCTRL,K_SPACE]
        ARROWS=[K_SPACE,K_RSHIFT,K_RCTRL]
        klawisze_strzal = pickle.load(open('settings','rb'))
        self.klawisz_wsad = int(klawisze_strzal[0]) 
        self.klawisz_arrows=int(klawisze_strzal[1]) 
#        self.klawisz_wsad=0
#        self.klawisz_arrows=0
        self.klawisz_strzal_1_wsad=WSAD[self.klawisz_wsad]
        self.klawisz_strzal_2_arrows=ARROWS[self.klawisz_arrows]
        
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
    def exit_window(self):
        loop=True
        otoczony=0
        Okno.list_text=[]
        self.screen.fill((100,100,100))
        self.napisz_text("Play once again",posy=-150,color=(255,255,255))
        self.napisz_text("Load game",posy=-70,color=(255,255,255))
        self.napisz_text("Exit game",posy=20,color=(255,255,255))
        otoczone_old=self.otocz_czolgami(Okno.list_text[otoczony])

        while loop:
            for event in pygame.event.get():
                # User presses QUIT-button.
                if event.type == QUIT:
                    pygame.quit()
                    
                elif event.type == KEYDOWN:
                    # User presses ESCAPE-Key
                    if event.key == K_ESCAPE:
                        pygame.quit()
                    elif event.key == K_RETURN:
                        loop = False
                    elif event.key == K_r:
                        self.GAME(PLAYERS_NUMBER)
                    elif event.key == K_UP and otoczony > 0:
                        otoczony-=1
                    elif event.key == K_DOWN and otoczony < len(Okno.list_text)-1:
                        otoczony+=1
            self.screen.fill((100,100,100),rect=otoczone_old[0])
            self.screen.fill((100,100,100),rect=otoczone_old[1])
            otoczone_old = self.otocz_czolgami(Okno.list_text[otoczony])
            pygame.display.flip()
        if otoczony == 0:
            self.GAME(Okno.PLAYER_NUMBER)
        elif otoczony == 1:
            self.save_game()
        elif otoczony == 2:
            pygame.quit()
            
    def pause_window(self):
        loop=True
        l=0
        otoczony=0
        Okno.list_text = []
        self.screen.fill((100,100,100))
        self.napisz_text("Continue game",posy=-100)
        self.napisz_text("Save game",posy=-30)
        self.napisz_text("Exit game without saving",posy=50)
        otoczone_old = self.otocz_czolgami(Okno.list_text[otoczony])
        pygame.display.flip()
        while loop:
            self.screen.fill((100,100,100),rect=otoczone_old[0])
            self.screen.fill((100,100,100),rect=otoczone_old[1])
            otoczone_old = self.otocz_czolgami(Okno.list_text[otoczony])
            pygame.display.flip()            
            for event in pygame.event.get():
                # User presses QUIT-button.
                if event.type == QUIT:
                    self.exit_window()
                    
                elif event.type == KEYDOWN:
                    # User presses ESCAPE-Key
                    if event.key == K_ESCAPE:
                        self.exit_window()
                    elif event.key == K_RETURN:
                        loop = False
                    elif event.key == K_UP and otoczony > 0:
                        otoczony-=1
                    elif event.key == K_DOWN and otoczony < len(Okno.list_text)-1:
                        otoczony+=1
        if otoczony == 0:
            pass
        elif otoczony == 1:
            self.save_game()
        elif otoczony == 2:
            pygame.quit()
            
                        
    def menu_window(self):
        loop=True

        otoczony = 0
        Okno.list_text=[]
        self.screen.fill((100,100,100))
        # konieczne rysowanie od góry do dołu
        self.napisz_text("NEW GAME",posy=-185)
        self.napisz_text("Load game",posy=-95)
        self.napisz_text("Tanks",posy=-10)
        self.napisz_text("Settings",posy=75)
        otoczone_old = self.otocz_czolgami(Okno.list_text[otoczony])
        while loop:
            self.screen.fill((100,100,100),rect=otoczone_old[0])
            self.screen.fill((100,100,100),rect=otoczone_old[1])
            otoczone_old = self.otocz_czolgami(Okno.list_text[otoczony])
            pygame.display.flip()
            for event in pygame.event.get():
                # User presses QUIT-button.
                if event.type == QUIT:
                    pygame.quit()
                    
                elif event.type == KEYDOWN:
                    # User presses ESCAPE-Key
                    if event.key == K_ESCAPE:
                        pygame.quit()
                    elif event.key == K_RETURN:
                        loop = False
                    elif event.key == K_UP and otoczony > 0:
                        otoczony-=1
                    elif event.key == K_DOWN and otoczony < len(Okno.list_text)-1:
                        otoczony+=1
        if otoczony == 0:
        # New game
            otoczony = 0          
            Okno.list_text = []
            self.screen.fill((100,100,100))
            # konieczne rysowanie od góry do dołu
            self.napisz_text("One player",posy=-60)
            self.napisz_text("Two players",posy=30)
            otoczone_old = self.otocz_czolgami(Okno.list_text[otoczony])
            loop = True
            while loop:
                self.screen.fill((100,100,100),rect=otoczone_old[0])
                self.screen.fill((100,100,100),rect=otoczone_old[1])
                otoczone_old = self.otocz_czolgami(Okno.list_text[otoczony])
                pygame.display.flip() 
                
                for event in pygame.event.get():
                    # User presses QUIT-button.
                    if event.type == QUIT:
                        pygame.quit()
                        
                    elif event.type == KEYDOWN:
                        # User presses ESCAPE-Key
                        if event.key == K_ESCAPE:
                            pygame.quit()
                        elif event.key == K_RETURN:
                            loop = False
                        elif event.key == K_UP and otoczony > 0:
                            otoczony-=1
                        elif event.key == K_DOWN and otoczony < len(Okno.list_text)-1:
                            otoczony+=1
            
                            
                            
            if otoczony == 0:
                # One player
                Okno.PLAYERS_NUMBER = 1
                self.GAME(Okno.PLAYERS_NUMBER)
                
            elif otoczony ==1:
                Okno.PLAYER_NUMBER = 2
                self.GAME(Okno.PLAYER_NUMBER)
        elif otoczony == 1:
            # Load game
            pass
        elif otoczony == 3:
            # Settings
            self.settings_window()

    def settings_window(self):
        loop = True        
        key_list_wsad=['LSHIFT','LCTRL','SPACE']
        key_list_arrows=['SPACE','RSHIFT','RCTRL']

#        klawisz_wsad=0
#        klawisz_arrows=0
        Okno.list_text=[]
        otoczony = 0
        self.screen.fill((100,100,100))
        self.napisz_text("Shoot key for player 1. (WSAD): ",posy=-100,posx=-100,size=30)
        self.napisz_text("Shoot key for player 2. (arrows): ",posy=-30,posx=-100,size=3)
        self.napisz_text(key_list_wsad[self.klawisz_wsad%len(key_list_wsad)],posy=-100,posx=0,size=30)
        self.napisz_text(key_list_arrows[self.klawisz_arrows%len(key_list_arrows)],posy=-30,posx=0,size=30)
        pygame.display.flip()

        while loop:
            
            Okno.list_text=[]
            self.screen.fill((100,100,100))
            self.napisz_text("Shoot key for player 1. (WSAD): ",posy=-100,posx=-100,size=20)
            self.napisz_text("Shoot key for player 2. (arrows): ",posy=-30,posx=-100,size=20)
            if otoczony ==0:
                self.napisz_text(key_list_wsad[self.klawisz_wsad%len(key_list_wsad)],posy=-100,posx=100,size=20,color=(255,255,0))
                self.napisz_text(key_list_arrows[self.klawisz_arrows%len(key_list_arrows)],posy=-30,posx=100,size=20)
            else:
                self.napisz_text(key_list_wsad[self.klawisz_wsad%len(key_list_wsad)],posy=-100,posx=100,size=20)
                self.napisz_text(key_list_arrows[self.klawisz_arrows%len(key_list_arrows)],posy=-30,posx=100,size=20,color=(255,255,0))                    
            
            pygame.display.flip() 
            
            for event in pygame.event.get():
                # User presses QUIT-button.
                if event.type == QUIT:
                    pygame.quit()
                    
                elif event.type == KEYDOWN:
                    # User presses ESCAPE-Key
                    if event.key == K_ESCAPE:
                        pygame.quit()
                    elif event.key == K_RETURN:
                        loop = False
                    elif event.key == K_UP and otoczony > 0:
                        otoczony-=1
                    elif event.key == K_DOWN and otoczony < len(Okno.list_text)-1:
                        otoczony+=1
                    elif event.key == K_RIGHT:
                        if otoczony == 0:
                            self.klawisz_wsad+=1
                        elif otoczony ==1:
                            self.klawisz_arrows +=1
                    elif event.key == K_LEFT:
                        if otoczony == 0:
                            self.klawisz_wsad-=1
                        elif otoczony ==1:
                            self.klawisz_arrows -=1
        if self.klawisz_arrows%len(key_list_arrows) == 0 and self.klawisz_wsad%len(key_list_wsad) == 2:
            self.screen.fill((100,100,100))
            self.napisz_text("The same key for both players :/ ")
            pygame.display.flip()
            time.sleep(2)
            self.settings_window()
        WSAD=[K_LSHIFT,K_LCTRL,K_SPACE]
        ARROWS=[K_SPACE,K_RSHIFT,K_RCTRL]
        self.klawisz_wsad=self.klawisz_wsad % len(key_list_wsad)
        self.klawisz_arrows=self.klawisz_arrows % len(key_list_arrows)
        self.klawisz_strzal_1_wsad=WSAD[self.klawisz_wsad]
        self.klawisz_strzal_2_arrows=ARROWS[self.klawisz_arrows]
        pickle.dump([str(self.klawisz_wsad),str(self.klawisz_arrows)],open("settings",'wb'))
        self.menu_window()
            

                        
    def napisz_text(self,string,posx=0,posy=0, color=(255,255,255),size=36):
        """ Domyślnie na środku """
        
        font = pygame.font.SysFont("verdana", size)
        text = font.render(string,1,color)
        #text = font.render('Uzyskałeś wynik: '+str(Bullet.SCORE),1,(0,0,0))
        textpos = text.get_rect()
        textpos.centerx = window.screen.get_rect().centerx+posx
        textpos.centery=window.screen.get_rect().centery+posy
        Okno.list_text.append(textpos)
        self.screen.blit(text, textpos)
    def save_game(self):
        pass
    
    
    
    
    
    def load_game(self,filename):
        pass
        
        
        
        
        
        
    def otocz_czolgami(self,rect):
        image_l = pygame.image.load('tan32a.png')
        image_r = pygame.image.load("tan32.png")
        rect_r=image_r.get_rect()
        rect_l=image_l.get_rect()
        rect_r.center=rect.center
        rect_l.center=rect.center
        rect_r.left=rect.right+20
        rect_l.right=rect.left-20
        self.screen.blit(image_l,rect_l)
        self.screen.blit(image_r,rect_r)
        return rect_r,rect_l
                
    def check_event(self):
        still_play=True
        for event in pygame.event.get():
            # User presses QUIT-button.
            if event.type == QUIT:
                still_play = False 
                
            elif event.type == KEYDOWN:
                # User presses ESCAPE-Key
                if event.key == K_ESCAPE:
                    still_play = False
        return still_play
    def GAME (self,PLAYERS_NUMBER):
        # Main game!!!
        if PLAYERS_NUMBER ==1:
            mainloop=True
            for i in range(3,0,-1):
                self.screen.fill((100,100,100))
                self.napisz_text(str(i),size=50)
                pygame.display.flip()
                time.sleep(0.7)
            player_one=Tank_own(self.screen,1,direction=2,x=350,y=350)
            rand_pos=random_position()
            enemy=Tank_enemy(self.screen,direction=1,x=rand_pos[0],y=rand_pos[1])
            Tank_own.update_all()
            Tank_enemy.update_all()
            pygame.display.flip()
            
            while mainloop:
                window.screen.fill((100,100,100))
                # Do not go faster than this framerate.
            
                for event in pygame.event.get():
                    # User presses QUIT-button.
                    if event.type == QUIT:
                        self.pause_window()
                        
                    elif event.type == KEYDOWN:
                        # User presses ESCAPE-Key
                        if event.key == K_ESCAPE:
                            self.pause_window()
                        elif event.key == K_UP or event.key == K_RIGHT or event.key == K_DOWN or event.key == K_LEFT:
                            player_one.move(event.key)
                        elif event.key == K_SPACE:
                            player_one.shoot()
                        elif event.key == K_p:
                            self.pause_window()
            
                keys = pygame.key.get_pressed()  #checking pressed keys
                if keys[K_UP]:
                    player_one.move(K_UP)
                elif keys[K_DOWN]:
                    player_one.move(K_DOWN)
                elif keys[K_RIGHT]:
                    player_one.move(K_RIGHT)        
                elif keys[K_LEFT]:
                    player_one.move(K_LEFT)
                while (len(Tank_enemy.Tank_enemy_list))<5:
                    rand_pos=random_position()
                    enemy=Tank_enemy(window.screen,direction=1,x=rand_pos[0],y=rand_pos[1])
                    
                    
                Bullet.update_all()
                Tank_enemy.update_all()
                Tank_own.update_all()
                pygame.display.flip()
                time.sleep(0.05)
                if len(Tank_own.Tank_own_list)==0:
                    mainloop=False
            self.exit_window()
            
        elif Okno.PLAYER_NUMBER ==2:
            mainloop=True
            for i in range(3,0,-1):
                self.screen.fill((100,100,100))
                self.napisz_text(str(i),size=50)
                pygame.display.flip()
                time.sleep(0.7)
            player_one=Tank_own(self.screen,1,direction=2,x=350,y=350)
            player_two=Tank_own(self.screen,2,direction=3,x=50,y=550)
            rand_pos=random_position()
            enemy=Tank_enemy(self.screen,direction=1,x=rand_pos[0],y=rand_pos[1])
            Tank_own.update_all()
            Tank_enemy.update_all()
            pygame.display.flip()
            
            while mainloop:
                window.screen.fill((100,100,100))
                # Do not go faster than this framerate.
            
                for event in pygame.event.get():
                    # User presses QUIT-button.
                    if event.type == QUIT:
                        self.pause_window()
                        
                    elif event.type == KEYDOWN:
                        # User presses ESCAPE-Key
                        if event.key == K_ESCAPE:
                            self.pause_window()
                        #### player two WSAD
                        elif (event.key == K_UP or event.key == K_RIGHT or event.key == K_DOWN or event.key == K_LEFT) and player_two in Tank_own.Tank_own_list :
                            player_two.move(event.key)
                        #### player one UP,DOWN,RIGHT,LEFT
                        elif event.key == (K_w or event.key == K_d or event.key == K_s or event.key == K_a) and player_one in Tank_own.Tank_own_list:
                            player_one.move(event.key)                            
                        elif event.key == self.klawisz_strzal_1_wsad and player_one in Tank_own.Tank_own_list:
                            player_one.shoot()
                        elif event.key == self.klawisz_strzal_2_arrows and player_two in Tank_own.Tank_own_list:
                            player_two.shoot()
                        elif event.key == K_p:
                            self.pause_window()
            
                keys = pygame.key.get_pressed()  #checking pressed keys
                if keys[K_UP] and player_two in Tank_own.Tank_own_list:
                    player_two.move(K_UP)
                elif keys[K_DOWN] and player_two in Tank_own.Tank_own_list:
                    player_two.move(K_DOWN)
                elif keys[K_RIGHT] and player_two in Tank_own.Tank_own_list:
                    player_two.move(K_RIGHT)        
                elif keys[K_LEFT] and player_two in Tank_own.Tank_own_list:
                    player_two.move(K_LEFT)
                elif keys[K_w] and player_one in Tank_own.Tank_own_list:
                    player_one.move(K_w)
                elif keys[K_s] and player_one in Tank_own.Tank_own_list:
                    player_one.move(K_s)
                elif keys[K_d] and player_one in Tank_own.Tank_own_list:
                    player_one.move(K_d)        
                elif keys[K_a] and player_one in Tank_own.Tank_own_list:
                    player_one.move(K_a)
                while (len(Tank_enemy.Tank_enemy_list))<5:
                    rand_pos=random_position()
                    enemy=Tank_enemy(window.screen,direction=1,x=rand_pos[0],y=rand_pos[1])
                    
                    
                Bullet.update_all()
                Tank_enemy.update_all()
                Tank_own.update_all()
                pygame.display.flip()
                time.sleep(0.05)
                if len(Tank_own.Tank_own_list)==0:
                    mainloop=False
            self.exit_window()            

        
            

            
class Tank_own(pygame.sprite.Sprite):
    Tank_own_list=[]
    Score=0
    
    def __init__(self,screen,player_number,x=0,y=0,dir=0,speed_bullet=15,direction=0,speed_tank=8,power=1):
       pygame.sprite.Sprite.__init__(self)    
       self.image = pygame.image.load('czoligs1.png')
       self.screen=screen
       self.speed_bullet=speed_bullet
       self.speed_tank=speed_tank
       self.rect = self.image.get_rect()
       self.rect = self.rect.move(x,y)
       self.direction = direction
       self.player_number = player_number
       
       self.image,self.rect,self.direction = rotate_image(self.image,self.rect,self.direction)
       Tank_own.Tank_own_list.append(self)

    def shoot(self):
        Bullet(self.rect.copy(),self.direction,self.screen,self.speed_bullet,self.player_number)
        
    def move(self,key):
        """
        Wykonuje ruch czołgu w zależności od wciśniętego klawisza 
        """
        old_center=self.rect.center
        
        if (key == K_UP or key == K_w) and self.rect.top >= self.speed_tank:
            if self.direction == 0 :
                self.rect = self.rect.move(0,-self.speed_tank)
            else:
                self.image,self.rect,self.direction = rotate_image(self.image,self.rect,0,self.direction)
                self.rect=self.image.get_rect()
                self.rect.center=old_center
           
        elif (key == K_RIGHT or key == K_d) and (WINDOWWIDTH-self.rect.right) >= self.speed_tank:
            if self.direction == 1:
                self.rect=self.rect.move(self.speed_tank,0)
            else:
                self.image,self.rect,self.direction = rotate_image(self.image,self.rect,1,self.direction)
                self.rect=self.image.get_rect()
                self.rect.center=old_center

        elif (key == K_DOWN or key == K_s) and (WINDOWHEIGHT-self.rect.bottom) >= self.speed_tank:
            if self.direction == 2: 
                self.rect=self.rect.move(0,self.speed_tank)
            else:
                self.image,self.rect,self.direction = rotate_image(self.image,self.rect,2,self.direction)
                self.rect=self.image.get_rect()
                self.rect.center=old_center
        elif (key == K_LEFT or key == K_a) and self.rect.left >= self.speed_tank:
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
    
    
    def __init__(self,screen,x=0,y=0,dir=0,speed_bullet=15,direction=0,speed_tank=4,power=1):
       pygame.sprite.Sprite.__init__(self)    
       self.image = pygame.image.load('czoligs2.png')
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
            if self.direction == 0 and self.rect.top >= self.speed_tank:
                self.rect = self.rect.move(0,-self.speed_tank)
            elif self.direction == 1 and (WINDOWWIDTH - self.rect.right) >= self.speed_tank:
                self.rect = self.rect.move(self.speed_tank,0)
            elif self.direction == 2 and (WINDOWHEIGHT-self.rect.bottom) >= self.speed_tank:
                self.rect = self.rect.move(0,self.speed_tank)
            elif self.direction == 3 and self.rect.left >= self.speed_tank:
                self.rect = self.rect.move(-self.speed_tank,0)
            
    def shoot(self):
        Bullet(self.rect.copy(),self.direction,self.screen,self.speed_bullet,3)
            
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
    
    def __init__(self,rect,direction,screen,speed_bullet,player_number):
        # Pamietac, ze self self wezmie pierwszego selfa, dlatego copy
        self.direction = direction
        self.screen=screen
        self.speed_bullet=speed_bullet
#        self.image=pygame.image.load()
        self.image = pygame.Surface([5,10])
        self.image.fill((255,255,0)) 
        self.rect=rect
        self.player_number = player_number
        if self.direction == 0:
            self.rect.y-=35
        elif self.direction == 1:
            self.rect.x+=35
        elif self.direction == 2:
            self.rect.y+=35
        elif self.direction == 3:
            self.rect.x-=35
            
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
                    if Bullet.bullet_list[l].player_number == 1 or Bullet.bullet_list[l].player_number == 2:
                        Tank_enemy.Tank_enemy_list[z].kill()
                        del Tank_enemy.Tank_enemy_list[z]
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
    
            
           
            
            
        
    

window=Okno(WINDOWWIDTH,WINDOWHEIGHT)
window.menu_window()
