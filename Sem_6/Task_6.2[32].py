# 6.2[32]: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)
# Напишите функцию
# - Аргументы: список чисел и границы диапазона
# - Возвращает: список индексов элементов (смотри условие)

# Примеры/Тесты:
# lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# <function_name>(lst1, 2, 10) -> [1, 3, 7, 9, 10, 13, 14, 19]
# <function_name>(lst1, 2, 9) -> [1, 3, 7, 10, 13, 19]
# <function_name>(lst1, 0, 6) -> [2, 3, 6, 7, 10, 11, 16]

# (*) Усложнение. Для формирования списка внутри функции используйте Comprehension

# (*) Усложнение. Функция возвращает список кортежей вида: индекс, значение

# Примеры/Тесты:
# lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# <function_name>(lst1, 2, 10) -> [(1, 9), (3, 3), (7, 4), (9, 10), (10, 2), (13, 8), (14, 10), (19, 7)]


lst1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

def search_index(lst, min_bound, max_bound):
    res = []
    for i in range(len(lst)):
        if min_bound <= lst[i] <= max_bound:
            res.append(i)
    return res
print(search_index(lst1,2,10))
print(search_index(lst1, 2, 9))
print(search_index(lst1, 0, 6))
# (*) Усложнение.

def search_index(lst, min_bound, max_bound):
    return [i for i in range(len(lst)) if min_bound <= lst[i] <= max_bound]
print(search_index(lst1,2,10))
print(search_index(lst1, 2, 9))
print(search_index(lst1, 0, 6))
# # (*) Усложнение.

def search_index(lst, min_bound, max_bound):
    return [(i, el) for i, el in enumerate(lst) if min_bound <= el <= max_bound]

print(search_index(lst1,2,10))
print(search_index(lst1, 2, 9))
print(search_index(lst1, 0, 6))