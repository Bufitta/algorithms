# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна
# завершаться, а должна запрашивать новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
# сообщать ему об ошибке и снова запрашивать знак операции. Также сообщать пользователю
# о невозможности деления на ноль, если он ввел 0 в качестве делителя.

while True:
    print('Введите 2 числа и знак операции')
    a = float(input('a = '))
    b = float(input('b = '))
    sign = input('sign = ')

    if sign == '+':
        result = a + b
        print(result)
    elif sign == '-':
        result = a - b
        print(result)
    elif sign == '*':
        result = a * b
        print(result)
    elif sign == '/':
        if b == 0:
            print('На 0 делить нельзя!')
        else:
            result = a / b
            print(result)
    elif sign == '0':
        break
    else:
        print("Вы ввели недопустимый знак! Разрешенные значения: '0', '+', '-', '*', '/'")

