# 1.Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные числа.
# Реализовать программу с использованием функции filter. Результат отобразить на экране в виде последовательности
# оставшихся чисел в одну строчку через пробел.
from random import randint

n = int(input('Введите кол-во элементов: '))
list_1 = [randint(0, 10) for i in range(n)]
print(list_1)


def even(num):
    if (num % 2) == 0:
        return True
    else:
        return False


print(list(filter(even, list_1)))
