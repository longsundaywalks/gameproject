#Main Class for Confidence Game

import pygame, sys
#from pygame.locals import *

#Game 

#Initialize pygame
pygame.init()
mainClock = pygame.time.Clock()

#Create the window for the game
window = pygame.display.set_mode((1000,600))
window.fill('#f88379')

#Title (bar heading)
pygame.display.set_caption("Confidence")
icon = pygame.image.load('Temp-Icon.png')
pygame.display.set_icon(icon)

#Game loop
running = True
while running:
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            

#Main menu
    #Declaring the font for text
    font = pygame.font.Font('freesansbold.ttf', 32)
 
# create a text surface object,
# on which text is drawn on it.
    text = font.render('Swiggity Swag', True, 'Green', 'Blue')
 
# create a rectangular object for the
# text surface object
    textRect = text.get_rect()
    #window.blit(text, textRect)