import pygame
import sys
from Init import *
from Tower import *


class FirstTower(Tower):
        def  __init__ (self):
                pygame.sprite.Sprite.__init__(self)
                self.image= pygame.image.load('Z:\pygame/assets/orange.jpg')
                self.rect = self.image.get_rect()
                self.isActive = False
        def startAction(self):
                self.isActive=True
                print("This is first tower!")
        def update(self):
                isMouseOkay=self.checkMousePosition()
                if isMouseOkay:
                
                #В Апдейте должен находитсяя мониторринег состояниек УЖЕ! созднанной башни, а не процесс ее создания

