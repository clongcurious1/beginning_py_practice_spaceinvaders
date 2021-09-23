#import modules
import math
import pygame

#Initialize pygame
pygame.init()

#Create game window Establish screen width, height
screen = pygame.display.set_mode((800,600))
#Run_window flashes but does not persist until master loop is created

#Game window_change title and icon
pygame.display.set_caption('Galactic Target Practice')
icon=pygame.image.load('alien.png')
pygame.display.set_icon(icon)

#player ship graphic and coordinates
playerImg = pygame.Image.load('space-invaders.png')
playerX = 370
playerY = 480
#draw player graphic on screen using method .blit
def player():
    screen.blit(playerImg, (playerX, playerY))

#Game Master Loop
#Allows game window to stay open or persist
running = True
while running:
    #Creates exit from infinite loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            running = False #Loop stops when someone tries to exit

#change color of game window background
screen.fill((0,0,0))#black
#draw player ship on screen background
player()
pygame.display.update()#game display continually updates

