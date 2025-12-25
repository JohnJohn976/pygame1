import pygame
import sys 
from colors import *
pygame.init()
pygame.display.set_caption("PG03")
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
dt = 0

p = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
print(p, p.x, p.y)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill(Colors.ALICEBLUE)
    pygame.draw.circle(screen, Colors.RED, p, 20)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        p.y -= 300 * dt
    if keys[pygame.K_s]:
        p.y += 300 * dt
    if keys[pygame.K_a]:
        p.x, -= 300 + dt
    if keys[pygame.K_d]:
        p.x += 300 + dt
    
    pygame.display.flip()
    dt = clock.tick(50) / 1000