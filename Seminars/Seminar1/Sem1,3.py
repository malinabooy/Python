"""Задача No5. Решение в группах
Вагоны в электричке пронумерованы натуральными числами, 
начиная с 1 (при этом иногда вагоны нумеруются от «головы» поезда, а иногда – с «хвоста»; 
это зависит от того, в какую сторону едет электричка). В каждом вагоне написан его номер. 
Витя сел в i-й вагон от головы поезда и обнаружил, что его вагон имеет номер j. 
Он хочет определить, сколько всего вагонов в электричке. Напишите программу, которая будет это делать или сообщать, 
что без дополнительной информации это сделать невозможно.
Input: 3 4(ввод на разных строках) Output: 6"""

i = int(input('В какой вагон сел Витя? '))
j = int(input('Какой номер написан в вагоне? '))

if i > j:
    print(f' {(i - 1) + j}')

elif i < j:
    print(f' {i + (j - 1)}')

else:
    print("без дополнительной информации это сделать невозможно")
