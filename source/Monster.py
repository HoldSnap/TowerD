import math
import pygame
import sys
from Init import *

class Monster:
    def __init__(self) :
        self.x = ROAD_CHECKPOINTS[0][0] #нач точки 7-8
        self.y =  ROAD_CHECKPOINTS[0][1]
        self.curr_checkpoint=0
        self.speed=3# 0->1
        self.health = 1
        self.maxHealth = 100
        self.road = ROAD_CHECKPOINTS 
        self.img = pygame.image.load(DEFAULT_MONSTER_PATH) #картинка олега

    def draw(self,window):
        #ОТРИСОВКА
        window.blit(self.img,(self.x, self.y)) 
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
            self.x = self.road[0][0]
            self.y = self.road[0][1]
            self.curr_checkpoint = 0
     

    def hit(self,damage):
        self.health -= damage
        if self.health <= 0:
            return True
        return False
    def collide(self, monsterA, monsterB):
        pass
            
    


