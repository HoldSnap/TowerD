from Tower import *
import pygame

class BombTower(Tower):
    def __init__(self, NAME, POSITION):
        super().__init__(NAME, POSITION)
        self.damagePower = 0.04
        self.damageArea = 150
        self.img = pygame.image.load(BOMB_TOWER_PATH )