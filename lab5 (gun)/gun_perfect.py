from random import *
import tkinter as tk
import math
import time
import sys

class bomb():
    """Бомба."""
    def __init__(self, x=0, y=0, side='right'):
        """Конструктор класса.
        Параметры: координаты, начальная скорость по вертикали,
        размеры изображения, вертикальное ускорение, направление
        изображения (смотрит вправо или влево), название файла
        с изображением, флаг "существования"."""
        self.x=x
        self.y=y
        self.vy=0
        self.rx = 75
        self.ry = 45
        self.g=0.03
        self.side=side
        self.image = ''
        self.exist = 1
    def move(self, t):
        """Перемещение бомбы по прошествии единицы времени.
        Метод описывает перемещение бомбы за один кадр перерисовки:
        обновляет значение self.y с учетом скорости self.vy (так как
        движение только по вертикали), силы гравитации, действующей
        на бомбу, и краев игрового поля (высота - 550)."""
        self.check_exist()
        self.check_hit(t)
        self.y += self.vy
        self.vy += self.g
    def check_exist(self):
        """Проверка существования бомбы: удаление, если координата
        по вертикали превысила высоту экрана."""
        if self.y > 550-self.ry:
            self.exist = 0
    def check_hit(self, obj):
        """Проверка столкновения с танком.
        Переменная obj - танк, с которым проверяется столкновение.
        Если бомба столкнулась с танком, бомба исчезает, а здоровье
        танка уменьшается на 10."""
        if abs(self.y-obj.y) <= abs((self.ry + obj.ry)/2) and abs(
            self.x - obj.x) <= abs((self.rx + obj.rx)/2):
            self.exist = 0
            obj.health -= 10

class cannonball():
    """Пушечное ядро."""
    def __init__(self, x, y):
        """ Конструктор класса.
        Переменные:
        x - начальное положение ядра по горизонтали,
        y - начальное положение ядра по вертикали.
        Параметры: кординаты, радиус, скорости, вертикальное
        ускорение, изображение ядра на экране, флаг
        "существования"."""
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 3
        self.vy = 3
        self.g = 0.3
        self.color = 'gray'
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )
        self.exist = 1

    def move(self):
        """Перемещение ядра по прошествии единицы времени.
        Метод описывает перемещение ядра за один кадр перерисовки:
        обновляет значения self.x и self.y с учетом скоростей self.vx
        и self.vy, силы гравитации, действующей на ядро, и краев
        игрового поля (размер - 1280x550)."""
        self.vy -= self.g
        self.x += self.vx
        self.y -= self.vy
        canv.delete(self.id)
        
        if self.x >= 1280 - self.r or self.x <= self.r or self.y >= 550 - self.r:
            self.exist = 0
            
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )

    def didhit(self, obj):
        """Функция проверяет, сталкивалкивается ли ядро с целью, описываемой
        в обьекте obj. Переменная obj - объект, с которым проверяется столкновение.
        Возвращает True в случае столкновения ядра и объекта. В противном случае
        возвращает False."""
        if abs(self.y-obj.y) <= abs(self.r + obj.ry/2) and abs(
            self.x - obj.x) <= abs(self.r + obj.rx/2):
            self.exist = 0
            return True
        else:
            return False

class rocket():
    """Ракета."""
    def __init__(self, x, y):
        """ Конструктор класса.
        Переменные:
        x - начальное положение ядра по горизонтали,
        y - начальное положение ядра по вертикали.
        Параметры: координаты, размер изображения, скорости,
        вертикальное ускорение, название файла с изображением,
        флаг "существования"."""
        self.x = x
        self.y = y
        self.rx = 50
        self.ry = 35
        self.vx = 10
        self.vy = 10
        self.g = 0.3
        self.image = 'ракетаr.png'
        self.exist = 1
        
    def move(self):
        """Перемещение ракеты по прошествии единицы времени.
        Метод описывает перемещение ракеты за один кадр перерисовки:
        обновляет значения self.x и self.y с учетом скоростей self.vx
        и self.vy, силы гравитации, действующей на ракету, и краев
        игрового поля (размер - 1280x550)."""
        self.vy -= self.g
        self.x += self.vx
        self.y -= self.vy
        
        if self.x >= 1280 - self.rx or self.x <= self.rx or self.y >= 550 - self.ry:
            self.exist = 0
            
    def didhit(self, obj):
        """Функция проверяет, сталкивалкивается ли ракета с целью, описываемой
        в обьекте obj. Переменная obj - объект, с которым проверяется столкновение.
        Возвращает True в случае столкновения ракеты и объекта. В противном случае
        возвращает False."""
        if abs(self.y-obj.y) <= abs((self.ry + obj.ry)/2) and abs(
            self.x - obj.x) <= abs((self.rx + obj.rx)/2):
            self.exist = 0
            return True
        else:
            return False

