per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму: "))
list_1=list(per_cent.values())
deposit = [list_1[0]*money, list_1[1]*money, list_1[2]*money, list_1[3]*money]
deposit_i=max(deposit)
print('Сумма процентов по вкладам: ', deposit)
print('Наивысшая доходность по вкладам: ', deposit_i)
