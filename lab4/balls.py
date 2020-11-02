import pygame
import random
from pygame.draw import *
from random import randint
pygame.init()

#Surfaces
f1 = pygame.font.SysFont('inkfree', 60)
f2 = pygame.font.SysFont('calibri', 48)

# Constants
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SKIN = (255, 229, 184)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
WIDTH = 1200
HEIGHT = 750
FPS = 60
G = 10
DT = 0.1

# Functions

# Drawing stars
def star(x, y, r, color):
    polygon(screen, color,
            [[int(x + r / 2), int(y + r)], [int(x), int(y - r)],
             [int(x - r / 2), int(y + r)], [int(x + r), int(y - r / 3)],
             [int(x - r), int(y - r / 3)], [int(x + r / 2), int(y + r)]])
    polygon(screen, WHITE,
            [[int(x + r // 2), int(y + r)], [int(x), int(y - r)],
             [int(x - r // 2), int(y + r)], [int(x + r), int(y - r // 3)],
             [int(x - r), int(y - r // 3)], [int(x + r // 2), int(y + r)]], 2)

# Creating objects on the screen: balls and stars
def new_balls():
    global a
    a = []
    n = randint(10, 15)
    for i in range (n):
        x = randint(100, WIDTH - 100)
        y = randint(100, HEIGHT - 100)
        dx = randint(2, 5) * random.choice([-1, 1])
        dy = randint(2, 5) * random.choice([-1, 1])
        r = randint(30, 90)
        color = COLORS[randint(0, 5)]
        flag = False
        a.append([x, y, dx, dy, r, color, flag])

def new_stars():
    global b
    b = []
    n = randint(3, 5)
    for i in range (n):
        x = randint(100, WIDTH - 100)
        y = randint(100, HEIGHT - 100)
        dx = randint(20, 50) * random.choice([-1, 1])
        dy = randint(60, 100) * random.choice([-1, 1])
        r = randint(30, 90)
        color = COLORS[randint(0, 5)]
        flag = False
        b.append([x, y, dx, dy, r, color, flag])

# Moving objects: a for balls, b for stars
def move_a():
    for i in range (len(a)):
        a[i][0] += a[i][2]
        a[i][1] += a[i][3]
        circle(screen, a[i][5], (a[i][0], a[i][1]), a[i][4])
        circle(screen, WHITE, (a[i][0], a[i][1]), a[i][4], 2)
        
def move_b():
    for i in range (len(b)):
        b[i][0] -= b[i][2] * DT
        b[i][3] -= G * DT
        b[i][1] -= b[i][3] * DT - G * (DT ** 2) / 2
        star(b[i][0], b[i][1], b[i][4], b[i][5])

# Reflecting objects if they bang in a wall
def reflect(a):
    for i in range (len(a)):
        if a[i][0] <= a[i][4] or a[i][0] >= WIDTH - a[i][4]:
            a[i][2] *= -1
        if a[i][1] <= a[i][4] or a[i][1] >= HEIGHT - a[i][4]:
            a[i][3] *= -1

# Giving points for clicking on an object: 1 for a ball, 3 for a star
def scores_a():
    kol = 0
    for i in range (len(a)):
        if ((event.pos[0]-a[i][0])**2 +
            (event.pos[1]-a[i][1])**2)**(1/2) <= a[i][4]:
            kol += 1
            a[i][6] = True
    return kol

def scores_b():
    kol = 0
    for i in range (len(b)):
        if ((event.pos[0]-b[i][0])**2 +
            (event.pos[1]-b[i][1])**2)**(1/2) <= b[i][4] // 2:
            kol += 3
            b[i][6] = True
    return kol

# Replacing an object with another one if it's clicked
def shift1(a):
    for i in range (len(a)):
        if a[i][6]:
            x = randint(100, WIDTH - 100)
            y = randint(100, HEIGHT - 100)
            dx = randint(2, 5) * random.choice([-1, 1])
            dy = randint(2, 5) * random.choice([-1, 1])
            r = randint(30, 90)
            color = COLORS[randint(0, 5)]
            flag = False
            a[i] = [x, y, dx, dy, r, color, flag]

# Deleting an object if it's clicked
def shift3(a):
    for i in range (len(a)-1, -1, -1):
        if a[i][6]:
            del a[i]

# Updating a leaders list
def write_leaders():
    f = open('leaders.txt', 'r')
    ind = 1
    flag = True
    lines = f.readlines()
    n = len(lines)
    while flag and n > 0:
        line = lines[len(lines) - n].split()
        if int(line[-1]) >= s:
            ind += 1
        else:
            flag = False
        n -= 1
    f.close()
    f = open('leaders.txt', 'w')
    if ind > len(lines):
        for i in range (len(lines)):
                f.write(lines[i])
        if ind < 11:
            f.write(str(ind) + '. ' + text + ' ' + str(s) + '\n')
    else:
        for i in range (ind-1):
                f.write(lines[i])
        f.write(str(ind) + '. ' + text + ' ' + str(s) + '\n')
        for i in range (ind-1, min(len(lines), 11)):
                f.write(str(i+2) + '. ' +
                        ' '.join(lines[i].split()[1:]) + '\n')
    f.close()

# THE GAME

# Primary settings
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.update()
clock = pygame.time.Clock()
finished = False
mode = 0
pygame.mixer.music.load('startmenu.mp3')
pygame.mixer.music.play()

# Main menu
while not finished:
    clock.tick(FPS)
    text1 = f1.render('KICK THE BALLS', True, RED)
    text2 = f2.render('Выберите режим:', True, RED)
    text3 = f2.render('• Бесконечный', True, RED)
    text4 = f2.render('• С таймером (соревновательный)', True, RED)
    text5 = f2.render('• На убирание шариков', True, RED)
    screen.blit(text1, (WIDTH // 2 - 270, HEIGHT // 2 - 285))
    screen.blit(text2, (WIDTH // 2 - 270, HEIGHT // 2 - 220))
    if pygame.mouse.get_focused():
        pos = pygame.mouse.get_pos()
        if WIDTH // 2 - 270 <= pos[0] <= WIDTH // 2 + 450:
            if HEIGHT // 2 - 160 <= pos[1] <= HEIGHT // 2 - 101:
                text3 = f2.render('• Бесконечный', True, RED, SKIN)
            elif HEIGHT // 2 - 100 <= pos[1] <= HEIGHT // 2 - 41:
                text4 = f2.render('• С таймером (соревновательный)',
                                  True, RED, SKIN)
            elif HEIGHT // 2 - 40 <= pos[1] <= HEIGHT // 2 + 19:
                text5 = f2.render('• На убирание шариков', True, RED, SKIN)
    screen.blit(text3, (WIDTH // 2 - 270, HEIGHT // 2 - 160))
    screen.blit(text4, (WIDTH // 2 - 270, HEIGHT // 2 - 100))
    screen.blit(text5, (WIDTH // 2 - 270, HEIGHT // 2 - 40))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if WIDTH // 2 - 230 <= pos[0] <= WIDTH // 2 + 253:
                finished = True
                if HEIGHT // 2 - 160 <= pos[1] <= HEIGHT // 2 - 101:
                    mode = 1
                elif HEIGHT // 2 - 100 <= pos[1] <= HEIGHT // 2 - 41:
                    mode = 2
                elif HEIGHT // 2 - 40 <= pos[1] <= HEIGHT // 2 + 19:
                    mode = 3
    pygame.display.update()
    screen.fill(BLACK)

# If the player has chosen a game mode, creating first objects
if mode:
    finished = False
new_balls()
new_stars()
for i in range (len(a)):
    circle(screen, a[i][5], (a[i][0], a[i][1]), a[i][4])
    circle(screen, WHITE, (a[i][0], a[i][1]), a[i][4], 2)
for i in range (len(b)):
    star(b[i][0], b[i][1], b[i][4], b[i][5])
s = 0

# Infinite mode
if mode == 1:
    pygame.mixer.music.load('undyne.mp3')
    pygame.mixer.music.play()
    while not finished:
        clock.tick(FPS)
        reflect(a)
        reflect(b)
        text1 = f2.render('Текущий счет: ' + str(s), True, RED)
        screen.blit(text1, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                s += scores_a()
                s += scores_b()
        move_a()
        move_b()
        shift1(a)
        shift1(b)
        pygame.display.update()
        screen.fill(BLACK)

# Competitive mode
elif mode == 2:
    time = 60
    ctrl = 0
    pygame.mixer.music.load('megalovania.mp3')
    pygame.mixer.music.play()
    while not finished:
        clock.tick(FPS)
        reflect(a)
        reflect(b)
        text1 = f2.render('Текущий счет: ' + str(s), True, RED)
        text2 = f2.render('Осталось времени: ' + str(time // 60) +
                          ':' + str(time % 60), True, RED)
        screen.blit(text1, (0, 0))
        screen.blit(text2, (WIDTH - 500, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                s += scores_a()
                s += scores_b()
        ctrl += 1
        if ctrl == FPS:
            time -= 1
            ctrl = 0
        move_a()
        move_b()
        shift1(a)
        shift1(b)
        pygame.display.update()
        screen.fill(BLACK)
        if time == 0:
            finished = True

# "Decreasing the amount of the balls" mode
elif mode == 3:
    pygame.mixer.music.load('core.mp3')
    pygame.mixer.music.play()
    while not finished:
        clock.tick(FPS)
        reflect(a)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                s += scores_a()
        move_a()
        shift3(a)
        pygame.display.update()
        screen.fill(BLACK)
        if len(a) == 0:
            finished = True

# Writing the player's name and his/her scores in a leaders list
if mode == 2:
    pygame.mixer.music.load('gameover.mp3')
    pygame.mixer.music.play()
    finished = False
    text = ''
    while not finished:
        clock.tick(FPS)
        text1 = f2.render('Введите свое имя: ', True, RED)
        text2 = f2.render(text, True, RED)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                elif event.key == pygame.K_RETURN:
                    finished = True
                    flag = True
                else:
                    text += event.unicode
        screen.blit(text1, (WIDTH // 2 - 230, HEIGHT // 2 - 160))
        screen.blit(text2, (WIDTH // 2 - 230, HEIGHT // 2 - 100))
        pygame.display.update()
        screen.fill(BLACK)    
    if flag:
        write_leaders()
        
pygame.quit()
