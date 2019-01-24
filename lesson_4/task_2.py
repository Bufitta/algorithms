import cProfile, math

def get_simple_num(i):
    num = 2
    idx = 1
    while i != idx:
        num += 1
        simple = False
        if num % 2 == 0 and num != 2:
            continue
        for n in range(1, num + 1):
            if num % n == 0 and n != 1 and n != num:
                simple = False
                break
            elif num % n == 0:
                simple = True
        if simple:
            idx += 1
    return num

def test_simple(func):
    simple_nums = [2, 3, 5, 7, 11, 13, 17, 19]
    for idx, num in enumerate(simple_nums):
        assert num == func(idx+1)
        print(f'Test ({num}) is OK')

# test_simple(get_simple_num)

# 100 loops, best of 3: 35.7 usec per loop - 10
# 100 loops, best of 3: 903 usec per loop - 50
# 100 loops, best of 3: 4.1 msec per loop - 100
# 100 loops, best of 3: 19.6 msec per loop - 200
# 100 loops, best of 3: 715 msec per loop - 1000

# cProfile.run('get_simple_num(10)')
   #       4 function calls in 0.000 seconds
   #
   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
   #      1    0.000    0.000    0.000    0.000 task_2.py:3(get_simple_num)
   #      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# cProfile.run('get_simple_num(100)')
   #       4 function calls in 0.005 seconds
   #
   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.004    0.004 <string>:1(<module>)
   #      1    0.004    0.004    0.004    0.004 task_2.py:3(get_simple_num)
   #      1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('get_simple_num(1000)')
#          4 function calls in 0.790 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.790    0.790 <string>:1(<module>)
#         1    0.790    0.790    0.790    0.790 task_2.py:3(get_simple_num)
#         1    0.000    0.000    0.790    0.790 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# --------------------------------------------------------------------------------------
#2.

def get_sieve(start, n):
    sieve = [i for i in range(start, n)]
    return sieve

def get_simple_num2(i):
    size = int(i * math.log(i))

    sieve = []
    result = []

    while len(result) < i:
        start = len(sieve)
        sieve.extend(get_sieve(start, start + size))

        try:
            idx = sieve.index(1)
            sieve[idx] = 0
        except:
            pass

        end = len(sieve)
        for m in range(2, end):
            if sieve[m] != 0:
                j = m + m
                while j < end:
                    sieve[j] = 0
                    j += m

        result = [num for num in sieve if num != 0]
        size = i

    return result[i-1]


# test_simple(get_simple_num2)

# 100 loops, best of 3: 24 usec per loop - 10
# 100 loops, best of 3: 159 usec per loop - 50
# 100 loops, best of 3: 395 usec per loop - 100
# 100 loops, best of 3: 942 usec per loop - 200
# 100 loops, best of 3: 10.5 msec per loop - 1000


# cProfile.run('get_simple_num2(10)')

   #       22 function calls in 0.000 seconds
   #
   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
   #      2    0.000    0.000    0.000    0.000 task_2.py:40(get_sieve)
   #      2    0.000    0.000    0.000    0.000 task_2.py:41(<listcomp>)
   #      1    0.000    0.000    0.000    0.000 task_2.py:44(get_simple_num2)
   #      2    0.000    0.000    0.000    0.000 task_2.py:68(<listcomp>)
   #      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
   #      7    0.000    0.000    0.000    0.000 {built-in method builtins.len}
   #      1    0.000    0.000    0.000    0.000 {built-in method math.log}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   #      2    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
   #      2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}


# cProfile.run('get_simple_num2(100)')
   #       22 function calls in 0.001 seconds
   #
   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.000    0.000 <string>:1(<module>)
   #      2    0.000    0.000    0.000    0.000 task_2.py:40(get_sieve)
   #      2    0.000    0.000    0.000    0.000 task_2.py:41(<listcomp>)
   #      1    0.000    0.000    0.000    0.000 task_2.py:44(get_simple_num2)
   #      2    0.000    0.000    0.000    0.000 task_2.py:68(<listcomp>)
   #      1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
   #      7    0.000    0.000    0.000    0.000 {built-in method builtins.len}
   #      1    0.000    0.000    0.000    0.000 {built-in method math.log}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   #      2    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
   #      2    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}

# cProfile.run('get_simple_num2(1000)')
   #       30 function calls in 0.011 seconds
   #
   # Ordered by: standard name
   #
   # ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   #      1    0.000    0.000    0.011    0.011 <string>:1(<module>)
   #      3    0.000    0.000    0.000    0.000 task_2.py:40(get_sieve)
   #      3    0.000    0.000    0.000    0.000 task_2.py:41(<listcomp>)
   #      1    0.009    0.009    0.011    0.011 task_2.py:44(get_simple_num2)
   #      3    0.001    0.000    0.001    0.000 task_2.py:68(<listcomp>)
   #      1    0.000    0.000    0.011    0.011 {built-in method builtins.exec}
   #     10    0.000    0.000    0.000    0.000 {built-in method builtins.len}
   #      1    0.000    0.000    0.000    0.000 {built-in method math.log}
   #      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   #      3    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
   #      3    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}

# ------------------------------------------------------------------------------------
# Вывод: Алгоритм с решетом Эратосфена значительно быстрее, более чем
# в 70 раз для 1000-ого простого числа.