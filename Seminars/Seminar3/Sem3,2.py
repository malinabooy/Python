# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический)
# на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3 Output: [4, 5, 1, 2, 3]
from random import randint

n = int(input('Введите длину листа: '))
k = int(input('На сколько элементов сдвинуть: '))

list = [randint(-10, 10) for i in range(n)]
print(list)

for i in range(k):
    list.insert(0, list.pop(-1))
print(list)
