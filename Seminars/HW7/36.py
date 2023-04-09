# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию,
# вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.
#
# *Пример:*
#
# **Ввод:** `print_operation_table(lambda x, y: x * y) `
# **Вывод:*

def print_operation_table(operation, num_line, num_columns):
    for i in range(1, num_line + 1):
        for j in range(1, num_columns + 1):
            print("%4d" % (i * j), end="")
        print()


columns = int(input("Введите количество строк: "))
line = int(input("Введите количество столбцов: "))
print_operation_table(lambda x, y: x * y, line, columns)
