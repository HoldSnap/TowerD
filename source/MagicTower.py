from Tower import *
import pygame

class MagicTower(Tower):
    def __init__(self, NAME, POSITION):
        super().__init__(NAME, POSITION)
        self.damagePower = 0.005
        self.damageArea = 300
        self.img = pygame.image.load(MAGIC_TOWER_PATH  )
        self.score = 10 
        self.name = NAME