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
#starting position
playerX = 370 #x axis
playerY = 480 #y axis
#x axis location does not change 
playerX_change = 0

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
        if event.type == pygame.QUIT:
            running = False #Loop stops when someone tries to exit

    
    #After screen fills, player is drawn on top of filled screen
    playerX += playerX_change
    player(playerX, playerY) #calling player to screen Allow for coordinates to change
    pygame.display.update() #game display continually updates

    #If keystroke pressed, note direction
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -0.3 #move left along x-axis
        if event.key == pygame.K_RIGHT:
            playerX_change = 0.3 #move right along x-axis
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0 #stop moving when key is released

    #add boundary to keep ship on screen when moving L&R
    if playerX <= 32: #ship png is 32 pixels wide
        playerX = 33 #reset position create left-side buffer
    if playerX >= 768: #right side screen position minus width of ship png
        playerX = 767 #reset position create right-side buffer


