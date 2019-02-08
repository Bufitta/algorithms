# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и
# отсортированный массивы.
import random

SIZE = 10
MIN_NUM = 0
MAX_NUM = 50

array = [round(random.uniform(MIN_NUM, MAX_NUM), 2) for _ in range(SIZE)]
print(array)


def merge(lst1, lst2):
    result = []

    while len(lst1) and len(lst2):
        min1 = min(lst1)
        min2 = min(lst2)
        if min1 < min2:
            result.append(lst1.pop(lst1.index(min1)))
        else:
            result.append(lst2.pop(lst2.index(min2)))

    if len(lst1):
        result.extend(lst1)
    if len(lst2):
        result.extend(lst2)

    return result


def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    middle = len(lst) / 2
    left_lst = []
    right_lst = []
    for i in range(len(lst)):
        if i < middle:
            left_lst.append(lst[i])
        else:
            right_lst.append(lst[i])

    left_lst = merge_sort(left_lst)
    right_lst = merge_sort(right_lst)
    result = merge(left_lst, right_lst)

    return result


print(merge_sort(array))