# 4. Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 10
MIN_NUM = 0
MAX_NUM = 100

array = [random.randint(MIN_NUM, MAX_NUM) for _ in range(SIZE)]
print(array)

max_count = 1
elem = array[0]

for num in set(array):
    count_num = 0
    for val in array:
        if val == num:
            count_num += 1
    if max_count < count_num:
        max_count = count_num
        elem = num

print(elem)

