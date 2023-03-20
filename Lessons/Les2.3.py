list_1 = [i for i in range(1, 10)]  # [1, 2, 3,..., 10]
print(list_1)

list_1 = [i for i in range(1, 10) if i % 2 == 0]  # [2, 4, 6,..., 10]
print(list_1)

list_1 = [i * 2 for i in range(10) if i % 2 == 0]
print(list_1)  # [0, 4, 8, 12, 16]
