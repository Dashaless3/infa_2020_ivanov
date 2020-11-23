import pygame
import random
from pygame.draw import *
from random import randint
pygame.init()

#Surfaces
f1 = pygame.font.SysFont('inkfree', 60)
f2 = pygame.font.SysFont('calibri', 48)
f3 = pygame.font.SysFont('calibri', 30)

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
MODE = 0

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

# Moving objects: balls and stars
def move_balls():
    for i in range (len(a)):
        a[i][0] += a[i][2]
        a[i][1] += a[i][3]
        circle(screen, a[i][5], (a[i][0], a[i][1]), a[i][4])
        circle(screen, WHITE, (a[i][0], a[i][1]), a[i][4], 2)
        
def move_stars():
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
def scores_balls(event):
    kol = 0
    for i in range (len(a)):
        if ((event.pos[0]-a[i][0])**2 +
            (event.pos[1]-a[i][1])**2)**(1/2) <= a[i][4]:
            kol += 1
            a[i][6] = True
    return kol

def scores_stars(event):
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
    ind = 1
    try:
        f = open('leaders.txt', 'r')
        flag = True
        lines = f.readlines()
        n = len(lines)
        while flag and n > 0:
            line = lines[len(lines) - n].split()
            if int(line[-1]) >= scores:
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
                f.write(str(ind) + '. ' + text + ' ' + str(scores) + '\n')
        else:
            for i in range (ind-1):
                    f.write(lines[i])
            f.write(str(ind) + '. ' + text + ' ' + str(scores) + '\n')
            for i in range (ind-1, min(len(lines), 11)):
                    f.write(str(i+2) + '. ' +
                            ' '.join(lines[i].split()[1:]) + '\n')
        f.close()
    except FileNotFoundError:
        f = open('leaders.txt', 'w')
        f.write(str(ind) + '. ' + text + ' ' + str(scores) + '\n')

