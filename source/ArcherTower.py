from _typeshed import Self
from Tower import *
import pygame

class ArcherTower(Tower):
    def __init__(self, NAME, POSITION):
        super().__init__(NAME, POSITION)
        self.score = 10 
        self.name = NAME
        self.damagePower = 0.02
        self.img = pygame.image.load(ARCHER_TOWER_PATH)
        self.damageArea = 170