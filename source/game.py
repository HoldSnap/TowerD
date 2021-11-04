import pygame
import keyboard
from math import *
import sys
from Init import *
from Monster import *
#from FirstTower import *
from Tower import *
from ArcherTower import *
from BombTower import *
from Music import *
from RockTower import *
import time
import random
pygame.font.init()




class Game:

	def __init__(self, window):
		self.width = WIN_WIDTH #ширина
		self.height = WIN_HEIGHT #высота 
		self.gameWindow = window  #окно игры 
		self.monsters = [Monster()] #монстры
		self.towers = [] #башенка 
		self.numOfActiveMonsters = 0
		self.monsterFrequency = 1
		self.numOfMonsters = 10
		self.gameScore = 100
		self.oldGameScore = 10
		self.currentTime= time.time()
		self.activeTowerCheckpoints = []
		self.backgroundImage = pygame.image.load(BACKGROUND_PATH) # карта
		self.backgroundImage = pygame.transform.scale(self.backgroundImage,(self.width,self.height)) # автоматическая  смена расширение для других мониторов  
		self.clicks=[] # найти координаты  
	def run(self):
		pygame.display.set_caption('My Game') # название окна игры 
		# Создаем группы игроков и башен, чтобы удобно было обновлять
		clock=pygame.time.Clock() # фпс
		Running = True 
		pygame.mixer.music.play(-1)
		
		while Running:# цикл для игры 
			#pygame.time.delay(0) #задержка 
			clock.tick(FPS) # фпс
			currentMousePosition = pygame.mouse.get_pos() # даёт координаты  мышки
			#Генерируем монстров с частотой monsterFrequency (в сек)
			self.monsterFrequency =random.randrange(1,10)/5
				
			if time.time()-self.currentTime>=self.monsterFrequency and self.numOfActiveMonsters < self.numOfMonsters:
				self.currentTime=time.time()
				self.numOfActiveMonsters+=1
				self.generate_monster()

			for event in pygame.event.get(): # ивент для выхода 
				if event.type == pygame.QUIT:
					Running=False
					
				keys = pygame.key.get_pressed()
				if keys[pygame.K_ESCAPE]:
					self.pause()
				"""""
				if event.type == pygame.MOUSEBUTTONDOWN:  # проверка на нажатие левой кнопки мыши 
					self.clicks.append(currentMousePosition) # даёт координаты 
					print(self.clicks)
			    """""
				for point in TOWERS_CHECKPOINTS: #пробегает по всем местам где нету или есть башенка
					if self.length_between_points(point,currentMousePosition)<TOWER_AREA_RADIUS: #проверка попадает ли мышка в область где можно ставить мышку 
						if event.type ==pygame.KEYDOWN and event.key ==pygame.K_t :  #проверка на нажатие 
							self.add_tower('archer_tower',point)  #добавление башни 
							self.activeTowerCheckpoints.append(point)  #делает так чтобы нельзя было паставить башню в это место опять 
							break #выход 

						if event.type ==pygame.KEYDOWN and event.key ==pygame.K_y :
							self.add_tower('bomb_tower',point)  
							self.activeTowerCheckpoints.append(point)
							break
						
						if event.type ==pygame.KEYDOWN and event.key ==pygame.K_u :
							self.add_tower('rock_tower',point) 
							self.activeTowerCheckpoints.append(point)
							break


			for m in self.monsters: # движение монстра 
				m.move()
			for t in self.towers:
				self.monsters = t.attack(self.monsters)
			
			#self.update_game_score()

			self.draw()
		pygame.quit()

	#def update_game_score(self):
		#font_name = pygame.font.Font(None, 36)
		#Score = font_name.render(self.gameScore,True,BLUE)
		#GAME_SPACE_WINDOW.blit(Score, (10,100))
		#pygame.display.update()


	def draw(self):
		self.gameWindow.blit(self.backgroundImage,(0,0)) #рисует  карту
	
		for click in self.clicks:
			pygame.draw.circle(self.gameWindow, BLUE,(click[0],click[1]), 5 ) #рисует круг 

		
		for m in self.monsters:
			m.draw(self.gameWindow)# отрисовка монстра
		
		for t in self.towers:
			t.draw(self.gameWindow)# рисует башню

		pygame.display.update()
	def generate_monster(self):
		newMonster= Monster()
		self.monsters.append(newMonster)
	
	

		
	def add_tower(self,name, position): #делает башню 	
		if (name == 'archer_tower'):
			new_tower = ArcherTower(name,position)
		if (name == 'bomb_tower'):
			new_tower = BombTower(name,position)
		if (name == 'rock_tower'):
			new_tower = RockTower(name,position)
			
		if position not in self.activeTowerCheckpoints and self.gameScore >= new_tower.score:
			new_tower.isActive = True
			self.gameScore -= new_tower.score
			self.towers.append(new_tower)
	
	#def main_ost(self): взаимодействие башен и монстров  + меню(начисление очков) 
	#	MAIN_OST
			
			
			

		

	def length_between_points(self,A, B): #расстояние от точкаи до точки 
		#x=КОРЕНЬ(X2-X1)**2+(Y2-Y1)**2
		AB=sqrt((A[0]- B[0])**2 + (A[1]-B[1])**2)
		return AB

	def pause (self):
		paused = True
		while paused :
			for event in pygame.event.get(): 
				if event.type == pygame.QUIT:
					Running=False
			keys = pygame.key.get_pressed()
			if keys[pygame.K_RETURN]:
				paused = False
			


				
				