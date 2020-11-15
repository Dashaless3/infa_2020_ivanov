import pygame
from pygame.draw import *
pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
screen = pygame.display.set_mode((500, 500))

rect(screen, (255, 0, 255), (100, 100, 200, 200))
rect(screen, (0, 0, 255), (100, 100, 200, 200), 5)
polygon(screen, (255, 255, 0), [(100,100), (200,50),
                               (300,100), (100,100)])
polygon(screen, (0, 0, 255), [(100,100), (200,50),
                               (300,100), (100,100)], 5)
circle(screen, (0, 255, 0), (200, 175), 50)
circle(screen, (255, 255, 255), (200, 175), 50, 5)
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
