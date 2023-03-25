# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания
# все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.
from random import randint

n = int(input('Введите количество N символов: '))
# list_1 = []
# for i in range(n):
#     num = int(input('Введите элемент: '))
#     list_1.append(num)
# print(list_1)
list_1 = [randint(0, 10) for i in range(n)]
print(list_1)

m = int(input('Введите количество M символов: '))
# list_2 = []
# for i in range(m):
#     num = int(input('Введите элемент: '))
#     list_2.append(num)
# print(list_2)
list_2 = [randint(0, 10) for i in range(n)]
print(list_2)

list_3 = list_1 + list_2
list_3.sort()
print(list_3)
for i in list_3:
    if list_3.count(i) > 1:
        print(i, end=', ')
