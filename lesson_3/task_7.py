# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

import random

SIZE = 10
MIN_NUM = 0
MAX_NUM = 100

array = [random.randint(MIN_NUM, MAX_NUM) for _ in range(SIZE)]
print(array)

min_1, min_2 = array[0], array[1]

for num in array[2:]:
    if min_1 > min_2 and min_1 > num:
        min_1 = num
    elif min_2 > num:
        min_2 = num

print([min_1, min_2])
