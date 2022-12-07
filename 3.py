from random import randint
 
N = int(input('Введите длину списка: '))
a = {randint(1, 50) for i in range(N)}
b = {randint(1, 50) for j in range(N)}
print('Список a -', a)
print('Список b -', b)
print('Одинаковые значения из обоих списков -', *(a & b))
print('Уникальные значения в списке а -', *(a - b))
print('Уникальные значения в списке b -', *(b - a))
print('Уникальные значения из обоих списков -', *(a ^ b))
