import pygame
import sys


def move(self,x,y):
    if self.rect.left + x < 0:
        self.rect.left = 0
    elif self.rect.right + x > 1600:
        self.rect.right = 1600
    elif self.rect.top + y < 0:
        self.rect.top = 0
    elif self.rect.bottom + y > 1024:
        self.rect.bottom = 1024
    else:
        self.rect.move_ip((x,y))