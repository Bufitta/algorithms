# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль
# за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести
# наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования
# предприятий, чья прибыль ниже среднего.

from collections import namedtuple, defaultdict

n = int(input('Введите количество предприятий (больше 0): '))
Company = namedtuple('Company', ['name', 'profit'])
companies = []
all_profit = 0

for i in range(1, n + 1):
    name = input(f'Введите наименование {i}-го предприятия: ')
    profit = 0
    for j in range(1, 5):
        profit += int(input(f'Введите прибыль предприятия за {j}-й квартал: '))

    all_profit += profit
    companies.append(Company(name, profit))

avg_profit = all_profit / n

d = defaultdict(list)
for company in companies:
    if company.profit < avg_profit:
        d['less_avg'].append(company.name)
    elif company.profit > avg_profit:
        d['more_avg'].append(company.name)

print(f'Средняя прибыль (за год для всех предприятий) равна: {avg_profit}')
print('Предприятия, чья прибыль ниже среднего значения:')
print('\n'.join(d['less_avg']))
print('Предприятия, чья прибыль выше среднего значения:')
print('\n'.join(d['more_avg']))


