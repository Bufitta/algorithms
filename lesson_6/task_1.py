import sys

def get_size(var, sum_):
    sum_ += sys.getsizeof(var)

    if hasattr(var, '__iter__') and type(var) != str:
        if type(var) == dict:
            for k in var.keys():
                sum_ = get_size(k, sum_)
            for v in var.values():
                sum_ = get_size(v, sum_)
        else:
            for i in var:
                sum_ = get_size(i, sum_)

    return sum_

def summary_size(vars):
    sum_size = 0

    for var in vars.values():
        sum_size = get_size(var, sum_size)

    return sum_size

# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

# 1.
def get_sum(n, a = 1.0, summa = 0):
    if n == 0:
        global lcl
        lcl = locals()
        return summa

    next_a = a * (-0.5)
    summa += a
    return get_sum(n - 1, next_a, summa)

# 2.
def get_sum2(n):
    lst = []
    for i in range(n):
        lst.append((-0.5)**i)

    global lcl2
    lcl2 = locals()

    return sum(lst)


#3.
def get_sum3(n):
    result = 0

    for i in range(n):
        result += (-0.5) ** i

    global lcl3
    lcl3 = locals()

    return result

get_sum(20)
get_sum2(20)
get_sum3(20)
print(summary_size(lcl))
print(summary_size(lcl2))
print(summary_size(lcl3))

# Версия Python 3.6.2, разрядность 64 бита
# Результаты:
# 72
# 800
# 80
#
# Меньше всего памяти расходует первый вариант, больше всего - второй. При этом
# увелечение значения n не отражается на размере расходуемой памяти в первой и
# третьей функциях, оно остается постоянным. А для второй функции отмечен рост в
# геометрической прогрессии.
