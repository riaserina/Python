# №1

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}
set_ids = set()
for geo in ids.values():
       set_ids = set_ids.union(set(geo))
print(f'Уникальные гео-метки: {set_ids}')

# №2

queries = [
'смотреть сериалы онлайн',
'новости спорта',
'афиша кино',
'курс доллара',
'сериалы этим летом',
'курс по питону',
'сериалы про спорт'
]
words_quantity = []
for item in queries:
    words_quantity.append(len(item.split()))
a = 1
while a <= max(words_quantity):
    if words_quantity.count(a) > 0:
        print('Поисковых запросов, содержащих', a, 'слов(а):', round(words_quantity.count(a)*100/len(words_quantity), 2))
a += 1

# №3

results = {
    'vk': {'revenue': 103, 'cost': 98},
    'yandex': {'revenue': 179, 'cost': 153},
    'facebook': {'revenue': 103, 'cost': 110},
    'adwords': {'revenue': 35, 'cost': 34},
    'twitter': {'revenue': 11, 'cost': 24},
}
for key, company in results.items():
    company['ROI'] = round((((int(company['revenue']) / int(company['cost'])) - 1) * 100), 2)
    print(key, company)

# №4

stats = {'facebook': 55, 'yandex': 115, 'vk': 120, 'google': 99, 'email': 42, 'ok': 98}
sorted_stats = sorted(stats.items(), key=lambda item: item[1], reverse=True)
max_stats = sorted_stats[0]
print(f'Максимальный объем продаж на рекламном канале: {max_stats[0]}')