class playertank():
    """Игровой танк."""
    def __init__(self, tank):
        """Конструктор класса.
        Параметры танка: координаты, название файла с изображением,
        скорости, размер изображения, здоровье, сила выстрела,
        угол вылета снаряда, количество оставшихся снарядов."""
        self.x=20
        self.y=450
        self.image = tank
        self.vx=5
        self.vy=5
        self.rx = 89
        self.ry = 71
        self.health = 100
        self.f1_power = 1
        self.f1_on = 0
        self.f2_power = 1
        self.f2_on = 0
        self.an = 0
        self.balls = 5
        self.rockets = 1
    def recalc_radius(self):
        """Пересчет размера изображения танка для правильного распознавания
        момента столкновения между танком и снарядом."""
        if self.image[4] in ['r', 'l']:
            self.rx = 89
            self.ry = 71
        else:
            self.rx = 71
            self.ry = 89
    def move(self, event):
        """Движение танка за один кадр перерисовки. В зависимости от нажатой
        кнопки переключается изображение и меняющаяся координата."""
        global who_is_player
        self.recalc_radius()
        if event.keysym == 'Up' and self.y > 78:
            self.y -= self.vy
            self.image = self.image[:5]+'u.png'
        elif event.keysym == 'Down' and self.y < 550 - self.ry - 5:
            self.y += self.vy
            self.image = self.image[:5]+'d.png'
        elif event.keysym == 'Left' and self.x > 640*(who_is_player-1) + 4:
            self.x -= self.vx
            self.image = self.image[:5]+'l.png'
        elif event.keysym == 'Right' and self.x < 640*who_is_player-self.rx-20:
            self.x += self.vx
            self.image = self.image[:5]+'r.png'
        x = self.x
        y = self.y
    def fire1_start(self, event):
        """Запуск процесса усиления пушки для выстрела ядром."""
        if self.balls > 0:
            self.f1_on = 1

    def fire1_end(self, event):
        """Выстрел ядром.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости ядра vx и vy зависят от положения
        мыши."""
        global cannonballs
        if self.balls > 0:
            self.balls -= 1
            new_cannonball = cannonball(self.x, self.y)
            try:
                self.an = math.atan((event.y-new_cannonball.y) / (event.x-new_cannonball.x))
            except ZeroDivisionError:
                self.an = math.atan(-1)
            if event.x > new_cannonball.x:
                new_cannonball.vx = self.f1_power * new_cannonball.vx * math.cos(self.an)
                new_cannonball.vy = -self.f1_power * new_cannonball.vy * math.sin(self.an)
            else:
                new_cannonball.vx = -self.f1_power * new_cannonball.vx * math.cos(self.an)
                new_cannonball.vy = self.f1_power * new_cannonball.vy * math.sin(self.an)
            cannonballs += [new_cannonball]
            self.f1_on = 0
            self.f1_power = 1
            
    def fire2_start(self, event):
        """Запуск процесса усиления пушки для выстрела ракетой."""
        if self.rockets > 0:
            self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел ракетой.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости ракеты vx и vy зависят от положения
        мыши."""
        global rockets
        if self.rockets > 0:
            self.rockets -= 1
            new_rocket = rocket(self.x, self.y)
            try:
                self.an = math.atan((event.y-new_rocket.y) / (event.x-new_rocket.x))
            except ZeroDivisionError:
                self.an = math.atan(-1)
            if event.x > new_rocket.x:
                new_rocket.vx = self.f2_power * new_rocket.vx * math.cos(self.an)
                new_rocket.vy = -self.f2_power * new_rocket.vy * math.sin(self.an)
            else:
                new_rocket.image = 'ракетаl.png'
                new_rocket.vx = -self.f2_power * new_rocket.vx * math.cos(self.an)
                new_rocket.vy = self.f2_power * new_rocket.vy * math.sin(self.an)
            rockets += [new_rocket]
            self.f2_on = 0
            self.f2_power = 1
        
    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            try:
                self.an = math.atan((event.y-self.x) / (event.x-self.y))
            except ZeroDivisionError:
                pass

    def power_up(self):
        """Усиление пушки при зажатии мыши. Переменные силы self.f1_power и
        self.f2_power увеличиваются до макс. значения, это иллюстрируется
        линиями над танками."""
        if self.f1_on:
            if self.f1_power < 10:
                self.f1_power += 0.05
                canv.create_line([self.x, self.y - 15, self.x + self.rx*(self.f1_power/10-0.1),
                                  self.y - 15], fill = 'orange', width = 5)
            else:
                canv.create_line([self.x, self.y - 15, self.x + self.rx,
                                  self.y - 15], fill = 'orange', width = 5)
        elif self.f2_on:
            if self.f2_power < 10:
                self.f2_power += 0.05
                canv.create_line([self.x, self.y - 15, self.x + self.rx*(self.f2_power/10-0.1),
                                  self.y - 15], fill = 'red', width = 5)
            else:
                canv.create_line([self.x, self.y - 15, self.x + self.rx,
                                  self.y - 15], fill = 'red', width = 5)
        
        
class plane():
    """Вражеский самолет."""
    def __init__(self, x=0, y=0):
        """Конструктор класса.
        Параметры: координаты, скорость по горизонтали, направление изображения
        (смотрит вправо или влево), название файла с изображением, время до
        сброса бомбы."""
        self.x=x
        self.y=y
        self.vx=1
        self.side='right'
        self.image = 'самолетr.png'
        self.time = randint(120, 240)
    def move(self):
        """Движение самолета за один кадр перерисовки. Проверка направления
        изображения самолета и сброс бомбы при исходе времени."""
        self.direction()
        self.drop_bomb()
        if self.side == 'right':
            self.image = self.image[:7] + 'r.png'
            self.x += self.vx
        else:
            self.image = self.image[:7] + 'l.png'
            self.x -= self.vx
    def direction(self):
        """Смена направления изображения при достижении края экрана
        (ширина - 1280)."""
        if self.side == 'right' and self.x > 1182:
            self.side = 'left'
        elif self.side == 'left' and self.x < 0:
            self.side = 'right'
    def period_til_drop(self):
        """Уменьшение времени до сброса бомбы и перезапуск таймера,
        если бомба сброшена."""
        global bombs
        if self.time == 0:
            self.time = randint(120, 240)
        elif self.time > 0:
            self.time -= 1
    def drop_bomb(self):
        """Сброс (создание) бомбы при истечении времени на таймере."""
        global bombs
        self.period_til_drop()
        if self.time == 0:
            new_bomb = bomb()
            new_bomb.x=self.x
            new_bomb.y=self.y+77
            new_bomb.side=self.side
            new_bomb.image = 'бомба' + self.side[0] + '.png'
            bombs.append(new_bomb)

"""Создание игрового окна и начальных игровых объектов."""
root = tk.Tk()
fr = tk.Frame(root)
root.geometry('1280x650')
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)
who_is_player = 1
player_time = 1800
tank = 'танк1r.png'
t1 = playertank(tank)
t2 = playertank(tank[:5]+'l.png')
t2.x = 1280 - t2.rx - 20
img_tank1 = tk.PhotoImage(file=t1.image)
img_tank2 = tk.PhotoImage(file=t2.image)
player1 = canv.create_image(t1.x, t1.y, anchor = 'nw', image=img_tank1)
player2 = canv.create_image(t2.x, t2.y, anchor = 'nw', image=img_tank2)
plane = plane()
img_plane = tk.PhotoImage(file=plane.image)
enemy = canv.create_image(plane.x, plane.y, anchor = 'nw', image=img_plane)
bombs = []
cannonballs = []
rockets = []

"""Основной цикл игры - продолжается, пока хотя бы один из танков не потеряет
все здоровье."""
while t1.health > 0 and t2.health > 0:
    """Фон."""
    canv.create_polygon(0, 0, 1280, 0, 1280, 77, 0, 77, fill='light sky blue')
    canv.create_polygon(0, 77, 1280, 77, 1280, 549, 0, 549, fill = 'green3')
    canv.create_line(640, 77, 640, 549, width = 3)
    """Отображение очков здоровья, времени хода и количества снарядов."""
    health_points_t1 = canv.create_text(t1.x + 26, t1.y - 30, text=t1.health,
                                    font='56')
    health_points_t2 = canv.create_text(t2.x + 26, t2.y - 30, text=t2.health,
                                    font='56')
    displayed_time = canv.create_text(620, 570, text='Время хода игрока ' + str(who_is_player)
                                      + ': ' + str(player_time//120 + 1) + ' секунд', font='108')
    if who_is_player == 1:
        displayed_weapon = canv.create_text(620, 600, text='Осталось ' + str(t1.balls) +
                                            ' ядер и ' + str(t1.rockets) + ' ракет', font='108')
    else:
        displayed_weapon = canv.create_text(620, 600, text='Осталось ' + str(t2.balls) +
                                            ' ядер и ' + str(t2.rockets) + ' ракет', font='108')
    """Уменьшение времени хода и переключение активного игрока при истечении времени."""
    player_time -= 1
    if player_time == 0:
        player_time = 1800
        if who_is_player == 1:
            t1.f1_on = 0
            t1.f2_on = 0
            t1.balls = 5
            t1.rockets = 1
            who_is_player = 2
        else:
            t2.f1_on = 0
            t2.f2_on = 0
            t2.balls = 5
            t2.rockets = 1
            who_is_player = 1
    """Передвижение неигровых объектов: самолета и "существующих" снарядов,
    удаление "несуществующих" снарядов, проверка всех возможных столкновений."""
    plane.move()
    for i in range (len(bombs)-1, -1, -1):
        if bombs[i].exist == 0:
            if len(bombs) == 1:
                bombs = []
            else:
                del bombs[i]
        else:
            if who_is_player == 1:
                bombs[i].move(t1)
            else:
                bombs[i].move(t2)
            img_bomb = tk.PhotoImage(file=bombs[i].image)
            bomba = canv.create_image(bombs[i].x, bombs[i].y, anchor = 'nw',
                                     image=img_bomb)
    for raketa in rockets:
        if raketa.exist == 0:
            del raketa
        else:
            img_rocket = tk.PhotoImage(file=raketa.image)
            canv.create_image(raketa.x, raketa.y, anchor = 'nw', image=img_rocket)
            raketa.move()
            for bomba in bombs:
                if raketa.didhit(bomba) and bomba.exist:
                    bomba.exist = 0
            if who_is_player == 1:
                if raketa.didhit(t2):
                    t2.health -= 10
            else:
                if raketa.didhit(t1):
                    t1.health -= 10
    for i in range (len(cannonballs)-1, -1, -1):
        if cannonballs[i].exist == 0:
            if len(cannonballs) == 1:
                cannonballs = []
            else:
                del cannonballs[i]
        else:
            c = cannonballs[i]
            c.move()
            for bomba in bombs:
                if c.didhit(bomba) and bomba.exist:
                    bomba.exist = 0
            if who_is_player == 1:
                if c.didhit(t2):
                    t2.health -= 5
            else:
                if c.didhit(t1):
                    t1.health -= 5
    """Создание изображений танков и самолета."""
    img_tank1 = tk.PhotoImage(file=t1.image)
    img_tank2 = tk.PhotoImage(file=t2.image)
    player1 = canv.create_image(t1.x, t1.y, anchor = 'nw', image=img_tank1)
    player2 = canv.create_image(t2.x, t2.y, anchor = 'nw', image=img_tank2)
    img_plane = tk.PhotoImage(file=plane.image)
    enemy = canv.create_image(plane.x, plane.y, anchor = 'nw', image=img_plane)
    """Привязка кнопок мыши к выстрелам снарядами."""
    if who_is_player == 1:
        canv.bind_all('<KeyPress-Up>', t1.move)
        canv.bind_all('<KeyPress-Down>', t1.move)
        canv.bind_all('<KeyPress-Left>', t1.move)
        canv.bind_all('<KeyPress-Right>', t1.move)
        canv.bind('<Button-1>', t1.fire1_start)
        canv.bind('<ButtonRelease-1>', t1.fire1_end)
        canv.bind('<Button-3>', t1.fire2_start)
        canv.bind('<ButtonRelease-3>', t1.fire2_end)
        canv.bind('<Motion>', t1.targetting)
    else:
        canv.bind_all('<KeyPress-Up>', t2.move)
        canv.bind_all('<KeyPress-Down>', t2.move)
        canv.bind_all('<KeyPress-Left>', t2.move)
        canv.bind_all('<KeyPress-Right>', t2.move)
        canv.bind('<Button-1>', t2.fire1_start)
        canv.bind('<ButtonRelease-1>', t2.fire1_end)
        canv.bind('<Button-3>', t2.fire2_start)
        canv.bind('<ButtonRelease-3>', t2.fire2_end)
        canv.bind('<Motion>', t2.targetting)
    """Увеличение силы выстрела."""
    t1.targetting()
    t1.power_up()
    t2.targetting()
    t2.power_up()
    """Обновление экрана и выход из игры при нажатии на крестик."""
    canv.update()
    try:
        canv.delete('all')
    except tk.TclError:
        sys.exit()

"""Похвала победителю."""
if t1.health > t2.health:
    canv.create_text(640, 400, text = 'Победил игрок 1. Поздравляем!', font = 56)
else:
    canv.create_text(640, 400, text = 'Победил игрок 2. Поздравляем!', font = 56)
