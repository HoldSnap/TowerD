import pygame
from math import *
import sys
from Init import *
from Monster import *
class Tower:
    def __init__(self, NAME, POSITION) :
        self.score = 10 
        self.name = NAME
        self.damagePower = 0.02
        self.isActive = False 
        self.x = POSITION[0]
        self.y = POSITION[1]
        self.img = pygame.image.load(ARCHER_TOWER_PATH)
        self.damageArea = 170
    def draw(self,window):
        if self.isActive:
            window.blit(self.img,(self.x-self.img.get_width()//2, self.y-self.img.get_height()//2))  #номрально ставит  башню 
    def attack (self, monsters: Monster):
        for monster in monsters: #взаидодействие с монстром (нанесение урона )
            distance = sqrt((monster.x-self.x)**2 +(monster.y-self.y)**2) #вычесление дистанции
            if distance < self.damageArea:
                if monster.hit(self.damagePower):
                    monsters.remove(monster)
                    self.update_score(10)
                break

        return monsters
    def update_score (self, updateValue):
        self.score += updateValue
