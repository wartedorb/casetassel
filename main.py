"""
Case-study Тесселяция
Разработчики:

Кондрашов - 2 %
Бикметов - 45 %
Бычков - 44 %
"""

import turtle as t


def get_num_hexagons():
    """Запрос колличества шестиугольников + прверка"""
    print('Пожалуйста, введите количество шестиугольников, располагаемых в ряд: ', end='')
    g = 0
    while g != 1:
        try:
            a = int(input())
            if 3 < a < 21:
                g = 1
                return a
            else:
                print('Оно должно быть от 4 до 20. Пожалуйста, повторите попытку: ', end='')
        except ValueError:
            print('Введеное значение не является целым числом от 4 до 20. Пожалуйста, повторите попытку: ', end='')


def get_color_choice():
    """Из предлженных цветов предлагает пользователю выбрать один + проверка"""
    print('Пожалуйста, выберите цвет\nДопустимые цвета '
          'заливки:\nкрасный\nсиний\nзеленый\nжелтый\nоранжевый\nфиолетовый\nрозовый\nциан\nсерый\nчерный')

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
    t.speed(100000)
    t.up()
    t.goto(x - 250, y + 250)
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



def non_or_one(a):
    return not a % 2 == 0


# рисуем ряды
def line1(v, m, n):
    m1 = non_or_one(m)

    for i in range(0, num_hex, 2):
        draw_hexagon(i * (r * 2) - v - r * m1, -1.5 * m * side - 0, side, n * second_color + (1 - n) * first_color)
    for i in range(1, num_hex, 2):
        draw_hexagon(i * (r * 2) - v - r * m1, -1.5 * m * side - 0, side, n * first_color + (1 - n) * second_color)


n = 0
for i in range(num_hex):
    if n == 4:
        n = 0
    if n == 0 or n == 1:
        line1(0, i, 0)
    else:
        line1(0, i, 1)
    n += 1

'''рисуем рамку 500x500 для проверки правильности размера'''
t.up()
t.goto(-r - 250, perpendicular + 250)

t.down()
for i in range(4):
    t.forward(500)
    t.right(90)
t.done()
