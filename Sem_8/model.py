


def create(data: list, el: list) -> list: # Добавляет запись в существующую телефонную книгу.
    data.append(el)
    return data

def batch_create(data: list, batch_data) -> list:
    for el in batch_data:
        data = create(data, el)
    return data

def print_phone_book(data: list) -> None:
    print(f'Контакты: ')
    for el in data:
        print_record(el)

def print_record(record: list) -> None:
    print(f'{record[0]}, {record[1]}, {record[2]}, {record[3]}')
        

def get_data() -> list:
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    discription = input('Введите описание: ')
    return [surname, name, phone, discription]



def read(data: list) -> list: # Выбор записи, удовлетворяющей заданному фильтру: по первой части фамилии человека. Берем первое совпадение по фамилии.
    part_surname = input('Введите первые буквы фамилии: ')
    for el in data:
        if part_surname.casefold() in (el[0]).casefold():
            return el


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
            break
    return data
 
