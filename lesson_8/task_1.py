# 1. Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.

s = input('Введите строку, состоящую только из маленьких латинских букв: ')

hash_s = hash(s)
hash_table = []

for i in range(len(s)):
    for j in range(i, len(s)):
        hash_val = hash(s[i:j+1])
        if hash_val != hash_s and hash_val not in hash_table:
            hash_table.append(hash_val)

print(f'Количество различных подстрок в этой строке - {len(hash_table)}')
