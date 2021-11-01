from Tower import *
import pygame

class BombTower(Tower):
    def __init__(self, NAME, POSITION):
        super().__init__(NAME, POSITION)
        self.damagePower = 60
        self.damageArea = 150
    