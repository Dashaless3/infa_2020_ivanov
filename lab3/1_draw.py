import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 500))

rect(screen, (217, 217, 217), (0, 0, 500, 500))
circle(screen, (255, 255, 0), (255, 255), 125)
circle(screen, (0, 0, 0), (255, 255), 125, 1)
line(screen, (0, 0, 0), (188, 324), (314, 324), 20)
circle(screen, (255, 0, 0), (188, 225), 25)
circle(screen, (0, 0, 0), (188, 225), 25, 1)
circle(screen, (0, 0, 0), (188, 225), 10)
circle(screen, (255, 0, 0), (314, 225), 20)
circle(screen, (0, 0, 0), (314, 225), 20, 1)
circle(screen, (0, 0, 0), (314, 225), 10)
line(screen, (0, 0, 0), (126, 149), (225, 213), 15)
line(screen, (0, 0, 0), (278, 213), (376, 174), 15)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
