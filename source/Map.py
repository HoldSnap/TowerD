import pygame
import sys
from Init import *

class Map(pygame.sprite.Sprite):
		def __init__(self):
			pygame.sprite.Sprite.__init__(self)
			
			self.H=HEIGHT//12
			self.W=WIDTH//12
			self.zeroBlock = pygame.image.load('Z:\pygame/assets/Grass2.png')
			self.oneBlock =  pygame.image.load('Z:\pygame/assets/Grass3.png')
			self.twoBlock = pygame.image.load('Z:\pygame/assets/Barrel1.jpg')
			self.threeBlock = pygame.image.load('Z:\pygame/assets/Stone2.png')

		def update(self,*players):
			keys =pygame.key.get_pressed()
			for player in players:
				x=player.getFirstXCoordinateByDirection()
				y=player.getFirstYCoordinateByDirection()
				if keys[pygame.K_i]==True:
					mapArray[y//12][x//12]=2
				if keys[pygame.K_t]==True:
					mapArray[y//12][x//12]=2
		
		def draw(self,screen):
			for i in range (self.H):
				for j in range(self.W):
					if(mapArray[i][j]==0):
						screen.blit(self.zeroBlock,(j*12,i*12))
					if(mapArray[i][j]==1):
						screen.blit(self.oneBlock,(j*12,i*12))
					if(mapArray[i][j]==2):
						screen.blit(self.twoBlock,(j*12,i*12))
					if(mapArray[i][j]==3):
						screen.blit(self.threeBlock,(j*12,i*12))
			