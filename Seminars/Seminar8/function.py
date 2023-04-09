def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии/имени/номеру/описанию\n"
          "3. Добавить абонента в справочник\n"
          "4. Сохранить справочник в текстовом формате\n"
          "5. Закончить работу")
    choice = int(input(''))
    return choice


def read_csv(filename: str) -> list:
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)

    return data


def print_result(data: list):  # принт результата
    for el in data:
        s = ''
        for k, v in el.items():
            s += f'{k}: {v}\n'
        print(s)


def search_param():  # определение параметров поиска
    print()
    search = input('1 - по фамилии\n2 - по имени\n3 - по номеру телефона\n4 - по описанию\n')
    print()
    search_value = None
    if search == '1':
        search_value = input('Введите фамилию для поиска: ')
        print()
    elif search == '2':
        search_value = input('Введите имя для поиска: ')
        print()
    elif search == '3':
        search_value = input('Введите номер для поиска: ')
        print()
    elif search == '4':
        search_value = input('Введите описание для поиска: ')
        print()
    return search, search_value


def find_param(data):  # поиск по параметрам
    search, search_value = search_param()
    search_value_dict = {'1': 'Фамилия', '2': 'Имя', '3': 'Телефон', '4': 'Описание'}
    find1 = []
    for line in data:
        if line[search_value_dict[search]] == search_value:
            find1.append(line)
    if len(find1) == 0:
        print('Контакт не найден!')
    else:
        print_result(find1)
    print()


def add_abonent(data):  # добавление абонента
    abonent = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    abonent.append(input('Введите фамилию: '))
    abonent.append(input('Введите имя: '))
    abonent.append(input('Введите телефон: '))
    abonent.append(input('Введите описание: '))
    new_abonent = dict(zip(fields, abonent))
    data.append(new_abonent)
    print()
    for k, v in new_abonent.items():
        print(f'{k}: {v}')
    print_result(data)


def save_book(data):  # сохранение файла
    with open(input('Имя файла: '), 'w', encoding='utf-8') as new_data:
        for i in data:
            str_i = ""
            for v in i.values():
                str_i += v + ", "
            str_i = str_i[:-1]
            new_data.write(str_i + "\n")
    print('Saved')
