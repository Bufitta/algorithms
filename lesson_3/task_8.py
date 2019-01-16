# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в
# последнюю ячейку строки. В конце следует вывести полученную матрицу.

matrix = []
for n in range(1, 6):
    print(f'Введите {n}-ю строку матрицы')
    row = []
    sum_row = 0
    for i in range(1, 4):
        num = int(input(f'Введите {i}-е число {n}-й строки матрицы: '))
        row.append(num)
        sum_row += num
    row.append(sum_row)
    matrix.append(row)

for line in matrix:
    for num in line:
        print(f'{num: > 5}', end='')
    print('\n')
