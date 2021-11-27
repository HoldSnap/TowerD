import math
import pygame
import sys
from Init import *
from game import *

class Monster:
    def __init__(self) :
        self.x = ROAD_CHECKPOINTS[0][0] #нач точки 7-8
        self.y =  ROAD_CHECKPOINTS[0][1]
        self.curr_checkpoint=0
        self.speed=3# 0->1
        self.health = 1
        self.DeathMonster = 0
        self.NastDeath = 0
        self.price = 10
        self.maxHealth = 1
        self.road = ROAD_CHECKPOINTS 
        self.img = pygame.image.load(DEFAULT_MONSTER_PATH) #картинка олега
        self.winner = False
    def draw(self,window):
        #ОТРИСОВКА
        barLength = 35 # общий размер прямоугольника, в котором отражаем уровень жизни
        part = float(barLength/self.maxHealth)
        healthBarLength = round( self.health * part) # Длина уровня жизни в пикселях
        
        window.blit(self.img,(self.x, self.y))

        pygame.draw.rect(window,RED,(self.x-20,self.y-50,barLength,10))
        pygame.draw.rect(window,GREEN,(self.x-20,self.y-50,healthBarLength,10))
    def move(self):
        nextCheckpoint_x = self.road[self.curr_checkpoint+1][0]
        nextCheckpoint_y = self.road[self.curr_checkpoint+1][1]
        change_x =nextCheckpoint_x - self.x #cколько прошёл 22-23
        change_y = nextCheckpoint_y - self.y
        step_x = change_x*self.speed/math.sqrt(change_x**2 + change_y**2)
        step_y = change_y*self.speed/math.sqrt(change_x**2 + change_y**2)
        self.x += step_x 
        self.y += step_y
        if change_x>=0: #не тп монстра 
            if change_y > 0:
                if self.x >=nextCheckpoint_x and self.y >= nextCheckpoint_y:
                    self.curr_checkpoint+=1
            if change_y <= 0:
                if self.x >=nextCheckpoint_x and self.y <= nextCheckpoint_y:
                    self.curr_checkpoint+=1
        if change_x<0:
            if change_y > 0:
                if self.x <=nextCheckpoint_x and self.y >= nextCheckpoint_y:
                    self.curr_checkpoint+=1
            if change_y <= 0:
                if self.x <=nextCheckpoint_x and self.y <= nextCheckpoint_y:
                    self.curr_checkpoint+=1

        if self.curr_checkpoint >= len(self.road)-1: #18-21 делаем круг 
           # self.x = self.road[0][0]
           # self.y = self.road[0][1]
           # self.curr_checkpoint = 0
            self.winner = True

     

    def hit(self,damage):    
        self.health -= damage
        if self.health <= 0:
            return True
        return False
    def collide(self, monsterA, monsterB):
        pass
            
    


