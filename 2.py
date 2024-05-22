# №1

word = input("Введите слово:")
letter_count = len(word)
middle = letter_count // 2
if letter_count % 2 == 0:
    print(word[middle-1:middle+1])
if letter_count % 2 != 0:
    print(word[middle])

# №2

x = int(input("Введите число:"))
sum = 0
while x != 0:
    sum += x
    x = int(input("Введите число:"))
print(sum)

# №3

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
if len(boys) == len(girls):
    pare = [(x, y) for x, y in zip(sorted(boys), sorted(girls))]
    for i in pare:
        print(*i, sep=' и ')
else:
    print("Внимание, кто-то может остаться без пары!")


boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
if len(boys) == len(girls):
    pare = [(x, y) for x, y in zip(sorted(boys), sorted(girls))]
    for i in pare:
        print(*i, sep=' и ')
else:
    print("Внимание, кто-то может остаться без пары!")

# №4

import statistics

countries_temperature = [
    ['Таиланд', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
    ['Германия', [57.2, 55.4, 59, 59, 53.6]],
    ['Россия', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
    ['Польша', [50, 50, 53.6, 57.2, 55.4, 55.4]]
]
for i in countries_temperature:
    print(i[0], round(((statistics.mean(i[1]) - 32) * 5 / 9), 2), 'C')

# №5

import re

#(1 буква, 3 цифры, 2 буквы, 2-3 цифры)

car_ids = 'А111АА11'
pattern = r'\b[АВЕКМНОРСТУХ]{1}\d{3}\b[АВЕКМНОРСТУХ]{2}\d{2}'
match = re.search(pattern, car_ids)
if match:
    print(f'Номер {car_ids} валиден. Регион:')
else:
    print(f'Номер {car_ids} не валиден')


lst = input()
print('Список номеров частных автомобилей:', re.findall(r'\b[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}\b', lst))
print('Список номеров такси:', re.findall(r'\b[АВЕКМНОРСТУХ]{2}\d{5,6}\b', lst))




r'\b[АВЕКМНОРСТУХ]{1}\d{3}\b[АВЕКМНОРСТУХ]{2}\d{2,3}'

#r'\b[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}\b'

car_ids = ['А222ВС96', 'АБ22ВВ193']
match = re.search(r'\[АВЕКМНОРСТУХ]\d{3}\[АВЕКМНОРСТУХ]{2}\d{2-3}', car_ids)
if match:
    print('Номер {match[1]} валиден. Регион:')
else:
    print('Номер {match[1]} не валиден')


import re
pattern = r'\s*([А-Яа-яЁё]+)(\d+)\s*'
string = r'---   Опять45   ---'
match = re.search(pattern, string)
print(f'Найдена подстрока >{match[0]}< с позиции {match.start(0)} до {match.end(0)}')
print(f'Группа букв >{match[1]}< с позиции {match.start(1)} до {match.end(1)}')
print(f'Группа цифр >{match[2]}< с позиции {match.start(2)} до {match.end(2)}')
###
# -> Найдена подстрока >   Опять45   < с позиции 3 до 16
# -> Группа букв >Опять< с позиции 6 до 11
# -> Группа цифр >45< с позиции 11 до 13
