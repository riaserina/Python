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
pattern = r'\b[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}\b'
if re.findall(pattern, car_ids):
    print(f'Номер {car_ids} валиден. Регион:')
else:
    print(f'Номер {car_ids} не валиден')

# №6

stream = [
    'user4,2021-01-01;3',
    'user3,2022-01-07;4',
    'user2,2022-03-29;1',
    'user1,2020-04-04;13',
    'user2,2022-01-05;7',
    'user1,2021-06-14;4',
    'user3,2022-07-02;10',
    'user4,2021-03-21;19',
    'user4,2022-03-22;4',
    'user4,2022-04-22;8',
    'user4,2021-05-03;9',
    'user4,2022-05-11;11'
]
print(stream.merge())

sum = 0
index = -1
for row in stream:
    sum += row[index]
    print(sum)


pattern = r'user4\D\d\d\d\d\D\d\d\D\d\d\D\d{1,10}'
if re.findall(pattern, stream)
print(sorted(stream))



x = int(input("Введите число:"))
sum = 0
while x != 0:
    sum += x
    x = int(input("Введите число:"))
print(sum)



