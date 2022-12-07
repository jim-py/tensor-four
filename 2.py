color = {'black': (0, 0, 0), 'white': (255, 255, 255), 'red': (255, 0, 0), 'green': (0, 255, 0), 'blue': (0, 0, 255), }
print(*color.keys())
color_name = input('Напишите название цвета из вышеперечисленных:\n')
print(f'RGB - {color[color_name]}')
