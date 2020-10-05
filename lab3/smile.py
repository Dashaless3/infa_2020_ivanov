import pygame
from pygame.draw import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
FPS = 30

rect(screen, (170, 170, 170), (0, 0, 800, 600))
circle(screen, (255, 255, 0), (400, 300), 100)
circle(screen, (0, 0, 0), (400, 300), 100, 1)
circle(screen, (255, 0, 0), (350, 280), 20)
circle(screen, (0, 0, 0), (350, 280), 20, 1)
circle(screen, (255, 0, 0), (450, 280), 17)
circle(screen, (0, 0, 0), (450, 280), 17, 1)
circle(screen, (0, 0, 0), (350, 280), 8)
circle(screen, (0, 0, 0), (450, 280), 8)
line(screen, (0, 0, 0), [380, 270], [300, 220], 12)
line(screen, (0, 0, 0), [420, 270], [500, 240], 12)
line(screen, (0, 0, 0), [350, 350], [450, 350], 20)

pygame.display.update()

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
#7 и 17s
