# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

def get_sum(a, n, summa):
    if n == 0:
        return summa

    next_a = a * (-0.5)
    summa += a
    return get_sum(next_a, n - 1, summa)


print('Введите количество элементов')
n = input('n = ')

a = 1
summa = 0

result = get_sum(a, int(n), summa)

print(f'Сумма равна {result}')
