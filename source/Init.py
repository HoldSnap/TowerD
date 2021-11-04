import pygame
import sys


TOWER_PRICE =10
WIN_WIDTH=1000 #50*32 	
WIN_HEIGHT=800 # 32*32
FPS=60
ROAD_CHECKPOINTS =[(14, 532), (75, 532), (112, 531), (138, 531), (158, 560), (168, 577), (185, 595), (240, 602), (307, 602), (361, 600), (418, 599), (489, 599), (553, 596), (593, 589), (625, 567), (639, 531), (646, 493), (648, 462), (645, 426), (632, 392), (606, 368), (573, 348), (538, 340), (495, 338), (446, 338), (407, 335), (366, 321), (339, 289), (334, 259), (334, 220), (344, 174), (367, 140), (406, 113), (456, 102), (526, 100), (586, 99), (670, 98), (733, 98), (793, 98), (845, 99), (916, 98), (980, 99)]
TOWERS_CHECKPOINTS=[(452, 742), (376, 497), (530, 492), (448, 238), (612, 228), (764, 233), (758, 493)]
BACKGROUND_PATH='Z:\\pygame\\assets\\M.png'#КАРТА
DEFAULT_MONSTER_PATH = 'Z:\\pygame\\assets\\Monster2.1.png'#САМЫЙ СТРАШНЫЙ МОНСТР 'ОЛЕГ'
ARCHER_TOWER_PATH='Z:\\pygame\\assets\\ART1.png'
START_BUTTON_PATH = 'Z:\\pygame\\assets\\PLAY.png'
MAGIC_TOWER_PATH = 'Z:\\pygame\\assets\\MT1.png'
ROCK_TOWER_PATH = 'Z:\\pygame\\assets\\RT1.png'
START_BUTTON_POSITION = (WIN_WIDTH/2,WIN_HEIGHT/2)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
TOWER_AREA_RADIUS = 50 #радиус куда можно поставить башню 
GAME_SPACE_WINDOW=pygame.display.set_mode ((WIN_WIDTH,WIN_HEIGHT)) #расширение монитора 
