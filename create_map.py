#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 01:18:05 2016

@author: maciej
"""
import pygame
import numpy as np
WINDOWHEIGHT=640
WINDOWWIDTH=832

class MapElement():
    def __init__(self,x,y,file,direction = 0,colision=True):
        self.image = pygame.image.load(file)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x,y)
        self.direction = direction
        self.colision=colision
    def destroy(self):
        pass

       
#       self.image,self.rect,self.direction = rotate_image(self.image,self.rect,self.direction)


class Mur(MapElement):
    
    def __init__(self,x,y,direction=0,destroyed_file='superdziurka322.png',colision=True,life=2):
        MapElement.__init__(self,x=x,y=y,file='supermurek322.png',direction=0,colision=True)
        self.destroyed_image=pygame.image.load(destroyed_file)
        self.life = life
    
    
    def destroy(self):
        self.life-=1
        if self.life ==1:
            self.image=self.destroyed_image
            return False
        elif self.life == 0:
            return True
            
class TwardyMur(MapElement):
     def __init__(self,x,y,direction=0,colision=True):
        MapElement.__init__(self,x=x,y=y,file='twardymurek.png',direction=0,colision=True)
     def destroy(self):
        pass

class Woda(MapElement):
    def __init__(self,x,y,direction=0,colision=True):
        MapElement.__init__(self,x=x,y=y,file='woda.png',direction=0,colision=False)
        
        
class Las(MapElement):
    def __init__(self,x,y,direction=0,colision=True):
        MapElement.__init__(self,x=x,y=y,file='superlas2.png',direction=0,colision=False)    
            
class Pingwinek(MapElement):
    def __init__(self,x,y,direction=0,colision=True):
        MapElement.__init__(self,x=x,y=y,file='linux.png',direction=0,colision=True)        
        
####################### BONUSY #######################        
        
class Granat(MapElement):
    def __init__(self,mapa,x,y,colision=True):
        MapElement.__init__(self,x=x,y=y,file='granat.png',direction=0,colision=True) 
        mapa.add(self)
           
class Stoper(MapElement):
    def __init__(self,mapa,x,y,colision=True):
        MapElement.__init__(self,x=x,y=y,file='stoper.png',direction=0,colision=True)  
        mapa.add(self)
        
class Pancerz(MapElement):
    def __init__(self,mapa,x,y,colision=True):
        MapElement.__init__(self,x=x,y=y,file='pancerz.png',direction=0,colision=True)           
        mapa.add(self)
        
class Gwiazdka(MapElement):
    def __init__(self,mapa,x,y,colision=True):
        MapElement.__init__(self,x=x,y=y,file='gwiazdka22.png',direction=0,colision=True)         
        mapa.add(self)
        
class Nurkowanie(MapElement):
    def __init__(self,mapa,x,y,colision=True):
        MapElement.__init__(self,x=x,y=y,file='nurkowanie.png',direction=0,colision=True)  
        mapa.add(self)
        
class Serduszko(MapElement):
    def __init__(self,mapa,x,y,colision=True):
        MapElement.__init__(self,x=x,y=y,file='zycie222.png',direction=0,colision=True)  
        mapa.add(self)        
        
 
        
        
        
        
        
        
        
        
        
        
        
        
class Map():
    def __init__(self,screen,list_of_elements,vec_if_colision):
        self.all_elements=list_of_elements
        self.screen=screen
        self.list_elements_colision=[]
        for i in vec_if_colision:
            self.list_elements_colision.append(self.all_elements[i].rect)
            
    def check_if_colision(self,element):
        """True if colision"""
        return element.rect.collidelist(self.list_elements_colision)
    def check_if_move(self,element,direction):
        """True if move is ok."""
        rect=element.rect.copy()
        if direction == 0:
            if rect.move(0,-element.speed_tank).collidelist(self.list_elements_colision)==-1:
                return True
        elif direction == 1:
            if rect.move(element.speed_tank,0).collidelist(self.list_elements_colision)==-1:
                return True          
        elif direction == 2:
            if rect.move(0,element.speed_tank).collidelist(self.list_elements_colision)==-1:
                return True
        elif direction == 3:
            if rect.move(-element.speed_tank,0).collidelist(self.list_elements_colision)==-1:
                return True
        return False   
    def draw_all(self):
        if len(self.all_elements)!=0:
            for el in self.all_elements:
                self.screen.screen.blit(el.image,el.rect)
    def destroy_el(self,element):
        if isinstance(element,Pingwinek):
            print("WHAT")
#            del self.list_elements_colision[self.list_elements_colision.index(element.rect)]
#            del self.all_elements[self.all_elements.index(element)]
            self.screen.exit_window()
            return None
        elif element.destroy():
            del self.list_elements_colision[self.list_elements_colision.index(element.rect)]
            del self.all_elements[self.all_elements.index(element)]
    def run_exit():
        screen.exit_window()
        
        
    def create_ring(self):
        l=[]
        l_rect=[]
        d0 = Mur(0,0)
        d0.rect.bottom=self.screen.rect.bottom
        d0.rect.right=self.screen.rect.centerx-32
        l.append(d0)
        l_rect.append(d0.rect)
        d01=Mur(self.screen.rect.centerx+32,0)
        d01.rect.bottom=self.screen.rect.bottom
        l.append(d01)
        l_rect.append(d01.rect)
        d1=Mur(d0.rect.x,0)
        d1.rect.bottom=d0.rect.top
        d11=Mur(self.screen.rect.centerx+32,0)
        d11.rect.bottom=d01.rect.top
        l.append(d1)
        l_rect.append(d1.rect)    
        l.append(d11)
        l_rect.append(d11.rect)
        d2=Mur(d1.rect.x,0)
        d2.rect.bottom=d1.rect.top
        d21=Mur(self.screen.rect.centerx+32,0)
        d21.rect.bottom=d11.rect.top  
        l.append(d2)
        l_rect.append(d2.rect)    
        l.append(d21)
        l_rect.append(d21.rect)
        d22=Mur(0,0)
        d22.rect.left=d2.rect.right
        d22.rect.top=d2.rect.top
        d23=Mur(0,0)
        d23.rect.left=d22.rect.right
        d23.rect.top=d22.rect.top
        l.append(d22)
        l_rect.append(d22.rect)    
        l.append(d23)
        l_rect.append(d23.rect)
        pin=Pingwinek(self.screen.rect.centerx-32,WINDOWHEIGHT-64)
        l.append(pin)
        l_rect.append(pin.rect)
        self.all_elements+=l
        self.list_elements_colision+=l_rect
        
    def add(self,el):
        self.all_elements.append(el)
        if el.colision:
            self.list_elements_colision.append(el.rect)
 
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
        self.rect=self.screen.get_rect()
        pygame.display.set_caption('Tankujemy')           
        
window=Okno(WINDOWWIDTH,WINDOWHEIGHT)
window.screen.fill((100,100,100))
lista_elementow=[Mur(100,100),TwardyMur(50,50)]
vec_collision=[0,1]
mapka=Map(window,lista_elementow,vec_collision)
pin=Pingwinek(window.rect.centerx-32,WINDOWHEIGHT-64)
mapka.add(pin)
mapka.draw_all()
pygame.display.flip()



