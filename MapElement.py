#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The MIT License (MIT)

Copyright (c) 2016 Maciej Śliwowski

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Graphical elements designed by Paulina Jastrzębska.
Sound effects downloaded from links presented below on the Creative Commons License (Attribution 3.0 unported https://creativecommons.org/licenses/by/3.0/).
https://www.freesound.org/people/ProjectsU012/sounds/333785/
https://www.freesound.org/people/jivatma07/sounds/173858/
https://www.freesound.org/people/AlaskaRobotics/sounds/221560/
https://www.freesound.org/people/jeremysykes/sounds/341238/
https://www.freesound.org/people/funhouse/sounds/2513/
https://www.freesound.org/people/smcameron/sounds/51464/
https://www.freesound.org/people/mialena24/sounds/364343/ 
"""
import pygame
import numpy as np
WINDOWHEIGHT=640
WINDOWWIDTH=832
import os

class MapElement():
    def __init__(self,x,y,file,direction = 0,colision=True):
        self.image = pygame.image.load(file)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x,y)
        self.direction = direction
        self.colision=colision
    def destroy(self):
        return False

       
#       self.image,self.rect,self.direction = rotate_image(self.image,self.rect,self.direction)


class Mur(MapElement):
    
    def __init__(self,x,y,direction=0,destroyed_file=os.path.join('graphics','superdziurka322.png'),colision=True,life=2):
        MapElement.__init__(self,x=x,y=y,file=os.path.join('graphics','supermurek322.png'),direction=0,colision=True)
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
        MapElement.__init__(self,x=x,y=y,file=os.path.join('graphics','twardymurek32.png'),direction=0,colision=True)
#     def destroy(self):
#        pass

class Woda(MapElement):
    def __init__(self,x,y,mapa,direction=0,colision=True):
        MapElement.__init__(self,x=x,y=y,file=os.path.join('graphics','woda.png'),direction=0,colision=False)
        mapa.add_water(self)
        
class Las(MapElement):
    def __init__(self,x,y,direction=0,colision=False):
        MapElement.__init__(self,x=x,y=y,file=os.path.join('graphics','superlas2.png'),direction=0,colision=False)    
            
class Pingwinek(MapElement):
    def __init__(self,x,y,direction=0,colision=True):
        MapElement.__init__(self,x=x,y=y,file=os.path.join('graphics','linux.png'),direction=0,colision=True)        
        
####################### BONUSY #######################        
        
class Granat(MapElement):
    def __init__(self,mapa,x,y,colision=True):
        MapElement.__init__(self,x=x,y=y,file=os.path.join('graphics','granat.png'),direction=0,colision=False) 
        mapa.add_bonus(self)

        self.typ=0
           
class Stoper(MapElement):
    def __init__(self,mapa,x,y,colision=True):
        MapElement.__init__(self,x=x,y=y,file='stoper.png',direction=0,colision=False)  
        mapa.add_bonus(self)
        self.typ=1
        
class Pancerz(MapElement):
    def __init__(self,mapa,x,y,colision=True):
        MapElement.__init__(self,x=x,y=y,file=os.path.join('graphics','pancerz.png'),direction=0,colision=False)           
        mapa.add_bonus(self)
        self.typ=2
        
class Gwiazdka(MapElement):
    def __init__(self,mapa,x,y,colision=True):
        MapElement.__init__(self,x=x,y=y,file=os.path.join('graphics','gwiazdka22.png'),direction=0,colision=False)         
        mapa.add_bonus(self)
        self.typ=3
        
class Nurkowanie(MapElement):
    def __init__(self,mapa,x,y,colision=True):
        MapElement.__init__(self,x=x,y=y,file=os.path.join('graphics','nurkowanie.png'),direction=0,colision=False)  
        mapa.add_bonus(self)
        self.typ=4
        
class Serduszko(MapElement):
    def __init__(self,mapa,x,y,colision=True):
        MapElement.__init__(self,x=x,y=y,file=os.path.join('graphics','zycie222.png'),direction=0,colision=False)  
        mapa.add_bonus(self)        
        self.typ=5
        
 
        
        
        
        
        
        
        
        
        
        
        
        
class Map():
    def __init__(self,screen,list_of_elements=[],vec_if_colision=[]):
        self.all_elements=list_of_elements
        self.screen=screen
        self.list_elements_colision=[]
        self.bonus_list=[]
        self.bonus_list_rect=[]
        self.water_rect_list = []
        self.zas=102
        self.l=[]
        self.l_rect=[]
        if len(vec_if_colision)!=0:
            for i in vec_if_colision:
                self.list_elements_colision.append(self.all_elements[i].rect)
            
    def check_if_colision(self,element):
        """True if colision"""
        return element.rect.collidelist(self.list_elements_colision)
    def check_if_move(self,element,direction,wat):
        """True if move is ok."""
        rect=element.rect.copy()
        if not self.water_rect_list or not wat:
            if direction == 0:
                if rect.move(0,-element.speed_tank).collidelist(self.list_elements_colision)==-1 and rect.move(0,-element.speed_tank).collidelist(self.water_rect_list)==-1:
                    return True
            elif direction == 1:
                if rect.move(element.speed_tank,0).collidelist(self.list_elements_colision)==-1 and rect.move(element.speed_tank,0).collidelist(self.water_rect_list)==-1:
                    return True          
            elif direction == 2:
                if rect.move(0,element.speed_tank).collidelist(self.list_elements_colision)==-1 and rect.move(0,element.speed_tank).collidelist(self.water_rect_list)==-1:
                    return True
            elif direction == 3:
                if rect.move(-element.speed_tank,0).collidelist(self.list_elements_colision)==-1 and rect.move(-element.speed_tank,0).collidelist(self.water_rect_list)==-1:
                    return True
        elif wat and self.water_rect_list:
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
        if self.zas<=100:
            self.zas+=1
            if len(self.all_elements)!=0:
                for el in self.all_elements:
                    self.screen.screen.blit(el.image,el.rect)
        elif self.zas==101:

            for el in self.l:
                del self.all_elements[self.all_elements.index(el)]
            for el in self.l_rect:
                del self.list_elements_colision[self.list_elements_colision.index(el)]
            self.l=[]
            self.l_rect=[]
            self.zas=103
        else:
            if len(self.all_elements)!=0:
                for el in self.all_elements:
                    self.screen.screen.blit(el.image,el.rect)      
    def destroy_el(self,element):
        if isinstance(element,Pingwinek):
#            del self.list_elements_colision[self.list_elements_colision.index(element.rect)]
#            del self.all_elements[self.all_elements.index(element)]
            self.screen.exit_window()
            return None
        elif element.destroy():
            if element.rect in self.list_elements_colision:
                del self.list_elements_colision[self.list_elements_colision.index(element.rect)]
            del self.all_elements[self.all_elements.index(element)]
#            except ValueError:
#                pass
    def run_exit():
        screen.exit_window()
    def umocnij(self):
        self.zas=0
        l=[]
        l_rect=[]
        d0 = TwardyMur(0,0)
        d0.rect.bottom=self.screen.rect.bottom
        d0.rect.right=self.screen.rect.centerx-32
        l.append(d0)
        l_rect.append(d0.rect)
        d01=TwardyMur(self.screen.rect.centerx+32,0)
        d01.rect.bottom=self.screen.rect.bottom
        l.append(d01)
        l_rect.append(d01.rect)
        d1=TwardyMur(d0.rect.x,0)
        d1.rect.bottom=d0.rect.top
        d11=TwardyMur(self.screen.rect.centerx+32,0)
        d11.rect.bottom=d01.rect.top
        l.append(d1)
        l_rect.append(d1.rect)    
        l.append(d11)
        l_rect.append(d11.rect)
        d2=TwardyMur(d1.rect.x,0)
        d2.rect.bottom=d1.rect.top
        d21=TwardyMur(self.screen.rect.centerx+32,0)
        d21.rect.bottom=d11.rect.top  
        l.append(d2)
        l_rect.append(d2.rect)    
        l.append(d21)
        l_rect.append(d21.rect)
        d22=TwardyMur(0,0)
        d22.rect.left=d2.rect.right
        d22.rect.top=d2.rect.top
        d23=TwardyMur(0,0)
        d23.rect.left=d22.rect.right
        d23.rect.top=d22.rect.top
        l.append(d22)
        l_rect.append(d22.rect)    
        l.append(d23)
        l_rect.append(d23.rect)
        self.all_elements+=l
        self.list_elements_colision+=l_rect        
        self.l=l
        self.l_rect=l
        
    def create_ring(self):
        self.add(Mur(352,WINDOWHEIGHT-32))
        self.add(Mur(448,WINDOWHEIGHT-32))
        self.add(Mur(448,WINDOWHEIGHT-64))
        self.add(Mur(352,WINDOWHEIGHT-64))
        self.add(Mur(352,WINDOWHEIGHT-96))
        self.add(Mur(448,WINDOWHEIGHT-96))
        self.add(Mur(416,WINDOWHEIGHT-96))
        self.add(Mur(384,WINDOWHEIGHT-96))
        self.add(Pingwinek(self.screen.rect.centerx-32,WINDOWHEIGHT-64))
    
    def create_random():
        pass
        
    def add(self,el):
        self.all_elements.append(el)
        if el.colision:
            self.list_elements_colision.append(el.rect)
    def add_bonus(self,bon):
        self.all_elements.append(bon)
        self.bonus_list.append(bon)
        self.bonus_list_rect.append(bon.rect)
    def add_water(self,bon):
        self.all_elements.append(bon)
        self.water_rect_list.append(bon.rect)
    def del_bonus(self,el):
        pass
        del self.all_elements[self.all_elements.index(el)]
        del self.bonus_list[self.bonus_list.index(el)]
        del self.bonus_list_rect[self.bonus_list_rect.index(el.rect)]
    def clear(self):
        self.all_elements=[]
        self.bonus_list=[]
        self.bonus_list_rect=[]
        self.list_elements_colision=[]
        self.water_rect_list=[]
        
                                 
#    def level4(self):
#            l=[]
#            l_rect=[]
#            k=0
#            for i in range(4):
#                self.add(Mur(0,k+192))
##                l_rect.append(Mur(0,k+192).rect)
#                self.add(Mur(800,k+192))
##                l_rect.append(Mur(800,k+192).rect)
#                k+=32
#            k=0
#            for i in range(4):
#                self.add(Mur(k,320))
##                l_rect.append(Mur(k,320).rect)
#                self.add(Mur(96,k+192))
##                l_rect.append(Mur(96,k+192).rect)
#                self.add(Mur(k+128,192))
##                l_rect.append(Mur(k+128,192).rect)
#    
#                self.add(Mur(800-k,320))
##                l_rect.append(Mur(800-k,320).rect)
#                self.add(Mur(800-96,k+192))
##                l_rect.append(Mur(800-96,k+192).rect)
#                self.add(Mur(800-k-128,192))
##                l_rect.append(Mur(800-k-128,192).rect)
#    
#                self.add(Mur(k,320+32))
##                l_rect.append(Mur(k+32,320).rect)
#                self.add(Mur(96+32,k+192+64))
##                l_rect.append(Mur(96+32,k+192+32).rect)
#                self.add(Mur(k+128,192+32))
##                l_rect.append(Mur(k+128+32,192+32).rect)
#    
#                self.add(Mur(800-k,320+32))
##                l_rect.append(Mur(800-k,320+32).rect)
#                self.add(Mur(800-96-32,k+192+64))
##                l_rect.append(Mur(800-96,k+192).rect)
#                self.add(Mur(800-k-128,192+32))
##                l_rect.append(Mur(800-k-128+32,192+32).rect)
#                k+=32
#    
#            k=256
#            for i in range(10):
#                self.add(Mur(k,192))
##                l_rect.append(Mur(k,192).rect)
#                self.add(Mur(k,192+32))
##                l_rect.append(Mur(k,192+32).rect)
#                k+=32
#            k=160
#            for i in range(8):
#                self.add(Las(k,256))
##                l_rect.append(Las(k,256).rect)
#                self.add(Las(k,256+64))
##                l_rect.append(Las(k,256+64).rect)
#                k+=64
#    
#            k=0
#            for i in range(2):
#                Woda(32,k+192,self)
#                Woda(800-64,k+192,self)
##                self.add(Woda(32,k+192))
##                l_rect.append(Woda(32,k+192).rect)
##                self.add(Woda(800-64,k+192))
##                l_rect.append(Woda(800-64,k+192).rect)
#                k+=64
#    
#            k=0
#            for i in range(13):
#                self.add(Las(k,256+128))
##                l_rect.append(Las(k,256+128).rect)
#                self.add(Las(k,256+64+128))
##                l_rect.append(Las(k,256+64+128).rect)
#    
#                self.add(Las(k,64))
##                l_rect.append(Las(k,64).rect)
#                self.add(Las(k,128))
##                l_rect.append(Las(k,128).rect)
#                k+=64
#    
#            k=0
#            for i in range(26):
#                self.add(Mur(k,256+128+128))
##                l_rect.append(Mur(k,256+128+128).rect)
#                k+=32
#                
##            self.all_elements+=l
##            self.list_elements_colision+=l_rect

    def level1(self):
            k=128
            m=96
            for i in range(5):
                for i in range(3):
                    self.add(Mur(k,m))
                    m+=32
                m=96
                k+=32
    
            k=800-128
            m=96
            for i in range(5):
                for i in range(3):
                    self.add(Mur(k,m))
                    m+=32
                m=96
                k-=32
                
            k=288
            m=288
            for i in range(4):
                self.add(Las(k,96))
                self.add(Mur(m,96+64))
                self.add(Mur(800-m,96+64))
                k+=64
                m+=32
    
            k=0
            for i in range(16):
                self.add(Mur(800-k,320-32))
                self.add(Mur(800-k,320))
                self.add(Mur(k,320+128))
                self.add(Mur(k,320+160))
                k+=32
    
            k=0
            for i in range(5):
                self.add(Las(k,288))
                self.add(Las(k+512,321+128))
                k+=64
                
              
    def level2(self):
        k=0
        for i in range(26):
            self.add(Mur(k,192+32))
            self.add(Mur(k,224+32))
            self.add(Mur(k,384+32))
            self.add(Mur(k,416+32))
            k+=32
            
        k=0
        for i in range(13):
            self.add(Las(k,64+32))
            self.add(Las(k,128+32))
            self.add(Las(k,448+32))
            k+=64
            
        k=0
        for i in range(2):
            self.add(Las(k,256+32))
            self.add(Las(k,256+96))
            k+=64
            
        k=128
        for i in range(4):
            Woda(k,256+32,self)
            self.add(Las(k,320+32))
            k+=64
            self.add(Las(k,256+32))
            Woda(k,320+32,self)
            k+=64

        k=640
        for i in range(3):
            self.add(Las(k,256+32))
            self.add(Las(k,256+96))
            k+=64

    def level3(self):
        l=[]
        l_rect=[]
        k=0
        for i in range(26):
            self.add(Mur(k,384))
            k+=32

        k=0
        for i in range(3):
            self.add(Las(k,320))
            k+=64
            for i in range(3):
                Woda(k,320,self)
                k+=64
            self.add(Las(768,320))
        k=0
        for i in range(13):
            self.add(Las(k,256))
            self.add(Las(k,192))
            k+=64
        k=0
        for i in range(26):
            self.add(Mur(k,160))
            self.add(Mur(k,128))
            k+=32

        k=64
        for i in range(6):
            self.add(Mur(k,448))
            self.add(Mur(800-k,448))

            self.add(Mur(k,512))
            self.add(Mur(800-k,512))

            self.add(Mur(k+160,448))
            self.add(Mur(800-k-160,448))
            k+=32
            
    
    def level4(self):
            l=[]
            l_rect=[]
            k=0
            for i in range(4):
                self.add(Mur(0,k+192))
                self.add(Mur(800,k+192))
                k+=32
            k=0
            for i in range(4):
                self.add(Mur(k,320))
                self.add(Mur(96,k+192))
                self.add(Mur(k+128,192))
    
                self.add(Mur(800-k,320))
                self.add(Mur(800-96,k+192))
                self.add(Mur(800-k-128,192))
    
                self.add(Mur(k,320+32))
                self.add(Mur(96+32,k+192+64))
                self.add(Mur(k+128,192+32))
    
                self.add(Mur(800-k,320+32))
                self.add(Mur(800-96-32,k+192+64))
                self.add(Mur(800-k-128,192+32))
                k+=32
    
            k=256
            for i in range(10):
                self.add(Mur(k,192))
                self.add(Mur(k,192+32))
                k+=32
            k=160
            for i in range(8):
                self.add(Las(k,256))
                self.add(Las(k,256+64))
                k+=64
    
            k=0
            for i in range(2):
                Woda(32,k+192,self)
                Woda(800-64,k+192,self)
                k+=64
    
            k=0
            for i in range(13):
                self.add(Las(k,256+128))
                self.add(Las(k,256+64+128))
    
                self.add(Las(k,64))
                self.add(Las(k,128))
                k+=64
    
            k=0
            for i in range(26):
                self.add(Mur(k,256+128+128))
                k+=32