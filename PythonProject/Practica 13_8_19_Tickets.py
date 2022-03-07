ticket = int(input("Количество  приобретаебых билетов - "))
price=[]
for i in range(1, ticket+1):
   age = int(input('Введите ваш возраст - '))
   if age < 18:
      price.append(0)
   elif 18 <= age <= 25:
      price.append(990)
   else:
      price.append(1390)
print('Стоимость билетов ВСЕГО =', sum(price))
if ticket >= 3:
   a = sum(price)*10/100
   print("Сумма вашей скидки (10%) -", a)
   print("Итого к оплате -", sum(price)-a)
else:
   print("Сумма вашей скидки (0%) - 0")
   print("Итого к оплате -", sum(price))