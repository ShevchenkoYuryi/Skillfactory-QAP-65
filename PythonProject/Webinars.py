
                                          # МОДУЛЬ 16 ООП и классы в Python
import math
# 1 TASK
print('ВВедите длины сторон треугольника')

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
p = a + b + c / 2
s = math.sqrt (p * (p - a) * (p - b) * (p - c))
print ("P = %d; S=%.2f" % (p, s))

# 2 TASK
n = int(input("Введите трехзначное число: "))
num1 = n % 10
num2 = n % 100 // 10
num3 = n // 100
print("Сумма цифр: ", num1 + num2 + num3)
print("Произведение цифр: ", num1 * num2 * num3)


# 3 TASK
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))

m = a
if m < b:
  m = b
if m < c:
  m = c
print (m)

# 4 TASK
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
if b < a < c or c < a < b:
  print("Среднее:", a)
elif a < b < c or c < b < a:
  print("Среднее:", b)
else:
  print("Среднее:", c)


# 5 TASK

import random

num = random.randint(1, 100)

while True:
  print("Угадайте число от 1 до 100")
  guess = int(input())
  if guess == num:
    print ('Правильно')
    break
  elif guess < num:
    print('Загаданное число больше')
  elif guess > num:
    print('Загаданное число меньше')

# 6 TASK (Сумма чисел из числа)
num = int(input('Введите целое число: '))
num1 = 0

while num > 0:
  digit = num % 10
  num = num // 10
  num1 = num1 * 10
  num1 = num1 + digit
print(num1)


# 6 TASK (количество четных и не четных чисел)
a = int(input())
even = 0
odd = 0

while a > 0:
  if a % 2 == 0:
    even += 1
  else:
    odd += 1
  a = a // 10
print("Even: %d, odd: %d" % (even, odd))


7 TASK (рекурсия)
n = int(input())
factorial = 1
while n > 1:
  factorial = factorial * n
  n -= 1
print(factorial)

n = int(input())
factorial = 1
for i in range(1, n+1):
  factorial = factorial * i
print(factorial)


8 TASK (таблица умножения)
for i in range(1, 10):
  for j in range(1, 10):
    print(i * j, end='\t')
  print('\n')


9 TASK (циклы в списках)
lst = []
for item in range(18, 1, -4):
    lst.append(item)
print(lst)

s = 10000 ** 2
d = 10000 * 13.288
x = s / d
print(f'{x:.3f}')
print(f'{x:2.10f}')
