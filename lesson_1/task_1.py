print('Введите целое трехзначное число')

x = input('x = ')

a, b, c = int(x[0]), int(x[1]), int(x[2])
s = a + b + c
p = a * b * c

print(f'Cумма: {s}\nПроизведение: {p}')
