import pygame
import sys



TOWER_PRICE =10
WIN_WIDTH=1000 #50*32 	
WIN_HEIGHT=800 # 32*32
FPS=60
ROAD_CHECKPOINTS =[(6, 520), (42, 523), (91, 522), (108, 525), (122, 543), (143, 566), (170, 583), (187, 593), (209, 597), (228, 592), (250, 584), (273, 576), (320, 571), (354, 586), (406, 598), (459, 597), (517, 596), (548, 594), (596, 583), (625, 551), (642, 506), (641, 466), (622, 417), (600, 389), (552, 352), (506, 331), (430, 320), (376, 311), (344, 282), (320, 240), (315, 214), (317, 165), (331, 146), (378, 106), (429, 87), (516, 82), (590, 77), (702, 79), (814, 82), (881, 81), (948, 79), (987, 79)]
TOWERS_CHECKPOINTS=[(452, 742), (376, 497), (530, 492), (448, 238), (612, 228), (764, 233), (758, 493)]
BACKGROUND_PATH='Z:\\pygame\\assets\\M.png'#КАРТА
DEFAULT_MONSTER_PATH = 'Z:\\pygame\\assets\\monster.png'#САМЫЙ СТРАШНЫЙ МОНСТР 'ОЛЕГ'
ARCHER_TOWER_PATH='Z:\\pygame\\assets\\ART1.png'
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
TOWER_AREA_RADIUS = 50 #радиус куда можно поставить башню 
GAME_SPACE_WINDOW=pygame.display.set_mode ((WIN_WIDTH,WIN_HEIGHT)) #расширение монитора 
