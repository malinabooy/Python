# sum = 0
# for i in range(1000):
#     if i % 3 == 0 or i % 5 == 0:
#         sum += i
# print(sum)


def get_middle(s):
    return s[len(s) // 2] if len(s) % 2 != 0 else s[len(s) // 2 - 1:len(s) // 2 + 1]
