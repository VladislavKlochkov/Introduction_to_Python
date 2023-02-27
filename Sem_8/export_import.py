def get_file_name() -> str:
    return input('Введите имя файла: ')


def get_batch_data(name_file: str) -> list: # Импорт данных из текстового файла формата csv.
    lst = []
    with open('Sem_8_phonebook.csv', 'r', encoding='utf-8') as file:
        for line in file:
            lst.append(list(line.strip().split('#')))
    return lst

def record_data(name_file, data): # Экспорт данных в текстовый файл формата csv.
    with open ('Sem_8_new_phonebook.csv', 'w', encoding = 'utf-8') as file:
        for el in data:
            file.write(f'{el[0]};{el[1]};{el[2]};{el[3]}\n')

