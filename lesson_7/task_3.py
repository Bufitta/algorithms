# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две
# равные части: в одной находятся элементы, которые не меньше медианы, в другой –
# не больше медианы. Задачу можно решить без сортировки исходного массива. Но если
# это слишком сложно, то используйте метод сортировки, который не рассматривался
# на уроках
import random

m = int(input('Введите натуральное число m: '))

SIZE = 2 * m + 1
MIN_NUM = -1000
MAX_NUM = 1000

array = [random.randint(MIN_NUM, MAX_NUM) for _ in range(SIZE)]
print(array)

avg_idx = SIZE // 2

def get_median(lst, idx):
    lt = []
    gt = []
    eq = []
    for val in lst:
        if val < lst[idx]:
            lt.append(val)
        elif val > lst[idx]:
            gt.append(val)
        else:
            eq.append(val)

    if len(eq) > 1:
        for i in eq[1:]:
            if len(lt) <= len(gt):
                lt.append(i)
            else:
                gt.append(i)

    if len(lt) == idx:
        return eq[0]
    elif len(lt) > idx:
        return get_median(lt, idx)
    else:
        return get_median(gt, idx - len(lt) - 1)

print(get_median(array, avg_idx))