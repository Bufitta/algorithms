# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

import cProfile

def test_sum(func):
    lst = [1, -0.5, 0.25, -0.125, 0.0625]
    assert sum(lst) == func(len(lst))
    print('Test is OK')

# 1.
def get_sum(n, a = 1.0, summa = 0):
    if n == 0:
        return summa

    next_a = a * (-0.5)
    summa += a
    return get_sum(n - 1, next_a, summa)

# test_sum(get_sum)

# 100 loops, best of 3: 3.66 usec per loop  - 10
# 100 loops, best of 3: 17 usec per loop - 50
# 100 loops, best of 3: 35.2 usec per loop - 100
# 100 loops, best of 3: 72.5 usec per loop - 200
# 100 loops, best of 3: 373 usec per loop - 900


# cProfile.run('get_sum(200)')
# 11/1    0.000    0.000    0.000    0.000 task_1.py:6(get_sum) - 10
# 51/1    0.000    0.000    0.000    0.000 task_1.py:6(get_sum) - 50
# 101/1    0.000    0.000    0.000    0.000 task_1.py:6(get_sum) - 100
# 201/1    0.000    0.000    0.000    0.000 task_1.py:6(get_sum) - 200

# cProfile.run('get_sum(900)')
   #       904 function calls (4 primitive calls) in 0.002 seconds
   #
   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.001    0.001 <string>:1(<module>)
   #  901/1    0.001    0.000    0.001    0.001 task_1.py:12(get_sum)
   #      1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# 2.
def get_sum2(n):
    lst = []
    for i in range(n):
        lst.append((-0.5)**i)
    return sum(lst)

# test_sum(get_sum2)

# 100 loops, best of 3: 4.41 usec per loop - 10
# 100 loops, best of 3: 16.6 usec per loop - 50
# 100 loops, best of 3: 33 usec per loop - 100
# 100 loops, best of 3: 67 usec per loop - 200
# 100 loops, best of 3: 312 usec per loop - 900


# cProfile.run('get_sum2(10)')

   #       15 function calls in 0.000 seconds
   #
   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
   #      1    0.000    0.000    0.000    0.000 task_1.py:33(summa)
   #      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
   #     10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('get_sum2(50)')
#          55 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_1.py:33(summa)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
#        50    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('get_sum2(100)')
#          105 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_1.py:33(summa)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
#       100    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('get_sum2(200)')
#          205 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_1.py:33(summa)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
#       200    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('get_sum2(900)')
#          905 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.000    0.000    0.001    0.001 task_1.py:46(summa)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
#       900    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#3.
def get_sum3(n):
    result = 0
    for i in range(n):
        result += (-0.5) ** i
    return result

# test_sum(get_sum3)

# 100 loops, best of 3: 2.78 usec per loop - 10
# 100 loops, best of 3: 11.2 usec per loop - 50
# 100 loops, best of 3: 21.9 usec per loop - 100
# 100 loops, best of 3: 44.1 usec per loop - 200
# 100 loops, best of 3: 223 usec per loop - 900

# cProfile.run('get_sum3(10)')
   #       4 function calls in 0.000 seconds
   #
   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
   #      1    0.000    0.000    0.000    0.000 task_1.py:127(get_sum3)
   #      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('get_sum3(50)')
   #       4 function calls in 0.000 seconds
   #
   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
   #      1    0.000    0.000    0.000    0.000 task_1.py:127(get_sum3)
   #      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('get_sum3(100)')
   #       4 function calls in 0.000 seconds
   #
   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
   #      1    0.000    0.000    0.000    0.000 task_1.py:127(get_sum3)
   #      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('get_sum3(200)')
#          4 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_1.py:127(get_sum3)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('get_sum3(900)')
#          4 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_1.py:127(get_sum3)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# ------------------------------------------------------------------------------------
# Вывод: Зависимость линейная. Самый оптимальный алгоритм №3: меньше затраты по времени, количество вызываемых функций не зависит от n.