# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

SIZE = 5
MIN_NUM = 0
MAX_NUM = 100

matrix = [[random.randint(MIN_NUM, MAX_NUM) for _ in range(SIZE)] for _ in range(SIZE)]

min_column = matrix[0]

for line in matrix:
    for idx, num in enumerate(line):
        print(f'{num: > 5}', end='')
        if min_column[idx] > num:
            min_column[idx] = num
    print('\n')

max_value = min_column[0]
for num in min_column:
    print(f'{num: > 5}', end='')
    if num > max_value:
        max_value = num

print('\n')
print(max_value)