# Кэширование файлов. Redis

import redis
import json

call_num = redis.Redis(
    host='хост',
    port=порт,
    password='пароль'
)

help = '''Список команд:
* ad - добавить контакт
* show - показать контакт
* del - удалить номер
* exit - выход из программы'''

while True:
    print('------------------------------------------------------')
    command = str(input('Введите команду: '))
    if command == 'ad':
        name = str(input('Введите имя контакта: '))
        phone_num = str(input('Введите номер контакта: '))
        call_num.set(name, phone_num)
        print(f"Добавлен контакт {name} номер: {call_num.get(name)}")

    elif command == 'show':
        name = str(input('Введите имя контакта: '))
        print(f"{name} номер: {call_num.get(name)}")

    elif command == 'del':
        name = str(input('Введите имя контакта: '))
        call_num.delete(name)
        print(f"Контакт {name} удален")

    elif command == 'help':
        print(help)

    elif command == 'exit':
        print('Спасибо что воспользовались нашим сервисом')
        break

    else:
        print("Неизвестная команда!")
        print(help)