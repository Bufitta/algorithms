# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

print('Введите натуральное число')

x = input('x = ')

even_nums = 0
odd_nums = 0

for i in x:
    if int(i) % 2 == 0:
        even_nums += 1
    else:
        odd_nums += 1

print(f'В введенном числе четных цифр: {even_nums}, нечетных: {odd_nums}.')