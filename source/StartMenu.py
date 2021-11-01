from game import *
import pygame
from Init import *

class StartMenu:
    def __init__(self, window):
        self.width = WIN_WIDTH #ширина
        self.height = WIN_HEIGHT #высота 
        self.startMenuWindow = window  #окно игры 
        self.backgroundImage = pygame.image.load(BACKGROUND_PATH) # карта
        self.backgroundImage = pygame.transform.scale(self.backgroundImage,(self.width,self.height)) # автоматическая  смена расширение для других мониторов  
        self.startButtonPosition = START_BUTTON_POSITION
        self.startButtonImage= pygame.image.load(START_BUTTON_PATH)
    def run(self):
        Running = True

        while Running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Running = False
                if event.type == pygame.MOUSEBUTTONUP:
                    currentMousePosition = pygame.mouse.get_pos()
                    if  self.startButtonPosition[0]-self.startButtonImage.get_width()/2<= currentMousePosition[0] <=  self.startButtonPosition[0]+self.startButtonImage.get_width()/2:
                        if self.startButtonPosition[1]-self.startButtonImage.get_height()/2<= currentMousePosition[1] <=  self.startButtonPosition[1]+self.startButtonImage.get_height()/2:
                            newGame = Game(self.startMenuWindow)
                            newGame.run()
                            del newGame
            self.draw()       
        pygame.quit()
    
    def draw(self):
        self.startMenuWindow.blit(self.backgroundImage,(0,0))
        self.startMenuWindow.blit(self.startButtonImage,self.startButtonPosition)
        pygame.display.update()

starter = StartMenu(GAME_SPACE_WINDOW)
starter.run()