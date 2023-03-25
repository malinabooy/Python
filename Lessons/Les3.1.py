# def sum_numbers(n):
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     return summa
#
# print(sum_numbers(5))

def sum_str(*args):
    res = ''
    for i in args:
        res += i
    return res


print(sum_str('q', 'e', '1'))
