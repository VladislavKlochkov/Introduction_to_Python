# 4.2[24]: В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растет N кустов. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом. На входе задано количество ягод на каждом кусте. Не обязательно вводить их с клавиатуры, 
# можно задать непосредственно в коде программы

# Примеры/Тесты:
# Input1: 1, 2, 3, 4, 5, 6, 7, 8
# Output1: Макс. кол-во ягод 21, собрано для куста 7

# Input1: 11, 92, 1, 42, 15, 12, 11, 81
# Output1: Макс. кол-во ягод 184, собрано для куста 1


bushes_number = int(input())
berries_number = [1, 2, 3, 4, 5, 6, 7, 8]
# berries_number = [11, 92, 1, 42, 15, 12, 11, 81]
res_sum = 0
pos = 0

for i in range(1, bushes_number - 1):
    current_sum = berries_number[i-1] + berries_number[i] + berries_number[i+1]
    if current_sum > res_sum:
        res_sum = current_sum
        pos = i+1
if berries_number[-2] + berries_number[-1] + berries_number[0] > res_sum:
    res_sum = berries_number[0] + berries_number[-1] + berries_number[-2]
    pos = bushes_number
if berries_number[0] + berries_number[1] + berries_number[-1] > res_sum:
    res_sum = berries_number[-1] + berries_number[0] + berries_number[1]
    pos = 1

print(f'Максимальное количество ягод {res_sum}, собрано для куста {pos}')