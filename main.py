
money = int(input('Money: '))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

list_per = list(per_cent.values())
money /= 100

list_per[0] *= money
list_per[1] *= money
list_per[2] *= money
list_per[3] *= money

deposit = list(map(int, list_per))
print('deposit=', deposit)

deposit.sort()
max_dep = deposit[-1]

print('Максимальная сумма, которую вы можете заработать- ', max_dep)










