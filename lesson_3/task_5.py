# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и
# позицию в массиве.

import random

SIZE = 10
MIN_NUM = -100
MAX_NUM = 100

array = [random.randint(MIN_NUM, MAX_NUM) for _ in range(SIZE)]
print(array)

min_elem, min_idx = None, None

for idx, num in enumerate(array):
    if num < 0:
        if min_elem is None or min_elem < num:
            min_elem = num
            min_idx = idx
if min_elem:
    print(f'максимальный отрицательный элемент {min_elem} находится в позиции {min_idx}')
else:
    print('В массиве нет отрицательных чисел')