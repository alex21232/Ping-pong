#importar librerias
from pickletools import pyfloat
import pygame

#Initializa pygame
pygame.init()

#window size
screen_windth = 800
screen_height = 600

# size variable
size = (screen_windth, screen_height)

#show window
screen = pygame.display.set_mode(size)

#Game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False