import sys, pygame, paddle, ball
from pygame.constants import *

pygame.init()
pygame.key.set_repeat(1,2)
size = width, height = 900, 600
black = 0,0,0
stop = False

screen = pygame.display.set_mode(size)
player1 = paddle.Paddle(5,375)
player2 = paddle.Paddle(width-30,375)
ball1 = ball.Ball(width/2,height/2)

def drawScreen():
    screen.fill(black)
    player1.draw(screen)
    player2.draw(screen)
    ball1.draw(screen)
    pygame.display.flip()

def updateLogic():
    dir = {"h":0,"v":0}
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == K_UP and player1.img.top>=0 :
                player1.moveUp()
            elif event.key == K_DOWN and player1.img.bottom<=height :
                player1.moveDown()
    ball1.move()



while 1:
        drawScreen()
        updateLogic()
