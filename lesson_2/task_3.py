# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и
# вывести на экран. Например, если введено число 3486, то надо вывести число 6843.


print('Введите натуральное число')

x = input('x = ')

reverse_num = ''

for i in x:
    reverse_num = i + reverse_num

print(int(reverse_num))