import telebot
from Config import money, TOKEN
from extensions import ConvertException, CryptoConverter


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = '''Для начала работы введите команду в следующем формате:\n
<имя валюты цену которой он хочет узнать> <мя валюты в которой надо узнать цену первой валюты> <количество переводимой валюты>\n
Увидеть список всех доступных валют: /values'''
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = "Доступные валюты: "
    text = '\n'.join((text, *sorted(money.keys())))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(" ")
        if len(values) != 3:
            raise ConvertException('Слишком много параметров.')
        v_1, v_2, amount = values
        total_base = CryptoConverter.convert(v_1, v_2, amount)
    except ConvertException as e:
        bot.reply_to(message, f'Ошибка пользователя\n {e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n {e}')
    else:
        text = f'Цена {amount} {v_1} в {v_2} - {total_base}'
        bot.send_message(message.chat.id, text)


bot.polling()


