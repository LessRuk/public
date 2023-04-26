money = int(input('insert money:'))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = {}
deposit = list(per_cent.values())
for i in range(0,4,1):
  deposit[i] = int(money*float(deposit[i])/100)
print(deposit)
print('Максимальная сумма, которую вы можете заработать —', max(deposit))