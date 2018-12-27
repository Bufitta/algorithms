# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного,
# но меньше другого).

print('Введите три целых числа')

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

if b > c:
    if b < a:
        md = b
    else:
        if a > c:
            md = a
        else:
            md = c
else:
    if b < a:
        if a > c:
            md = a
        else:
            md = c
    else:
        md = b

print(md)
