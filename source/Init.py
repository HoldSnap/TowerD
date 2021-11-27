import pygame
import sys


TOWER_PRICE =10
WIN_WIDTH=1000 #50*32 	
WIN_HEIGHT=800 # 32*32
FPS=60
ROAD_CHECKPOINTS =[(973, 57), (937, 54), (880, 61), (810, 60), (736, 64), (658, 73), (603, 87), (596, 132), (610, 185), (642, 209), (687, 207), (714, 207), (749, 217), (788, 246), (791, 275), (783, 312), (759, 341), (712, 354), (649, 356), (587, 356), (535, 350), (497, 332), (439, 313), (388, 312), (319, 312), (263, 312), (204, 311), (155, 307),(126, 274), (122, 232), (133, 191), (183, 168), (246, 167), (316, 170), (369, 160), (392, 120), (398, 80), (382, 42), (343, 11), (259, 10), (182, 14), (89, 22), (49, 35), (38, 96), (35, 152), (35, 211), (28, 280), (20, 
331), (25, 411), (27, 471), (27, 537), (36, 592), (38, 649), (39, 702), (57, 737), (114, 743), (159, 744), (189, 771), (253, 771), (316, 769),(386, 769), (416, 741), (426, 706), (432, 666), (420, 636), (379, 621), (324, 620), (275, 613), (244, 576), (243, 533), (263, 497), (315, 480), (366, 478), (434, 478), (515, 478), (598, 474), (671, 479), (743, 481), (778, 505), (792, 554), (767, 612), (716, 637), (646, 635), (561, 629),(525, 646), (511, 685), (517, 732), (539, 753), (576, 758), (627, 763), (695, 766), (764, 770), (836, 766), (907, 766), (950, 766), (982, 766), (996, 766)]
TOWERS_CHECKPOINTS=[(452, 742), (376, 497), (530, 492), (448, 238), (612, 228), (764, 233), (758, 493)]
BACKGROUND_PATH='Z:\\pygame\\assets\\M1.png'#КАРТА
DEFAULT_MONSTER_PATH = 'Z:\\pygame\\assets\\MON.png'#САМЫЙ СТРАШНЫЙ МОНСТР 'ОЛЕГ'
ARCHER_TOWER_PATH='Z:\\pygame\\assets\\ART1.1.png'
START_BUTTON_PATH = 'Z:\\pygame\\assets\\PLAY.png'
MAGIC_TOWER_PATH = 'Z:\\pygame\\assets\\MT1,1.png'
ROCK_TOWER_PATH = 'Z:\\pygame\\assets\\RT1.1.png'
START_BUTTON_POSITION = (WIN_WIDTH/2,WIN_HEIGHT/2)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
TOWER_AREA_RADIUS = 50 #радиус куда можно поставить башню 
GAME_SPACE_WINDOW=pygame.display.set_mode ((WIN_WIDTH,WIN_HEIGHT)) #расширение монитора 
