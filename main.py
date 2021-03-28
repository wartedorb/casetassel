"""
Case-study Тесселяция
Разработчики:
Кондрашов -
Бикметов -
Бычков -
"""

import turtle as t


def get_num_hexagons():
    """Запрос колличества шестиугольников + прверка"""
    print('Пожалуйста, введите количество шестиугольников, располагаемых в ряд: ', end='')
    g = 0
    while g != 1:
        try:
            a = int(input())
            if a > 3 and a < 21:
                g = 1
                return a
            else:
                print('Оно должно быть от 4 до 20. Пожалуйста, повторите попытку: ', end='')
        except ValueError:
            print('Введеное значение не является целым числом от 4 до 20. Пожалуйста, повторите попытку: ', end='')


def get_color_choice():
    """Из предлженных цветов предлагает пользователю выбрать один + проверка"""
    print(
        'Пожалуйста, выберите цвет\nДопустимые цвета заливки:\nкрасный\nсиний\nзеленый\nжелтый\nоранжевый\nфиолетовый\nрозовый\nциан\nсерый\nчерный')
    print('Пожалуйста, введите цвет: ', end='')
    list_color = ['красный', 'синий', 'зеленый', 'желтый', 'оранжевый', 'фиолетовый', 'розовый', 'циан', 'серый',
                  'черный']
    englist = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'cyan', 'gray', 'black']
    g = 0
    while g != 1:
        c = input().lower()
        a = 0
        while a != len(list_color):
            if c == list_color[a]:
                g = 1
                return englist[a]
            a += 1
        else:
            print('"', c, '"', ' не является верным значением. Пожалуйста, повторите попытку: ', sep='', end='')


def draw_hexagon(x, y, side, color):
    """Рисует правильный шестиуглольник на координатах, с заданной стороной, нужного цвета"""
    t.up()
    t.speed(10000)
    t.goto(x, y)
    t.down()
    t.color(color)
    t.left(30)
    t.begin_fill()
    for const in range(6):
        t.forward(side)
        t.right(60)
    t.end_fill()
    t.color('black')
    for const in range(6):
        t.forward(side)
        t.right(60)
    t.right(30)
    t.up()


num_hex = get_num_hexagons()

r = 500 / ((int(num_hex) * 2) + 1)

side = (2 * r) / (3 ** (1 / 2))

perpendicular = (side ** 2 - r ** 2) ** (1 / 2)

first_color = get_color_choice()

second_color = get_color_choice()


# рисуем ряды каждого типа
for c in range(0, num_hex + 1, 6):
    for i in range(0, num_hex, 2):
        draw_hexagon(i * (r * 2), -c * side, side, second_color)
    for i in range(1, num_hex, 2):
        draw_hexagon(i * (r * 2), -c * side, side, first_color)


# рисуем рамку проверки в 500 пикселей
t.up()
t.goto(-r, perpendicular)
t.down()
for i in range(4):
    t.forward(500)
    t.right(90)
t.done()

'''
Мой вам совет - рисунок может багнуться, изза функции, для того чтобы этого не происходило 
вам надо всегда возвращать черепаху под тот угол, в котором она начианлась, НО, скорее всего, 
это не произойдет так как я уже предусмотрел это в дефе и вам не нужно поворачивать рисунок 6уг
'''
