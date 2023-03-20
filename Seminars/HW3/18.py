# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

from random import randint

n = int(input('Введите кол-во элементов: '))
x = int(input('Введите число, которое надо найти: '))

list = [randint(0, 10) for i in range(n)]
print(list)
x1 = x - 1
x2 = x + 1
for i in range(len(list)):
    while list[i] == x1 or list[i] == x2 or list[i] == x:
        print(list[i], end=' ')
        break
