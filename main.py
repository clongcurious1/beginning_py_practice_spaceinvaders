#import modules
import pygame
import math

#Initialize pygame
pygame.init()

#Game window screen width, height
screen = pygame.display.set_mode((800,600))
#window flashes but does not persist until master loop is created

#Game window change title and icon
pygame.display.set_caption('Galactic Target Practice')
icon = pygame.image.load('alien.png')
pygame.display.set_icon(icon)

#load player image and coordinates
playerImg = pygame.image.load('space-invaders.png')
playerX = 370 #x axis
playerY = 480 #y axis

#draw player image on the screen
#send in changing values of x y coordinates
def player(x, y):
    screen.blit(playerImg, (x, y))

#Game Master Loop
#Allows game window to stay open while condition is met
running = True
while running:
    
    #change color of game window background
    screen.fill((0,0,0)) #black
    
    #Creates exit from infinite loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            running = False #Loop stops when someone tries to exit

    #After screen fills, player is drawn on top of filled screen
    player(playerX, playerY) #calling player to screen Allow for coordinates to change
    pygame.display.update() #game display continually updates

#If keystroke pressed, note direction
if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_LEFT:
        print('left arrow is pressed')
    if event.key == pygame.K_RIGHT:
        print('right arrow is pressed')
if event.type == pygame.KEYUP:
    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        print('keystroke has been released')




