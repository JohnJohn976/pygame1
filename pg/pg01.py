import pygame
import sys 
from colors import *

pygame.init()
pygame.display.set_caption("PG01")
screen = pygame.display.set_mode((800, 600))

screen.fill(Colors.ALICEBLUE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('hi')
            pygame.quit()
            sys.exit()

    pygame.display.flip() 
