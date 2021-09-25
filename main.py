#import modules
import pygame
import random
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

#load background image
background = pygame.image.load('universebackdrop.png')

#load player image and coordinates
playerImg = pygame.image.load('space-invaders.png')
#starting position is fixed
playerX = 370 #x axis
playerY = 480 #y axis
#x axis location does not change 
playerX_change = 0

#load enemy image and coordinates
enemyImg = pygame.image.load('angrygreenie.png')
#starting position is random
enemyX = random.randint(0, 736)
enemyY = random.randint(50, 150)
enemyX_change = 0

#draw player image on the screen
#send in changing values of x y coordinates
def player(x, y):
    screen.blit(playerImg, (x, y))

#draw enemy on the screen
def enemy(x, y):
    screen.blit(enemyImg, (x, y))

#Game Master Loop
#Allows game window to stay open while condition is met
running = True
while running:
    
    #change color of game window background
    screen.fill((0,0,0)) #black
    screen.blit(background, (0,0)) #draw background and cover the screen
    
    #Creates exit from infinite loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False #Loop stops when someone tries to exit

    #After screen fills, player and enemy are drawn on top of filled screen
    playerX += playerX_change
    player(playerX, playerY) #call player to screen, allow for coordinates to change
    enemy(enemyX, enemyY) #call enemy to screen, allow for coordinates to change
    pygame.display.update() #game display continually updates

    #If keystroke pressed, note direction
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -3 #move left along x-axis
            enemyX_change = -2 #moves slightly slower than player
        if event.key == pygame.K_RIGHT:
            playerX_change = 3 #move right along x-axis
            enemyX_change = 2 #moves slightly slower than player
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0 #stop moving when key is released

    #player boundary, keep ship on screen when moving L&R
    if playerX <= 32: #ship png is 32 pixels wide
        playerX = 33 #reset position create left-side buffer
    if playerX >= 768: #right side screen position minus width of ship png
        playerX = 767 #reset position create right-side buffer

    #enemy boundary, drop-down when reaching left or right boundary
    #enemies drop down until they get shot or until they drop below the x-axis location of the ship (game ends)
    if enemyX <= 32: #when edge of enemy touches LH border... 
        enemyX = 33 #enemy location on x-axis shifts to the right
    if enemyX >= 736: #when edge of enemy touches RH border...
        enemyX = -4 #reset RH enemy location on x-axis
        

