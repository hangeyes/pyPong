import pygame, paddle
from pygame.constants import *

class Ball(object):

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = self.height = 20
        self.color = 150,150,150
        self.direction = {"vertical":0,"horizontal":-1}

    def move(self):
        self.x += self.direction["horizontal"]
        self.y += self.direction["vertical"]

    def bounce(self,dir):
        if dir["h"] == 1:
            self.direction["horizontal"] = -self.direction["horizontal"]
        if dir["v"] == 1:
            if self.direction["vertical"] < 1:
                self.direction["vertical"] += 1
        elif dir["v"] == -1:
            if self.direction["vertical"] > -1:
                self.direction["vertical"] -= 1


    def draw(self,screen):
        self.img = pygame.Rect(self.x,self.y,self.width,self.height)
        pygame.draw.rect(screen,self.color,self.img)





