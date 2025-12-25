import pygame
import sys 
from colors import *

pygame.init()
pygame.display.set_caption("PG01")
screen = pygame.display.set_mode((1280, 720))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTON:
            print(event.pos)
    

    screen.fill(Colors.ALICEBLUE)
    pygame.draw.rect(screen, Colors.GREEN, (200, 200, 20, 20))

    pygame.display.flip()
