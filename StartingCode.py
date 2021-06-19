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

#game loop variables

#game loop
while True:
    #clear screen
    screen.fill(black)

    #draw all items

    #conditions

    #check for events and chnage statuses/variables
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        #if conditions for keyboard and mouse movement

    #update
    pygame.display.update()
