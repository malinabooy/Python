list_1 = []
list_1 = list()
list_1 = [1, 2, 3, 8]
print(list_1)

list_1.append(9)  # добавить элемент в конец
print(list_1)

list_1.pop()  # удалить элемент в конце
print(list_1)

list_1.insert(2, 11)  # добавить элемент в нужную позицию
print(list_1)

list_1 = []  # заполнение листа
for i in range(5):
    list_1.append(i)
    print(list_1)

# КОРТЕЖИ
t = (1, 2,)
print(type(t))

v = [1, 2, 3]
print(type(v))

v = tuple(v)
print(v)
print(type(v))

a, b, c = v
print(a, b, c)

t = (1, 2, 3, 4, 5,)
for i in range(len(t)):
    print(t[i])
