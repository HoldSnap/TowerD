import pygame
import sys

WIDTH=1680 #50*32 	
HEIGHT=1050 # 32*32
FPS=30
screen=pygame.display.set_mode ((WIDTH,HEIGHT))
class Player(pygame.sprite.Sprite):
		def  __init__ (self):
				pygame.sprite.Sprite. __init__(self)
				self.imagesUp=[pygame.image.load('Z:\pygame/assets/up0.png'),pygame.image.load('Z:\pygame/assets/up1.png'),pygame.image.load('Z:\pygame/assets/up2.png')]
				self.imagesDown=[pygame.image.load('Z:\pygame/assets/d0.png'),pygame.image.load('Z:\pygame/assets/d1.png'),pygame.image.load('Z:\pygame/assets/d2.png')]
				self.imagesLeft=[pygame.image.load('Z:\pygame/assets/l0.png'),pygame.image.load('Z:\pygame/assets/l1.png'),pygame.image.load('Z:\pygame/assets/l2.png' )]
				self.imagesRight=[pygame.image.load('Z:\pygame/assets/r0.png'),pygame.image.load('Z:\pygame/assets/r1.png'),pygame.image.load('Z:\pygame/assets/r2.png ')]
				self.image = pygame.image.load('Z:\pygame/assets/up0.png')
				self.rect = self.image.get_rect()
				self.rect.center = (WIDTH / 2, HEIGHT / 2)
				self.speed = 10
				self.currentFrame=0
				self.keyboardMode=0
				self.currentDirection='U'# U-up D-down R-right L-left
		#Возвращает иксовую координату края прямоуугольника игрока в зависимости от направления
		def getFirstXCoordinateByDirection(self):
			if self.currentDirection=='U':
				return self.rect.centerx
			if self.currentDirection=='D':
				return self.rect.centerx
			if self.currentDirection=='R':
				return self.rect.centerx + self.rect.width//2
			if self.currentDirection=='L':
				return self.rect.centerx - self.rect.width//2
		
		def getFirstYCoordinateByDirection(self):
			if self.currentDirection=='U':
				return self.rect.centery - self.rect.height//2
			if self.currentDirection=='D':
				return self.rect.centery + self.rect.height//2
			if self.currentDirection=='R':
				return self.rect.centery
			if self.currentDirection=='L':
				return self.rect.centery

		def update(self):
					keys =pygame.key.get_pressed()
					isPressed=False
					if self.keyboardMode==0:
						if(self.currentFrame>2):
							self.currentFrame=0

						if keys[pygame.K_LEFT] :
							self.currentDirection='L'	
							if(self.rect.left>0):
								self.rect.x-=self.speed
							self.image=self.imagesLeft[self.currentFrame]				
							isPressed=True

						if keys[pygame.K_RIGHT] :
							self.currentDirection='R'	
							if(self.rect.right<WIDTH):
								self.rect.x+=self.speed							
							self.image=self.imagesRight[self.currentFrame]
							isPressed=True
 
						if keys[pygame.K_UP] :
							self.currentDirection='U'	
							if(self.rect.top>0):
								self.rect.y-=self.speed							
							self.image=self.imagesUp[self.currentFrame]
							isPressed=True

						if keys[pygame.K_DOWN] :
							self.currentDirection='D'	
							if(self.rect.bottom<HEIGHT) :
								self.rect.y+=self.speed						
							self.image=self.imagesDown[self.currentFrame]
							isPressed=True
						if isPressed:
							self.currentFrame+=1
						else:
							screen.blit(self.image,(self.rect.x,self.rect.y),(0,0,96,96))

					if self.keyboardMode==1:

						if(self.currentFrame>2):
							self.currentFrame=0
					
						if keys[pygame.K_a]:
							self.currentDirection='L'	
							if(self.rect.left>0):
								self.rect.x-=self.speed
							self.image=self.imagesLeft[self.currentFrame]		
							isPressed=True
					

						if keys[pygame.K_d] :
							self.currentDirection='R'	
							if(self.rect.right<WIDTH):
								self.rect.x+=self.speed
							self.image=self.imagesRight[self.currentFrame]		
							isPressed=True

						if keys[pygame.K_w] :
							self.currentDirection='U'	
							if(self.rect.top>0):
								self.rect.y-=self.speed
							self.image=self.imagesUp[self.currentFrame]		
							isPressed=True

						if keys[pygame.K_s] :
							self.currentDirection='D'	
							if(self.rect.bottom<HEIGHT):
								self.rect.y+=self.speed
							self.image=self.imagesDown[self.currentFrame]			
							isPressed=True
						if isPressed:
							self.currentFrame+=1
						else:
						    screen.blit(self.image,(self.rect.x,self.rect.y),(0,0,96,96))