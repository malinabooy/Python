# Задача No17. Решение в группах
# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4] Output: 6

from random import randint

list_1 = [randint(1, 11) for _ in range(10)]
print(list_1)
set_random = set(list_1)

print(set_random)
print(len(set_random))
