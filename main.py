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
enemyX_change = 0.3
enemyY_change = 30

#load bullet image and coordinates
bulletImg = pygame.image.load('artillery.png')
#bullet x-axis coordinate must be same as ship's x-coordinate
bulletX = 370
bulletY = 480 #shoots from top of player ship
bulletX_change = 0 #fires straight line so x-axis coordinate is constant 
bulletY_change = 10 #y-axis coordinate increases as bullets are fired + travel
bullet_state = "ready" #bullet is not seen on screen in ready state

score = 0

#draw player image on the screen
#send in changing values of x y coordinates
def player(x, y):
    screen.blit(playerImg, (x, y))

#draw enemy on the screen
def enemy(x, y):
    screen.blit(enemyImg, (x, y))

#draw bullets on screen
def bullet_fire (x, y):
#draw bullet at center of spaceship nose
    screen.blit(bulletImg, (x,  y + 10))
    global bullet_state 
    bullet_state = "fire"

#defining that Collision occurs based on distance between bullet and enemy
#using distance formula with square roots and exponential powers
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2))
    if distance< 27:
        return True
    else:
        return False

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

    #If keystroke pressed, note direction
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -1 #move left along x-axis
            if event.key == pygame.K_RIGHT:
                playerX_change = 1 #move right along x-axis
            if event.key == pygame.K_SPACE: #when space bar is pressed
                if bullet_state == "ready":
            #get current x-coordinate of player ship
            #store as bulletX
                    bulletX = playerX
                    bullet_fire(bulletX, bulletY)
    
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0 #stop moving when key is released
    
    #player boundary, keep ship on screen when moving L&R
    if playerX <= 0: #ship png is 32 pixels wide
        playerX = 33 #reset position create left-side buffer
    elif playerX >= 768: #right side screen position minus width of ship png
        playerX = 733 #reset position create right-side buffer

    #player movement
    playerX += playerX_change

    #enemy boundary, drop-down when reaching left or right boundary
    #enemies drop down until they get shot or until they drop below the ship's x-axis location (game ends)
    if enemyX <= 32: #when edge of enemy touches LH border... 
        enemyX_change = 0.5 #enemy location on x-axis shifts to the right
        enemyY += enemyY_change #and drops down on the screen
    elif enemyX >= 768: #when edge of enemy touches RH border...
        enemyX_change = -0.5 #reset RH enemy location on x-axis
        enemyY += enemyY_change #and drops down on the screen
        
    #enemy movement
    enemyX += enemyX_change

    if bullet_state == "fire":
    #when fired bullet travels independently of player x-coordinate
        bullet_fire(bulletX, bulletY) 
    
    #bullet movement
    bulletY -= bulletY_change 
    
    #reset bullet to starting point so you can fire again
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    
    #when Collision occurs
    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 480 #reset bullet to fire
        bullet_state = "ready"
        score += 1 #increase score by 1 each time enemy is shot
        print(score) #appears in terminal not on screen
        #after collision occurs enemy respawns to random location
        enemyX = random.randint(0, 736)
        enemyY = random.randint(50, 150)

    #After screen fills: player, enemy, bullets are drawn on top of filled screen
    # allow for coordinates to change    
    player(playerX, playerY) 
    enemy(enemyX, enemyY) 
    
    pygame.display.update() #game display continually updates
  
