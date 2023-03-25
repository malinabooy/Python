# Проверка палиндрома.Напишите функцию, которая проверяет, является ли строка палиндромом
# (то есть читается одинаково справа налево и слева направо) с использованием рекурсии.
def palindrom(s):
    if len(s) == 1:
        return True
    else:
        if s[0] == s[-1]:
            return palindrom(s[1:-1])
        else:
            return False


s = input('Введите строку: ')
if palindrom(s) == True:
    print('Палиндром!')
else:
    print('Не палиндром!')
