import pygame
import keyboard
from math import *
import sys
from Init import *
from Monster import *
#from FirstTower import *
from Tower import *
from ArcherTower import *
from MagicTower import *
from Music import *
from RockTower import *
import time
import random
pygame.font.init()


class Scorer:
    def __init__(self,initScore):
        self.currentScore = initScore
    def update_score(self, prevMonsters, prevTowers,currMonsters,currTowers):
        sumPrevMonsters = 0
        sumCurrMonsters = 0
        for m in prevMonsters:
            sumPrevMonsters+= m.price
        for m in currMonsters:
            sumCurrMonsters += m.price
        monsterScore = sumPrevMonsters - sumCurrMonsters
        prevTowersScore = 0
        currTowersScore = 0
        for t in prevTowers:
            prevTowersScore+=t.score
        for t in currTowers:
            currTowersScore+=t.score
        towerScore=currTowersScore- prevTowersScore 
        
        self.currentScore+= monsterScore - towerScore


        

    def draw(self,window):
        font_name = pygame.font.SysFont('impact', 30)
        Score = font_name.render(str(self.currentScore),True,WHITE)
        window.blit(Score, (WIN_WIDTH*0.9,WIN_HEIGHT*0.03))
        #pygame.display.update()

