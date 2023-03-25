# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

from random import randint

list_1 = [randint(1, 5) for _ in range(15)]
print(list_1)
min_ocenka = min(list_1)
max_ocenka = max(list_1)
for i in range(15):
    if list_1[i] == max_ocenka:
        list_1[i] = min_ocenka
print(list_1)
