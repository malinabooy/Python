colors = {'red', 'green', 'blue'}
print(colors)  # {'red', 'green', 'blue'}
colors.add('red')
print(colors)  # {'red', 'green', 'blue'}
colors.add('gray')
print(colors)  # {'red', 'green', 'blue','gray'}
colors.remove('red')  # Удаляет
print(colors)  # {'green', 'blue','gray'}

colors.discard('red')  # Проверяет множество и удаляет если есть
print(colors)  # {'green', 'blue','gray'}
colors.clear()  # { }
print(colors)  # set()

a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy()  # c = {1, 2, 3, 5, 8} Копирует
u = a.union(b)  # u = {1, 2, 3, 5, 8, 13,21} Добавляет
i = a.intersection(b)  # i = {8, 2, 5} Схожие
dl = a.difference(b)  # dl = {1, 3} Разница
dr = b.difference(a)  # dr = {13, 21} Разница
q = a.union(b).difference(a.intersection(b))  # {1, 21, 3, 13}

a = {1, 2, 3, 5, 8}
b = frozenset(a)
print(b)  # frozenset({1, 2, 3, 5, 8}) Заморозка
