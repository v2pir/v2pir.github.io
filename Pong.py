import webbrowser
import pygame
import random
import time
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Pong")
blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
purple = (255,0,255)
black = (0,0,0)
white = (255,255,255)
yellow = (255,255,0)
orange = (255,128,0)
aqua = (0,204,204)
pink = (175,0,175)
grey = (127.5, 127.5, 127.5)
y1 = 250
y2 = 250
clock = pygame.time.Clock()

colors = [blue, red, green, purple, white, yellow, orange, aqua, pink]
width = random.randint(50,100)
height = random.randint(50,100)

def randcolor():
    randomcolor = (random.randint(10,245), random.randint(10,245), random.randint(10,245))
    return randomcolor

def show_text(msg, x, y, color):
    fontobj = pygame.font.SysFont("comicsansms", 32)
    msgobj = fontobj.render(msg, False, color)
    screen.blit(msgobj,(x,y))

def rekt_center(x, y, width, height):
    mid_x = (x + width)/2
    mid_y = (y + height)/2
    center = (mid_x, mid_y)
    return center

#paddle variables
go_up = False
go_down = False
go_up1 = False
go_down1 = False

#ball variables
x = 300
y = 300
ballcenter = (x,y)
ballmovex = True
ballmovey = True

#score
leftscore = 0
rightscore = 0

#game loop
while True:
   
    #clear screen
    screen.fill(black)
   
    #draw all items
    ball = pygame.draw.circle(screen, green, (x,y), 20)
    leftpaddle = pygame.draw.rect(screen, green, (0, y1, 30, 100))
    rightpaddle = pygame.draw.rect(screen, green, (570, y2, 30, 100))

    #paddles conditions
    clock.tick(144)
    if go_up == True:
        y1 -= 1
    if go_down == True:
        y1 += 1
    if go_down1 == True:
        y2 += 1
    if go_up1 == True:
        y2 -= 1

    #making sure paddles don't go offscreen
    if y1 < 0:
        y1 = 0
    if y1 > 500:
        y1 = 500
    if y2 < 0:
        y2 = 0
    if y2 > 500:
        y2 = 500

    #ball conditions
    if ballmovex == True:
        x += 1
    if ballmovex == False:
        x -= 1
    if x > 580:
        time.sleep(1)
        leftscore += 1
        x = 300
        y = 300
    if x < 0:
        time.sleep(1)
        rightscore += 1
        x = 300
        y = 300
    if ballmovey == True:
        y += 1
    if ballmovey == False:
        y -= 1
    if y > 580:
        ballmovey = False
    if y < 20:
        ballmovey = True

    #collision detection and scoring
    if ball.colliderect(rightpaddle):
        ballmovex = False
    if ball.colliderect(leftpaddle):
        ballmovex = True

    #displaying score
    show_text("Score = " + str(rightscore), 400, 40, yellow)
    show_text("Score = " + str(leftscore), 50, 40, yellow)

   #winner conditions
    if rightscore >= 5:
        show_text("RIGHT PLAYER WINS!", 150, 284, yellow)
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        exit()
    if leftscore >= 5:
        show_text("LEFT PLAYER WINS!", 150, 284, yellow)
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        exit()
   
    #check for events and change statuses/variables
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                go_up1 = True
            if event.key == K_w:
                go_up = True
            if event.key == K_DOWN:
                go_down1 = True
            if event.key == K_s:
                go_down = True
        if event.type == KEYUP:
            go_up = False
            go_up1 = False
            go_down = False
            go_down1 = False

    #update
    pygame.display.update()
