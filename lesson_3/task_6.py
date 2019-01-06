# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и
# максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 10
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

new_array = array[max_idx + 1:min_idx] if max_idx < min_idx else array[min_idx + 1:max_idx]
print(new_array)

summa = 0
for num in new_array:
    summa += num

print(summa)
