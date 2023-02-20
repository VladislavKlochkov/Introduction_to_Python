# 6.1[30]: Напишите программу, генерирующую элементы арифметической прогрессии
# Программа принимает от пользователя три числа :

# Первый элемент прогрессии, Разность (шаг) и Количество элементов
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.

# Напишите функцию
# - Аргументы: три указанных параметра
# - Возвращает: список элементов арифмитической прогрессии.

# Примеры/Тесты:
# Ввод: 7 2 5
# Вывод: [7 9 11 13 15]
# Ввод: 2 3 12
# Вывод: [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]

# (*) Усложнение. Для формирования списка внутри функции используйте Comprehension

# (**) Усложнение. Присвоение значений переменным a1,d,n запишите, используя только один input, в одну строку, вам понадобится распаковка и Comprehension или map


a1 = int(input('Введите первый элемент прогрессии: '))
d = int(input('Введите шаг: '))
n = int(input('Введите количество элементов: '))

def create_arith_progression(first_element, step, quantity):
    res = []
    for i in range(quantity):
        res.append(first_element + i * step)
    return res
print(create_arith_progression(a1, d, n))

# (*) Усложнение.

def create_arith_progression(first_element, step, quantity):
    return [first_element + i * step for i in range(quantity)]
print(create_arith_progression(a1, d, n))

# (**) Усложнение.

a1, d, n = map(int, input().split())
a1, d, n = [int(el) for el in input().split()]

def create_arith_progression(first_element, step, quantity):
    return [first_element + i * step for i in range(quantity)]
print(create_arith_progression(a1, d, n))