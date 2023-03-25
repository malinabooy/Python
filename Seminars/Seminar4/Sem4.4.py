# Напишите программу, которая найдёт произведение пар чисел списка.Парой считаем первый и последний элемент, второй
# и предпоследний и т.д.
# *Пример: *
# - [2, 3, 4, 5, 6] = > [12, 15, 16];
# - [2, 3, 5, 6] = > [12, 15]

from random import randint

n = int(input('Введите кол-во элементов: '))

list = [randint(0, 10) for i in range(n)]
print(list)

mult = 0
for i in range(int(len(list) / 2 + 1)):
    mult = list[i] * list[len(list) - i - 1]
    print(mult, end=' ')