# Main menu
def main_menu():
    global MODE
    finished = False
    ne_pravila = True
    pygame.mixer.music.load('startmenu.mp3')
    pygame.mixer.music.play()
    while not finished:
        clock.tick(FPS)
        text1 = f1.render('KICK THE BALLS', True, RED)
        text2 = f2.render('Выберите режим:', True, RED)
        text3 = f2.render('• Бесконечный', True, RED)
        text4 = f2.render('• С таймером (соревновательный)', True, RED)
        text5 = f2.render('• На убирание шариков', True, RED)
        text6 = f2.render('Правила игры', True, RED)
        nazad = f2.render('• В главное меню', True, RED)
        pravila1 = f3.render('• В бесконечном режиме Вы можете неограниченно лопать шарики и звезды,', True, RED)
        pravila2 = f3.render('вместо которых появляются новые. За каждый убранный шарик Вы получаете', True, RED)
        pravila3 = f3.render('по одному очку, за каждую убранную звезду - по три. Свои очки Вы можете', True, RED)
        pravila4 = f3.render('видеть в левом верхнем углу. Результат нигде не сохраняется.', True, RED)
        pravila5 = f3.render('• В режиме с таймером Вам предстоит за минуту набрать как можно больше', True, RED)
        pravila6 = f3.render('очков. Фигуры те же - звезды и шарики. Ваш результат по желанию будет', True, RED)
        pravila7 = f3.render('сохранен в таблицу лидеров - так все смогут позавидовать Вашему мастерству.', True, RED)
        pravila8 = f3.render('• Режим с убиранием шариков самый скучный - Вы можете лопнуть все', True, RED)
        pravila9 = f3.render('летающие на экране шарики, после чего игра закончится. А можете не лопать.', True, RED)
        if pygame.mouse.get_focused():
            pos = pygame.mouse.get_pos()
            if ne_pravila:
                if WIDTH // 2 - 270 <= pos[0] <= WIDTH // 2 + 450:
                    if HEIGHT // 2 - 160 <= pos[1] <= HEIGHT // 2 - 101:
                        text3 = f2.render('• Бесконечный', True, RED, SKIN)
                    elif HEIGHT // 2 - 100 <= pos[1] <= HEIGHT // 2 - 41:
                        text4 = f2.render('• С таймером (соревновательный)',
                                          True, RED, SKIN)
                    elif HEIGHT // 2 - 40 <= pos[1] <= HEIGHT // 2 + 19:
                        text5 = f2.render('• На убирание шариков', True, RED, SKIN)
                    elif HEIGHT // 2 + 20 <= pos[1] <= HEIGHT // 2 + 79:
                        text6 = f2.render('Правила игры', True, RED, SKIN)
            else:
                if WIDTH // 2 - 270 <= pos[0] <= WIDTH // 2 + 450 and HEIGHT // 2 - 220 <= pos[1] <= HEIGHT // 2 - 161:
                    nazad = f2.render('• В главное меню', True, RED, SKIN)
        if ne_pravila:
            screen.blit(text1, (WIDTH // 2 - 270, HEIGHT // 2 - 285))
            screen.blit(text2, (WIDTH // 2 - 270, HEIGHT // 2 - 220))
            screen.blit(text3, (WIDTH // 2 - 270, HEIGHT // 2 - 160))
            screen.blit(text4, (WIDTH // 2 - 270, HEIGHT // 2 - 100))
            screen.blit(text5, (WIDTH // 2 - 270, HEIGHT // 2 - 40))
            screen.blit(text6, (WIDTH // 2 - 270, HEIGHT // 2 + 20))
        else:
            screen.blit(nazad, (WIDTH // 2 - 270, HEIGHT // 2 - 220))
            screen.blit(pravila1, (WIDTH // 2 - 470, HEIGHT // 2 - 170))
            screen.blit(pravila2, (WIDTH // 2 - 470, HEIGHT // 2 - 140))
            screen.blit(pravila3, (WIDTH // 2 - 470, HEIGHT // 2 - 110))
            screen.blit(pravila4, (WIDTH // 2 - 470, HEIGHT // 2 - 80))
            screen.blit(pravila5, (WIDTH // 2 - 470, HEIGHT // 2 - 40))
            screen.blit(pravila6, (WIDTH // 2 - 470, HEIGHT // 2 - 10))
            screen.blit(pravila7, (WIDTH // 2 - 470, HEIGHT // 2 + 20))
            screen.blit(pravila8, (WIDTH // 2 - 470, HEIGHT // 2 + 60))
            screen.blit(pravila9, (WIDTH // 2 - 470, HEIGHT // 2 + 90))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if ne_pravila:
                    if WIDTH // 2 - 230 <= pos[0] <= WIDTH // 2 + 253:
                        if HEIGHT // 2 - 160 <= pos[1] <= HEIGHT // 2 - 101:
                            MODE = 1
                            finished = True
                        elif HEIGHT // 2 - 100 <= pos[1] <= HEIGHT // 2 - 41:
                            MODE = 2
                            finished = True
                        elif HEIGHT // 2 - 40 <= pos[1] <= HEIGHT // 2 + 19:
                            MODE = 3
                            finished = True
                        elif HEIGHT // 2 + 20 <= pos[1] <= HEIGHT // 2 + 79:
                            ne_pravila = False
                else:
                    if WIDTH // 2 - 230 <= pos[0] <= WIDTH // 2 + 253 and HEIGHT // 2 - 220 <= pos[1] <= HEIGHT // 2 - 161:
                        ne_pravila = True
        pygame.display.update()
        screen.fill(BLACK)

# If the player has chosen a game mode, creating first objects
def first_balls():
    new_balls()
    for i in range (len(a)):
        circle(screen, a[i][5], (a[i][0], a[i][1]), a[i][4])
        circle(screen, WHITE, (a[i][0], a[i][1]), a[i][4], 2)
        
def first_stars():
    new_stars()
    for i in range (len(b)):
        star(b[i][0], b[i][1], b[i][4], b[i][5])
    

# Infinite mode
def infinite_mode():
    first_balls()
    first_stars()
    scores = 0
    finished = False
    pygame.mixer.music.load('undyne.mp3')
    pygame.mixer.music.play()
    while not finished:
        clock.tick(FPS)
        reflect(a)
        reflect(b)
        text1 = f2.render('Текущий счет: ' + str(scores), True, RED)
        screen.blit(text1, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                scores += scores_balls(event)
                scores += scores_stars(event)
        move_balls()
        move_stars()
        shift1(a)
        shift1(b)
        pygame.display.update()
        screen.fill(BLACK)

# Competitive mode
def competitive_mode():
    global hochu_igrat, scores
    first_balls()
    first_stars()
    finished = False
    time = 60
    frapes = 0
    scores = 0
    pygame.mixer.music.load('megalovania.mp3')
    pygame.mixer.music.play()
    hochu_igrat = True
    while not finished:
        clock.tick(FPS)
        reflect(a)
        reflect(b)
        text1 = f2.render('Текущий счет: ' + str(scores), True, RED)
        text2 = f2.render('Осталось времени: ' + str(time // 60) +
                          ':' + str(time % 60), True, RED)
        screen.blit(text1, (0, 0))
        screen.blit(text2, (WIDTH - 500, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
                hochu_igrat = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                scores += scores_balls(event)
                scores += scores_stars(event)
        frapes += 1
        if frapes == FPS:
            time -= 1
            frapes = 0
        move_balls()
        move_stars()
        shift1(a)
        shift1(b)
        pygame.display.update()
        screen.fill(BLACK)
        if time == 0:
            finished = True

# "Decreasing the amount of the balls" mode
def decreasing_mode():
    first_balls()
    finished = False
    scores = 0
    pygame.mixer.music.load('core.mp3')
    pygame.mixer.music.play()
    while not finished:
        clock.tick(FPS)
        reflect(a)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                scores += scores_balls(event)
        move_balls()
        shift3(a)
        pygame.display.update()
        screen.fill(BLACK)
        if len(a) == 0:
            finished = True

# Writing the player's name and his/her scores in a leaders list
def update_leaders_list():
    global text
    pygame.mixer.music.load('gameover.mp3')
    pygame.mixer.music.play()
    finished = False
    text = ''
    flag = False
    time = 0
    while not finished:
        clock.tick(FPS)
        time += 1
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
        text3 = text
        if 40 < time % 80 <= 80:
            text3 = text3 + 'l'
        text1 = f2.render('Введите свое имя: ', True, RED)
        text2 = f2.render(text3, True, RED)
        screen.blit(text1, (WIDTH // 2 - 230, HEIGHT // 2 - 160))
        screen.blit(text2, (WIDTH // 2 - 230, HEIGHT // 2 - 100))
        pygame.display.update()
        screen.fill(BLACK)    
    if flag:
        write_leaders()

# The game
def game():
    # Primary settings
    global screen, clock
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.update()
    clock = pygame.time.Clock()
    
    # Sequence of game functions
    main_menu()
    if MODE == 1:
        infinite_mode()
    elif MODE == 2:
        competitive_mode()
        if MODE == 2 and hochu_igrat:
            update_leaders_list()
    elif MODE == 3:
        decreasing_mode()
    pygame.quit()

game()
