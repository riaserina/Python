# №1

x = len('Насколько проще было бы писать программы, если бы не заказчики')
y = len('640Кб должно хватить для любых задач. Билл Гейтс (по легенде)')
if x > y:
    print("Фраза 1 длиннее фразы 2")
elif x < y:
    print("Фраза 2 длиннее фразы 1")
elif x == y:
    print("Фразы равны")

# №2

year = 2024
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("високосный год")
else:
    print("обычный год")

# №3

date = int(input("Введите день:"))
month = input("Введите месяц:")
if (date >= 21 and month == "Март") or (date <= 19 and month == "Апрель"):
    print("Овен")
elif (date >= 20 and month == "Апрель") or (date <= 20 and month == "Май"):
    print("Телец")
elif (date >= 21 and month == "Май") or (date <= 21 and month == "Июнь"):
    print("Близнецы")
elif (date >= 22 and month == "Июнь") or (date <= 22 and month == "Июль"):
    print("Рак")
elif (date >= 23 and month == "Июль") or (date <= 22 and month == "Август"):
    print("Лев")
elif (date >= 23 and month == "Август") or (date <= 22 and month == "Сентябрь"):
    print("Дева")
elif (date >= 23 and month == "Сентябрь") or (date <= 23 and month == "Октябрь"):
    print("Весы")
elif (date >= 24 and month == "Октябрь") or (date <= 21 and month == "Ноябрь"):
    print("Скорпион")
elif (date >= 22 and month == "Ноябрь") or (date <= 21 and month == "Декабрь"):
    print("Стрелец")
elif (date >= 22 and month == "Декабрь") or (date <= 20 and month == "Январь"):
    print("Козерог")
elif (date >= 21 and month == "Январь") or (date <= 20 and month == "Февраль"):
    print("Водолей")
elif (date >= 21 and month == "Февраль") or (date <= 20 and month == "Март"):
    print("Рыбы")

# №4

width = 15
length = 55
height = 201
if width <= 15 and length <= 15 and height <= 15:
    print("Корoбка №1")
elif width > 200 or length > 200 or height > 200:
    print("Упаковка для лыж")
elif 50 > width > 15 or 50 > length > 15 or 50 > height > 15:
    print("Корoбка №2")
else:
    print("Корoбка №3")

# №5

number = 111111
number = int(number)
a = number // 100000
b = number % 100000 // 10000
c = number % 10000 // 1000
d = number % 1000 // 100
e = number % 100 // 10
f = number % 10
if (a + b + c) == (d + e +f):
    print("Счастливый билет")
else:
    print("Несчастливый билет")

# №6

import math

figure = (input("Введите название фигуры:"))
if figure == "Круг":
    r = int(input("Введите радиус:"))
    print(3.14 * (r ** 2))
elif figure == "Треугольник":
    ab = int(input("Введите длину стороны ab:"))
    bc = int(input("Введите длину стороны bc:"))
    ca = int(input("Введите длину стороны ca:"))
    p = (ab + bc + ca) / 2
    print(math.sqrt(p * (p - ab) * (p - bc) * (p - ca)))
elif figure == "Прямоугольник":
    ab = int(input("Введите длину стороны ab:"))
    bc = int(input("Введите длину стороны bc:"))
    print (2 * ab + 2 * bc)
