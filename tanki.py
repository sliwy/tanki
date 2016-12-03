#!/usr/bin/env/python
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 18:22:54 2016

@author: maciej
"""
import pygame

from pygame.locals import *
import time
import copy
import pickle
import numpy as np
from MapElement import *

WINDOWHEIGHT=640
WINDOWWIDTH=832


class Okno():
    """ Inicjalizuje obiekt okna gry """
    list_text=[]
    PLAYER_NUMBER=1
    liczba_gier=0
    def __init__(self,window_width,window_height):
        WSAD=[K_LSHIFT,K_LCTRL,K_SPACE]
        ARROWS=[K_SPACE,K_RSHIFT,K_RCTRL]
        klawisze_strzal = pickle.load(open('settings','rb'))
#        self.levels=pickle.load(open('level_max','rb'))
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
        self.rect=self.screen.get_rect()
        self.level_number=0
        pygame.display.set_caption('Tankujemy')

    def exit_window(self):
        loop=True
        if Okno.PLAYER_NUMBER ==1:
            self.screen.fill((100,100,100))
            self.napisz_text("You lost and linux died :( ",posy=-80)            
            self.napisz_text("Player one score: "+str(Tank_own.Score_1),posy=0)
            pygame.display.flip()
            time.sleep(2)
        else:
            self.screen.fill((100,100,100))
            self.napisz_text("You lost and linux died :( ",posy=-100)
            self.napisz_text("Player one score: "+str(Tank_own.Score_1),posy=-20)
            self.napisz_text("Player two score: "+str(Tank_own.Score_2),posy=60)
            pygame.display.flip()
            time.sleep(2)
        otoczony=0
        Okno.list_text=[]
        self.screen.fill((100,100,100))
        self.napisz_text("Play once again",posy=-70,color=(255,255,255))
#        self.napisz_text("Load game",posy=-70,color=(255,255,255))
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

            pygame.quit()
            
    def pause_window(self):
        loop=True
        l=0
        otoczony=0
        Okno.list_text = []
        self.screen.fill((100,100,100))
        self.napisz_text("Reset game",posy=-100)
        self.napisz_text("Continue game",posy=-30)
#        self.napisz_text("Save game",posy=-30)
        self.napisz_text("Exit game",posy=50)
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
            self.GAME(Okno.PLAYER_NUMBER)
        if otoczony == 1:
            pass
        elif otoczony == 2:
            pygame.quit()
            
                        
    def menu_window(self):
        loop=True

        otoczony = 0
        Okno.list_text=[]
        self.screen.fill((100,100,100))
        # konieczne rysowanie od góry do dołu
        self.napisz_text("NEW GAME",posy=-60)
#        self.napisz_text("Load game",posy=-95)
#        self.napisz_text("Tanks",posy=-10)
        self.napisz_text("Settings",posy=25)
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
        levels=[Map.level1,Map.level2,Map.level3,Map.level4]
        # Main game!!!
        Tank_own.clear()
        Tank_enemy.clear()
        Bullet.clear()
        mapka=Map(self)
        mapka.clear()
        mapka.create_ring()
        levels[self.level_number](mapka)

        if PLAYERS_NUMBER ==1:
            mainloop=True
            for i in range(3,0,-1):
                self.screen.fill((100,100,100))
                self.napisz_text(str(i),size=50)
                pygame.display.flip()
                time.sleep(0.7)
            Tank_own(self.screen,mapka,1,direction=0)
            Tank_own.update_all()
            Tank_enemy.update_all(mapka)
            mapka.draw_all()
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
                            Tank_own.Tank_own_list[0].move(event.key,mapka)
                        elif event.key == K_SPACE:
                            Tank_own.Tank_own_list[0].shoot()
                        elif event.key == K_p:
                            self.pause_window()
            
                keys = pygame.key.get_pressed()  #checking pressed keys
                if keys[K_UP]:
                    Tank_own.Tank_own_list[0].move(K_UP,mapka)
                elif keys[K_DOWN]:
                    Tank_own.Tank_own_list[0].move(K_DOWN,mapka)
                elif keys[K_RIGHT]:
                    Tank_own.Tank_own_list[0].move(K_RIGHT,mapka)        
                elif keys[K_LEFT]:
                    Tank_own.Tank_own_list[0].move(K_LEFT,mapka)
                while (len(Tank_enemy.Tank_enemy_list))<5:
                    rand_pos=random_position(mapka,Tank_enemy.Tank_enemy_rect_list,Tank_own.Tank_own_rect_list)
                    enemy=Tank_enemy(window.screen,mapka,rand_pos[0],rand_pos[1])


                Bullet.update_all(mapka)
                Tank_enemy.update_all(mapka)
                Tank_own.update_all()
                mapka.draw_all()  
                pygame.display.flip()
                time.sleep(0.05)
                if sum([Tank_own.Score_1,Tank_own.Score_2])>12:
                    self.level_number+=1
                    if self.level_number == 4:
                        self.screen.fill((100,100,100))
                        self.napisz_text("Dzięki za grę. Sprawdzaj aktualizacje :)")
                        pygame.display.flip()
                        time.sleep(5)
                        pygame.quit()
                if len(Tank_own.Tank_own_list)==0:
                    mainloop=False

            self.exit_window()
            
        elif Okno.PLAYER_NUMBER ==2:

            levels=[Map.level1,Map.level2,Map.level3,Map.level4]
            Tank_own.clear()
            Tank_enemy.clear()
            Bullet.clear()
            mapka=Map(self)
            mapka.clear()
            mapka.create_ring()
            levels[self.level_number](mapka)
            mainloop=True
            for i in range(3,0,-1):
                self.screen.fill((100,100,100))
                self.napisz_text(str(i),size=50)
                pygame.display.flip()
                time.sleep(0.7)
            player_one=Tank_own(self.screen,mapka,1,direction=0)
            player_two=Tank_own(self.screen,mapka,2,direction=0)

            Tank_own.update_all()
            Tank_enemy.update_all(mapka)
            mapka.draw_all()
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
                            player_two.move(event.key,mapka)
                        #### player one UP,DOWN,RIGHT,LEFT
                        elif event.key == (K_w or event.key == K_d or event.key == K_s or event.key == K_a) and player_one in Tank_own.Tank_own_list:
                            player_one.move(event.key,mapka)                            
                        elif event.key == self.klawisz_strzal_1_wsad and player_one in Tank_own.Tank_own_list:
                            player_one.shoot()
                        elif event.key == self.klawisz_strzal_2_arrows and player_two in Tank_own.Tank_own_list:
                            player_two.shoot()
                        elif event.key == K_p:
                            self.pause_window()
            
                keys = pygame.key.get_pressed()  #checking pressed keys
                if keys[K_UP] and player_two in Tank_own.Tank_own_list:
                    player_two.move(K_UP,mapka)
                elif keys[K_DOWN] and player_two in Tank_own.Tank_own_list:
                    player_two.move(K_DOWN,mapka)
                elif keys[K_RIGHT] and player_two in Tank_own.Tank_own_list:
                    player_two.move(K_RIGHT,mapka)        
                elif keys[K_LEFT] and player_two in Tank_own.Tank_own_list:
                    player_two.move(K_LEFT,mapka)
                if keys[K_w] and player_one in Tank_own.Tank_own_list:
                    player_one.move(K_w,mapka)
                elif keys[K_s] and player_one in Tank_own.Tank_own_list:
                    player_one.move(K_s,mapka)
                elif keys[K_d] and player_one in Tank_own.Tank_own_list:
                    player_one.move(K_d,mapka)        
                elif keys[K_a] and player_one in Tank_own.Tank_own_list:
                    player_one.move(K_a,mapka)
                while (len(Tank_enemy.Tank_enemy_list))<5:
                    rand_pos=random_position(mapka,Tank_enemy.Tank_enemy_rect_list,Tank_own.Tank_own_rect_list)
                    enemy=Tank_enemy(window.screen,mapka,rand_pos[0],rand_pos[1])
                    
                    
                Bullet.update_all(mapka)
                Tank_enemy.update_all(mapka)
                Tank_own.update_all()
                mapka.draw_all()
                pygame.display.flip()
                time.sleep(0.05)
                if sum([Tank_own.Score_1,Tank_own.Score_2])>16:
                    self.level_number+=1
                    if self.level_number == 4:
                        self.screen.fill((100,100,100))
                        self.napisz_text("Dzięki za grę. Sprawdzaj aktualizacje :)")
                        time.sleep(5)
                        pygame.quit()
                    self.next_level()
                if len(Tank_own.Tank_own_list)==0:
                    mainloop=False
            self.exit_window()
    def next_level(self):
        self.screen.fill((100,100,100))
        self.napisz_text("Congratulations!!! You reached next level")
        pygame.display.flip()
        time.sleep(2)
        self.GAME(Okno.PLAYER_NUMBER)
        
            
class Tank_own(pygame.sprite.Sprite):
    Tank_own_list=[]
    Tank_own_rect_list=[]
    Score_1=0
    Score_2=0
    strong=False
    strong_licznik=101
    def __init__(self,screen,mapa,player_number,speed_bullet=15,direction=0,speed_tank=8,power=1):
       pygame.sprite.Sprite.__init__(self)
       if player_number == 1:
           self.image = pygame.image.load('czoligs1.png')
           self.image_strong=pygame.image.load('czoligs1och.png')
       else: 
           self.image = pygame.image.load('czoligs2.png')
           self.image_strong = pygame.image.load('czoligs2och.png')
       self.screen=screen
       self.mapa = mapa
       self.speed_bullet=speed_bullet
       self.speed_tank=speed_tank
       self.rect = self.image.get_rect()
       rand_pos=random_position1(self.mapa,Tank_enemy.Tank_enemy_rect_list,Tank_own.Tank_own_rect_list)
       
       self.rect = self.rect.move(rand_pos[0],rand_pos[1])
       self.direction = direction
       self.player_number = player_number
       self.life=3
       self.image,self.rect,self.direction = rotate_image(self.image,self.rect,self.direction)
       self.water=False
       self.sound_kill=pygame.mixer.Sound('failure.wav')
       self.sound_shoot=pygame.mixer.Sound('strzal.wav')

       Tank_own.Tank_own_list.append(self)
       Tank_own.Tank_own_rect_list.append(self.rect)
       
    def shoot(self):
        Bullet(self.rect.copy(),self.direction,self.screen,self.speed_bullet,self.player_number)
        self.sound_shoot.play()
        
    def move(self,key,mapa):
        """
        Wykonuje ruch czołgu w zależności od wciśniętego klawisza 
        """
        list_bez=[i for i in Tank_own.Tank_own_list if i !=self.rect]      
        list_bez=list_bez+Tank_enemy.Tank_enemy_rect_list
        ind = Tank_own.Tank_own_rect_list.index(self.rect)
        old_center=self.rect.center
        
        if (key == K_UP or key == K_w) :
            if self.direction == 0 and mapa.check_if_move(self,0,self.water) and self.rect.move(0,-self.speed_tank).collidelist(list_bez)==-1 and self.rect.top >= self.speed_tank:
                self.rect = self.rect.move(0,-self.speed_tank)
            else:
                self.image,self.rect,self.direction = rotate_image(self.image,self.rect,0,self.direction)
                self.rect=self.image.get_rect()
                self.rect.center=old_center
           
        elif (key == K_RIGHT or key == K_d):
            if self.direction == 1 and mapa.check_if_move(self,1,self.water) and self.rect.move(self.speed_tank,0).collidelist(list_bez)==-1  and (WINDOWWIDTH-self.rect.right) >= self.speed_tank:
                self.rect=self.rect.move(self.speed_tank,0)
            else:
                self.image,self.rect,self.direction = rotate_image(self.image,self.rect,1,self.direction)
                self.rect=self.image.get_rect()
                self.rect.center=old_center

        elif (key == K_DOWN or key == K_s):
            if self.direction == 2 and mapa.check_if_move(self,2,self.water) and self.rect.move(0,self.speed_tank).collidelist(list_bez)==-1  and (WINDOWHEIGHT-self.rect.bottom) >= self.speed_tank: 
                self.rect=self.rect.move(0,self.speed_tank)
            else:
                self.image,self.rect,self.direction = rotate_image(self.image,self.rect,2,self.direction)
                self.rect=self.image.get_rect()
                self.rect.center=old_center
        elif (key == K_LEFT or key == K_a) :
            if self.direction == 3 and mapa.check_if_move(self,3,self.water) and self.rect.move(-self.speed_tank,0).collidelist(list_bez)==-1 and self.rect.left >= self.speed_tank:
                self.rect=self.rect.move(-self.speed_tank,0)
            else:
                self.image,self.rect,self.direction = rotate_image(self.image,self.rect,3,self.direction)
                self.rect=self.image.get_rect()
                self.rect.center=old_center
        Tank_own.Tank_own_rect_list[ind]=self.rect       
                
    def update(self):
        sound_bonus= pygame.mixer.Sound('bonus.wav')
        i = self.rect.collidelist(self.mapa.bonus_list_rect)
        if i != -1 :
            sound_bonus.play()
            if self.mapa.bonus_list[i].typ == 5:
                # zycie
                if self.life!=3:
                    self.life+=1

            elif self.mapa.bonus_list[i].typ == 4:
                # nurkowanie
                self.water=True
            elif self.mapa.bonus_list[i].typ == 3:
                # gwiazdka

                self.mapa.umocnij()

            elif self.mapa.bonus_list[i].typ == 2:
                Tank_own.strong=True
                Tank_own.strong_licznik=0

            elif self.mapa.bonus_list[i].typ == 1:
                Tank_enemy.zastygnij()
#                sound_timer=pygame.mixer.Sound('zegar.wav')
#                sound_timer.play()

            elif self.mapa.bonus_list[i].typ == 0:
                self.sound_granat=pygame.mixer.Sound('wybuch.wav')
                self.sound_granat.play()
                Tank_enemy.kill_all(self.player_number)

            self.mapa.del_bonus(self.mapa.bonus_list[i])
        
        if self.player_number == 1:

            self.screen.blit(pygame.image.load('zycia'+str(self.life)+'.png'),(0,0))
        elif self.player_number == 2:
            self.screen.blit(pygame.image.load('zycia'+str(self.life)+'.png'),(WINDOWWIDTH-130,0))
        if Tank_own.strong:
            self.screen.blit(rotate_tank(self.image_strong,self.direction),self.rect)
        else:
            self.screen.blit(self.image,self.rect)
        
    def update_all():
        if Tank_own.strong_licznik<=99:
            Tank_own.strong_licznik+=1
            for l in range(len(Tank_own.Tank_own_list)-1,-1,-1):
                 Tank_own.Tank_own_list[l].update()    
        elif Tank_own.strong_licznik==100:
            Tank_own.strong=False
            for l in range(len(Tank_own.Tank_own_list)-1,-1,-1):
                 Tank_own.Tank_own_list[l].update() 
        else:
            for l in range(len(Tank_own.Tank_own_list)-1,-1,-1):
                 Tank_own.Tank_own_list[l].update() 
    def kill(self):
        # wyjdz do menu
        if not Tank_own.strong:
            ind = Tank_own.Tank_own_rect_list.index(self.rect)
            self.sound_kill.play()
            self.life-=1
            if self.life>0:
               self.rect = self.image.get_rect()
               places=np.array([WINDOWWIDTH/2+64,WINDOWWIDTH/2-64])
               x=np.random.randint(30,WINDOWWIDTH-70)       
               while self.rect.move(x,self.screen.get_rect().bottom-64).collidelist(self.mapa.list_elements_colision)!=-1 or  self.rect.move(x,self.screen.get_rect().bottom-64).collidelist(self.Tank_own_rect_list)!=-1 or self.rect.move(x,self.screen.get_rect().bottom-64).collidelist(Tank_enemy.Tank_enemy_rect_list)!=-1:
                   x=np.random.randint(30,WINDOWWIDTH-70)
               self.rect = self.rect.move(x,self.screen.get_rect().bottom-64)
               Tank_own.Tank_own_rect_list[ind]=self.rect 
            else:
                del Tank_own.Tank_own_list[Tank_own.Tank_own_list.index(self)]
                del Tank_own.Tank_own_rect_list[Tank_own.Tank_own_rect_list.index(self.rect)]
    def clear():
        Tank_own.Tank_own_list=[]
        Tank_own.Tank_own_rect_list=[]
        Tank_own.Score_1=0
        Tank_own.Score_2=0
            
            
class Tank_enemy(pygame.sprite.Sprite):
    Tank_enemy_list=[]
    Tank_enemy_rect_list=[]
    zas=101
    
    def __init__(self,screen,mapa,x=0,y=0,speed_bullet=15,direction=0,speed_tank=4,power=1):
       pygame.sprite.Sprite.__init__(self)    
       self.image = pygame.image.load('czoligs3.png')
       self.screen=screen
       self.speed_bullet=speed_bullet
       self.speed_tank=speed_tank
       self.rect = self.image.get_rect()
       self.rect = self.rect.move(x,y)
       self.direction = direction
       self.mapa=mapa
       self.wybuch=pygame.image.load('wybuch.png')
       self.zs=101
       self.sound_kill=pygame.mixer.Sound('wybuch2.wav')
       self.image,self.rect,self.direction = rotate_image(self.image,self.rect,self.direction)
       Tank_enemy.Tank_enemy_list.append(self)
       Tank_enemy.Tank_enemy_rect_list.append(self.rect)
      
    def move(self,mapa):
        ch=np.random.choice(np.array([0,1,2,3]),p=np.array([0.1,0.2,0.5,0.2]))
        ind = Tank_enemy.Tank_enemy_rect_list.index(self.rect)
        old_center=self.rect.center
        list_bez=[i for i in Tank_enemy.Tank_enemy_list if i !=self.rect]
        list_bez=list_bez+Tank_own.Tank_own_rect_list
        if np.random.choice(np.array([False,True]),p=np.array([0.8,0.2])):
            self.image,self.rect,self.direction = rotate_image(self.image,self.rect,ch,self.direction)
            self.rect.center=old_center

        else:
            if self.direction == 0 and mapa.check_if_move(self,0,False) and self.rect.top >= self.speed_tank and self.rect.move(0,-self.speed_tank).collidelist(list_bez)==-1:
                self.rect = self.rect.move(0,-self.speed_tank)
            elif self.direction == 1 and mapa.check_if_move(self,1,False) and (WINDOWWIDTH - self.rect.right) >= self.speed_tank and self.rect.move(self.speed_tank,0).collidelist(list_bez)==-1:
                self.rect = self.rect.move(self.speed_tank,0)
            elif self.direction == 2 and mapa.check_if_move(self,2,False) and (WINDOWHEIGHT-self.rect.bottom) >= self.speed_tank and self.rect.move(0,self.speed_tank).collidelist(list_bez)==-1:
                self.rect = self.rect.move(0,self.speed_tank)
            elif self.direction == 3 and mapa.check_if_move(self,3,False) and self.rect.left >= self.speed_tank and self.rect.move(-self.speed_tank,0).collidelist(list_bez)==-1:
                self.rect = self.rect.move(-self.speed_tank,0)
        Tank_enemy.Tank_enemy_rect_list[ind]=self.rect
                
    def shoot(self):
        Bullet(self.rect.copy(),self.direction,self.screen,self.speed_bullet,3)
    
    def zastygnij():
        Tank_enemy.zas=0
            
    def update(self,mapa,log):
        if log:
            self.move(mapa)
            if np.random.choice(np.array([False,True]),p=np.array([0.85,0.15])):
                self.shoot()
        self.screen.blit(self.image,self.rect)
    def update_all(mapa):
        if Tank_enemy.zas <=100:
            Tank_enemy.zas+=1
            for l in range(len(Tank_enemy.Tank_enemy_list)-1,-1,-1):
                 Tank_enemy.Tank_enemy_list[l].update(mapa,False) 
        else:
            for l in range(len(Tank_enemy.Tank_enemy_list)-1,-1,-1):
                 Tank_enemy.Tank_enemy_list[l].update(mapa,True)        
    def kill(self,player_number):
        # jakis dzwiek
        # jakas grafika wybuchu moze
        if player_number == 1:
            Tank_own.Score_1 +=1
        else:
            Tank_own.Score_2 +=1
        k=np.array([True,False])
        self.screen.blit(self.wybuch,self.rect)
        self.sound_kill.play()
        if np.random.choice(k,p=np.array([0.4,0.6])):
            bon=np.array([Stoper,Gwiazdka,Nurkowanie,Granat,Pancerz,Serduszko])
            bonus=np.random.choice(bon)
            bonus(self.mapa,self.rect.x,self.rect.y)
    def clear():
        Tank_enemy.Tank_enemy_list=[]
        Tank_enemy.Tank_enemy_rect_list=[]     
    def kill_all(player_number):
        for el in Tank_enemy.Tank_enemy_list:
            el.kill(player_number)
            del Tank_enemy.Tank_enemy_list[Tank_enemy.Tank_enemy_list.index(el)]
        for re in Tank_enemy.Tank_enemy_rect_list:
            del Tank_enemy.Tank_enemy_rect_list[Tank_enemy.Tank_enemy_rect_list.index(re)]
        
        
        
        
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
    def update_all(mapa):
        p=set()
        for l in range(len(Bullet.bullet_list)-1,-1,-1):
            x, y = Bullet.bullet_list[l].update()
            if x>WINDOWWIDTH or x<0 or y>WINDOWHEIGHT or y<0:
                p.add(l)
            for z in range(len(Tank_enemy.Tank_enemy_list)-1,-1,-1):
                if Tank_enemy.Tank_enemy_list[z].rect.collidepoint(x,y):
                    p.add(l)
                    if Bullet.bullet_list[l].player_number == 1 or Bullet.bullet_list[l].player_number == 2:
                        Tank_enemy.Tank_enemy_list[z].kill(Bullet.bullet_list[l].player_number)
                        del Tank_enemy.Tank_enemy_list[z]
                        del Tank_enemy.Tank_enemy_rect_list[z]
            for z in range(len(Tank_own.Tank_own_list)-1,-1,-1):
                if Tank_own.Tank_own_list[z].rect.collidepoint(x,y):
                    if Bullet.bullet_list[l].player_number == 3:
                        p.add(l)
                        Tank_own.Tank_own_list[z].kill()
            for z in range(len(mapa.all_elements)-1,-1,-1):
                
                if mapa.all_elements[z].rect.collidepoint(x,y) and mapa.all_elements[z].colision :
                    mapa.destroy_el(mapa.all_elements[z])
                    p.add(l)
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
    def clear():
        Bullet.bullet_list=[]
                
def random_position(mapa,list1,list2):
    x,y=np.random.randint(0, WINDOWWIDTH - 99),np.random.randint(0, 150)
    while pygame.Rect(x,y,64,64).collidelist(mapa.list_elements_colision)!=-1 or  pygame.Rect(x,y,64,64).collidelist(list1)!=-1 or pygame.Rect(x,y,64,64).collidelist(list2)!=-1:
        x,y=np.random.randint(0, WINDOWWIDTH - 99),np.random.randint(0, 150)
    return (x,y)
def random_position1(mapa,list1,list2):
    x,y=np.random.randint(0, WINDOWWIDTH - 99),np.random.randint(WINDOWHEIGHT-170, WINDOWHEIGHT-70)
    while pygame.Rect(x,y,64,64).collidelist(mapa.list_elements_colision)!=-1 or  pygame.Rect(x,y,64,64).collidelist(list1)!=-1 or pygame.Rect(x,y,64,64).collidelist(list2)!=-1:
        x,y=np.random.randint(0, WINDOWWIDTH - 99),np.random.randint(WINDOWHEIGHT-170, WINDOWHEIGHT-70)
    return (x,y)

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
    
            
           
            
def rotate_tank(image,dire):
    return pygame.transform.rotate(image,-dire*90)            
        
    

window=Okno(WINDOWWIDTH,WINDOWHEIGHT)
window.menu_window()
