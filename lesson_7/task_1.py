# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный
# и отсортированный массивы. Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).

import random

SIZE = 10
MIN_NUM = -100
MAX_NUM = 99

array = [random.randint(MIN_NUM, MAX_NUM) for _ in range(SIZE)]
print(array)


def bubble_sort(lst):
    n = 0
    while n < len(lst) - 1:
        for i in range(len(lst) - n - 1):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        n += 1


bubble_sort(array)

print(array)
