# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
#
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной
from function import *


def phonebook():
    choice = show_menu()
    data = read_csv('phonebook.csv')
    while choice != 5:
        if choice == 1:
            print_result(data)
        elif choice == 2:
            find_param(data)
        elif choice == 3:
            add_abonent(data)
        elif choice == 4:
            save_book(data)

        choice = show_menu()
    print('Bye!')


phonebook()
