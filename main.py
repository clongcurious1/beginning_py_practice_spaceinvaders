#import modules
import math
import pygame

#Initialize pygame
pygame.init()

#Create game window Set screen width, height
screen = pygame.display.set_mode((800,600))
#Run_window flashes but does not persist until master loop is created

#Game window_change title and icon
pygame.display.set_caption('Galactic Target Practice')
icon = pygame.image.load('alien.png')
pygame.display.set_icon(icon)

#player ship graphic and coordinates
playerImg = pygame.Image.load('space-invaders.png')
playerX = 370 #x axis
playerY = 480 #y axis

#create player function
def player(x, y):
#draw player graphic on screen using method .blit    
    screen.blit(playerImg, (x, y))

#Game Master Loop
#Allows game window to stay open while condition is met
running = True
while running:
    #Creates exit from infinite loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            running = False #Loop stops when someone tries to exit

#If keystroke pressed, note direction
if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_LEFT:
        print('left arrow is pressed')
    if event.key == pygame.K_RIGHT:
        print('right arrow is pressed')
if event.type == pygame.KEYUP:
    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        print('keystroke has been released')

#change color of game window background
screen.fill((0,0,0)) #black
player(playerX, playerY) #calling player to screen Allow for coordinates to change
pygame.display.update() #game display continually updates


