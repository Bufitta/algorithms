# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 2
MIN_NUM = 0
MAX_NUM = 100

array = [random.randint(MIN_NUM, MAX_NUM) for _ in range(SIZE)]
print(array)

max_elem, max_idx = array[0], 0
min_elem, min_idx = array[0], 0

for idx, num in enumerate(array):
    if max_elem < num:
        max_elem = num
        max_idx = idx
    if min_elem > num:
        min_elem = num
        min_idx = idx

array[max_idx] = min_elem
array[min_idx] = max_elem

print(array)
