from Tower import *
import pygame

class RockTower(Tower):
    def __init__(self, NAME, POSITION):
        super().__init__(NAME, POSITION)
        self.damagePower = 0.05
        self.damageArea = 150
        self.img = pygame.image.load(ROCK_TOWER_PATH)
        self.score = 10 
        self.name = NAME