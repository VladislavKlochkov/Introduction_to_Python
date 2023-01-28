# 1.3[6]. Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# Примеры/Тесты:
# 385916 >>> yes
# 123456 >>> no
# (*) Усложнение. Вывод результат на экран сделайте одной строкой(только один print), для этого используйте тернарный оператор



number = int(input('Введите номер билета: '))

if number < 0 or number < 10000 or number > 999999:
    print('Введены некорректные данные!')
elif number // 100000 + number // 10000 % 10 + number // 1000 % 10 == number // 100 % 10 + number // 10 % 10 + number % 10:
        print(f'Ваш билет с номером {number} счастливый!')
else:
        print(f'Ваш билет с номером {number} несчастливый!') 



# (*) Усложнение.

print(f'{number} >>> yes' if number // 100000 + number // 10000 % 10 + number // 1000 % 10 == number // 100 % 10 + number // 10 % 10 + number % 10 else f'{number} >>> no')