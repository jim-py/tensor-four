inventory = {'pants': 3}
weight = 3
max_weight = 20
items = {'axe': 5, 'pickaxe': 7, 'bed': 5, 'obsidian': 17, 'bedrock': 21}
print('''Добро пожаловать в приложение "Инвентарь"''')
while True:
    try:
        choice = int(input('''1 - Посмотреть инвентарь
2 - Посмотреть предметы
3 - Положить предмет в инвентарь
4 - Выложить предмет из инвентаря
5 - Узнать вес инвентаря

0 - Выход
Выбор - '''))
    except ValueError:
        print('-----Напишите число!-----')
        continue
    if choice == 0:
        print('-----Пока!-----')
        break
    elif choice == 1:
        print('----- Инвентарь:', *sorted(inventory.items(), key=lambda x: x[1]), '-----')
    elif choice == 2:
        print('----- Предметы:', *sorted(items.items(), key=lambda x: x[1]), '-----')
    elif choice == 3:
        print(*items.items())
        s = input('Какой предмет хотите добавить? Напишите его название:\n')
        try:
            if weight + items[s] <= max_weight:
                weight += items[s]
            else:
                print('-----Слишком тяжело!-----')
                continue
            inventory[s] = items[s]
            items.pop(s)
        except KeyError:
            print('-----Такого предмета нет!-----')
    elif choice == 4:
        print(*inventory.items())
        s = input('Какой предмет хотите убрать? Напишите его название:\n')
        try:
            items[s] = inventory[s]
            weight -= inventory[s]
            inventory.pop(s)
        except KeyError:
            print('-----Такого предмета нет!-----')
    elif choice == 5:
        print(f'----- {weight} кг. -----')
    else:
        print('-----Нет такого выбора!-----')
