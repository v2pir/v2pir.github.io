#import modules
import pygame
from pygame.locals import *
import random
import webbrowser
import time
import math

#initialize pygame
pygame.init()

#open pygame window
size = (600, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tic Tac Toe")

#Define some colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
purple = (255, 0, 255)
aqua = (0, 200, 150)

#initial variables
x = 300
y = 300
coordinates = (x,y)

#fps
clock = pygame.time.Clock()

#define functions
def midpoint(x,y,x1,y1):
    midpoint = (((x+x1)/2), ((y+y1)/2))
    return midpoint

def show_text(msg, x, y, color):
    fontobj = pygame.font.SysFont("comicsansms", 25)
    msgobj = fontobj.render(msg, False, color)
    screen.blit(msgobj,(x,y))

def draw_x(x,y):
    pygame.draw.line(screen, white, (x,y), (x+200, y+200), 5)
    pygame.draw.line(screen, white, (x+200, y), (x, y+200), 5)

def draw_o(x,y):
    pygame.draw.circle(screen, white, (x+100, y+100), 100, 3)
    d = (x/200) + (3*(y/200))

def grid():
    pygame.draw.line(screen, white, (0,0), (0,600), 5)
    for lines in range(1, 4):
        pygame.draw.line(screen, white, (lines*200, 0), (lines*200, 600), 5)
    pygame.draw.line(screen, white, (0,0), (600, 0), 5)
    for sidelines in range(1,4):
        pygame.draw.line(screen, white, (0, sidelines*200), (600, sidelines*200), 5)

#variables for game loop
running = True #While loop is running
turn = True #If true, then X's turn. If false, then O's turn.
change = 1 #If 1, then X's turn. If -1, then O's turn.
#"0" represents top left, "1" represents top middle, "2" represents top right, etc...
D = {0:"", 1:"", 2:"", 3:"", 4:"", 5:"", 6:"", 7:"", 8:""}
#main game loop
while running:

    #draws grid
    grid()

    #set fps
    clock.tick(60)

    #main event loop
    for event in pygame.event.get():
        if event.type == pygame.quit:
            running = False
            exit()

        #if mouse is clicked
        if event.type == MOUSEBUTTONDOWN:
            
#------------------------conditions for drawing X---------------------
            
            if change == 1:
                #finds if cursor is in a specific box
                thingx = (event.pos[0]//200)*200
                thingy = (event.pos[1]//200)*200
                #proceeds to drawing X
                turn = True

#------------------------conditions for drawing O----------------------
                
            if change == -1:
                #finds if cursor is in a specific box
                thingx = (event.pos[0]//200)*200 
                thingy = (event.pos[1]//200)*200
                #proceeds to drawing O
                turn = False

            #make dictionary key in terms of where mouse clicked
            d = (thingx/200) + (3*(thingy/200))

#-----------------------If it is __ Player's turn----------------------
            
            if turn == True: #If it is X's turn
                if D[d] == "": #Makes sure there is nothing in the spot clicked
                    D[d] = "X" #If nothing is in the spot, add X
                    draw_x(thingx,thingy) #draw X on display
                    change = -1 #Switch to O
                    
            elif turn == False: #if it is O's turn
                if D[d] == "": #Makes sure there is nothing in the spot clicked
                    D[d] = "O" #If nothing is in the spot, add O
                    draw_o(thingx, thingy)#draw O on the display
                    change = 1#Switch to X

 #---------------------------Winning Conditions-------------------------
                    
                #if X/O is in this specific order, then X/O wins
                if  (D[0] == D[1] == D[2] == "X") or\
                    (D[3] == D[4] == D[5] == "X") or\
                    (D[6] == D[7] == D[8] == "X") or\
                    (D[0] == D[3] == D[6] == "X") or\
                    (D[1] == D[4] == D[7] == "X") or\
                    (D[2] == D[5] == D[8] == "X") or\
                    (D[0] == D[4] == D[8] == "X") or\
                    (D[2] == D[4] == D[6] == "X"):
                        screen.fill(black)
                        show_text("Player X wins!", 220, 300, green)
                        
                if  (D[0] == D[1] == D[2] == "O") or\
                    (D[3] == D[4] == D[5] == "O") or\
                    (D[6] == D[7] == D[8] == "O") or\
                    (D[0] == D[3] == D[6] == "O") or\
                    (D[1] == D[4] == D[7] == "O") or\
                    (D[2] == D[5] == D[8] == "O") or\
                    (D[0] == D[4] == D[8] == "O") or\
                    (D[2] == D[4] == D[6] == "O"):
                        screen.fill(black)
                        show_text("Player O wins!", 220, 300, green)
        
    #update screen
    pygame.display.update()
