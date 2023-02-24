# 8.1[49]: Создать телефонный справочник с возможностью импорта и экспорта данных в формате csv. 
# Доделать задание вебинара и реализовать Update, Delete
# Информация о человеке: Фамилия, Имя, Телефон, Описание
# Корректность и уникальность данных не обязательны.

# Функционал программы
# 1) телефонный справочник хранится в памяти в процессе выполнения кода.
# Выберите наиболее удобную структуру данных для хранения справочника.
# 2) CRUD: Create, Read, Update, Delete
# Create: Создание новой записи в справочнике: ввод всех полей новой записи, занесение ее в справочник.
# Read: он же Select. Выбор записей, удовлетворяющих заданном фильтру: по первой части фамилии человека. Берем первое совпадение по фамилии.
# Update: Изменение полей выбранной записи. Выбор записи как и в Read, заполнение новыми значениями.
# Delete: Удаление записи из справочника. Выбор - как в Read.
# 3) экспорт данных в текстовый файл формата csv
# 4) импорт данных из текстового файла формата csv

# Используйте функции для реализации значимых действий в программе

# (*) Усложнение.

# Сделать тесты для функций
# Разделить на model-view-controller


phone_book = []
# phone_book = [['Иванов', 'Иван', '777-000', 'Друг'], ['Морозов', 'Андрей', '333-555', 'Коллега']]

def menu(data: list):
    while True:
        print('Выберите действие: ')
        print('0 - Выйти из справочника')
        print('1 - Создать новую запись')
        print('2 - Распечатать содержимое справочника')
        print('3 - Выбрать запись по первой части фамилии')
        print('4 - Изменить поле(я) выбранной записи')
        print('5 - Удалить записи из справочника')
        print('6 - Импортировать данные из текстового файла')
        print('7 - Экспортировать данные в текстовый файл')

        get = input('Введите действие: ')
        if get =='0':
            print('До свидания!')
            break
        elif get == '1':
            data = create(data, get_data())
        elif get == '2':
            print_phone_book(data)
        elif get == '3':
            read(data)
        elif get == '4':
            update(data)
        elif get == '5':
            delete(data)  
        elif get == '6':
            name_file = get_file_name()
            batch_data = get_batch_data(name_file)
            data = batch_create(data, batch_data)
        elif get == '7':
            name_file = get_file_name()
            record_data(name_file, data)
        else:
            print('Некорректный ввод данных!')

def create(data: list, el: list) -> list: # Добавляет запись в существующую телефонную книгу.
    data.append(el)
    return data

def print_phone_book(data: list) -> None:
        print(f'Контакты: {data}')

def get_data() -> list:
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    discription = input('Введите описание: ')
    return [surname, name, phone, discription]

def get_file_name() -> str:
    return input('Введите имя файла: ')

def read(data: list) -> list: # Выбор записи, удовлетворяющей заданному фильтру: по первой части фамилии человека. Берем первое совпадение по фамилии.
    part_surname = input('Введите первые буквы фамилии: ')
    select_contact = None
    for el in data:
        if part_surname.casefold() in (el[0]).casefold():
            select_contact = el
    return select_contact

def update(data: list) -> list: # Изменение полей выбранной записи.
    change_contact = read(data)
   
    while True:
        print(f'Вы выбрали: {change_contact}')
        print('Выберите действие: ')
        print('0 - Выйти в главное меню')
        print('1 - Изменить фамилию')
        print('2 - Изменить имя')
        print('3 - Изменить телефон')
        print('4 - Изменить описание')
        
        for el in data:
            if el == change_contact:
                get_action = input('Введите действие: ')
                if get_action =='0':
                    print('Успешно!')
                    break
                elif get_action == '1':
                    change_contact[0] = input('Введите фамилию: ')
                elif get_action == '2':
                    change_contact[1] = input('Введите имя: ')
                elif get_action == '3':
                    change_contact[2] = input('Введите телефон: ')
                elif get_action == '4':
                    change_contact[3] = input('Введите описание: ')
                else:
                    print('Некорректный ввод данных!')       
                el = change_contact
        return data
  
def delete(data: list) -> list: # Удаление записи из справочника.
    del_contact = read(data)
    print(f'Вы удалили: {del_contact}')
    for el in data:
            if el == del_contact:
                data.remove(el)
    return data
 
def get_batch_data(name_file: str) -> list: # Импорт данных из текстового файла формата csv.
    lst = []
    with open('Sem_8_phonebook.csv', 'r', encoding='utf-8') as file:
        for line in file:
            lst.append(list(line.split('#')))
    return lst

def batch_create(data: list, batch_data) -> list:
    for el in batch_data:
        data = create(data, el)
    return data

def record_data(name_file, data): # Экспорт данных в текстовый файл формата csv.
    with open ('Sem_8_new_phonebook.csv', 'w', encoding = 'utf-8') as file:
        for el in data:
            file.write(f'{el[0]};{el[1]};{el[2]};{el[3]}\n')
    
menu(phone_book)