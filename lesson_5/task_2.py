# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
# соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

first_hex = input('Введите первое шестнадцатеричное число: ')
sec_hex = input('Введите второе шестнадцатеричное число: ')

hexs = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

def get_num(hex_num):
    num = deque()
    for hn in hex_num:
        num.appendleft(hexs[hn.upper()])
    return num

first_num = get_num(first_hex)
sec_num = get_num(sec_hex)

def get_hex_sum(arrays):
    hex_sum = deque()
    in_mem = 0
    max_array = max(arrays, key=len)
    for i in range(len(max_array)):
        sum_ = in_mem
        for array in arrays:
            if len(array) > i:
                sum_ += array[i]
        if sum_ >= 16:
            hex_sum.appendleft(sum_ % 16)
            in_mem = sum_ // 16
        else:
            hex_sum.appendleft(sum_)
            in_mem = 0

    for idx, num in enumerate(hex_sum):
        for key, value in hexs.items():
            if num == value:
                hex_sum[idx] = key

    return list(hex_sum)

def get_hex_mult(first_num, sec_num):
    arrays = []
    for idx, fn in enumerate(first_num):
        arrays.append(deque())
        in_mem = 0
        for sn in sec_num:
            mult = fn * sn + in_mem
            arrays[idx].append(mult % 16)
            in_mem = mult // 16
        else:
            if in_mem:
                arrays[idx].append(in_mem)

    for idx, deq in enumerate(arrays):
        deq.extendleft([0] * idx)

    return get_hex_sum(arrays)

hex_sum = get_hex_sum([first_num, sec_num])
hex_mult = get_hex_mult(first_num, sec_num)
print(f'Сумма равна {hex_sum}.', f'Произведение равно {hex_mult}.', sep='\n')