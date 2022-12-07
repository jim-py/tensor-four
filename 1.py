from random import randint
 
N = int(input('Введите длину списка: '))
a = [randint(1, 50) for i in range(N)]
print(f'Исходный список чисел: {a}')

for i in range(N - 1):
    for j in range(N - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
 
print(f'Отсортированный список чисел: {a}')
