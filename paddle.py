import pygame
from pygame.constants import *

class Paddle(object):
    """Paletka"""

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.height = 75
        self.width = 25
        self.color = 255,255,255

    def moveDown(self):
        self.y += 1

    def moveUp(self):
        self.y -= 1

    def setPosition(self,x,y):
        self.x, self.y = x, y

    def draw(self,screen):
        self.img = pygame.Rect(self.x,self.y,self.width,self.height)
        pygame.draw.rect(screen,self.color,self.img)



