import webbrowser
import pygame
import random
import time
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("K&M Movement")
x = 300
y = 300
coordinates = (x,y)
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

letter = ""

#game loop
while True:
   
    #clear screen
    screen.fill(black)
   
    #draw all items
##    pygame.draw.circle(screen, green, coordinates, 30)
    show_text(letter, 30, 300, red)
   
    #check for events and change statuses/variables
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if (event.key >= 48 and event.key <=56) or (event.key >= 97 and event.key <= 123):
                letter += chr(event.key)
            elif event.key == 8:
                letter = letter[:-1]
            else:
                print("Invalid Input. This program only accepts numbers and lowercase letters")

           
    #update
    pygame.display.update()
