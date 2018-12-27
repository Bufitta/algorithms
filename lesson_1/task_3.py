# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

print('Введите целое число от 1 до 26')

x = int(input('x = '))

eng = 'abcdefghijklmnopqrstuvwxyz'
alpha = eng[x-1]

print(alpha)