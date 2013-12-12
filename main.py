import sys, pygame, paddle, ball
from pygame.constants import *

pygame.init()
pygame.key.set_repeat(1,2)
size = width, height = 900, 600
black = 0,0,0
stop = False

screen = pygame.display.set_mode(size)
player1 = paddle.Paddle(5,325)
player2 = paddle.Paddle(width-30,325)
ball1 = ball.Ball(width/2,height/2)

def reset():
    player1.setPosition(5, 325)
    player2.setPosition(width-30, 325)
    ball1.setPosition(width/2, height/2)

def drawScreen():
    screen.fill(black)
    player1.draw(screen)
    player2.draw(screen)
    ball1.draw(screen)
    pygame.display.flip()

def detectCollision():

    bounced = False
    dir = {"h":0,"v":0}

    # lewy gracz
    if ball1.img.left == player1.img.right:
        if not (ball1.img.bottom < player1.img.top or ball1.img.top > player1.img.bottom):
            bounced = True
            dir["h"] = 1
            if ball1.img.top < player1.img.top:
                return True, {"h":1,"v":-1}
            if ball1.img.bottom > player1.img.bottom:
                return  True, {"h":1,"v":1}

    # prawy gracz
    if ball1.img.right == player2.img.left:
        if not (ball1.img.bottom < player2.img.top or ball1.img.top > player2.img.bottom):
            bounced = True
            dir["h"] = 1
            if ball1.img.top < player2.img.top:
                return True, {"h":1,"v":-1}
            if ball1.img.bottom > player2.img.bottom:
                return  True, {"h":1,"v":1}

    # gorna krawedz
    if ball1.img.top == 0:
        bounced = True
        dir["v"] = 1
    elif ball1.img.bottom == height:
        bounced = True
        dir["v"] = -1

    return bounced, dir

def point():
    if ball1.img.left == 0:
        return -1
    if ball1.img.right == width:
        return 1
    return 0

def player1Control():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == K_UP and player1.img.top>=0 :
                player1.moveUp()
            elif event.key == K_DOWN and player1.img.bottom<=height :
                player1.moveDown()

def updateLogic():
    dir = {"h":0,"v":0}
    bounced = False
    score = 0

    player1Control()
    bounced, dir = detectCollision()

    if bounced:
        ball1.bounce(dir)

    score = point()
    ball1.move()
    if score != 0:
        reset()

while 1:
        drawScreen()
        updateLogic()
