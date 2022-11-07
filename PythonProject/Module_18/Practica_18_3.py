import telebot

TOKEN = '5784962834:AAHNJ7WF0UqDI1jcYwrtQQYc8jMThXoPFBM'

bot = telebot.TeleBot(TOKEN)


# @bot.message_handler(commands=['start', 'help'])
# def hadle_start_help(message):
#     pass
#
# @bot.message_handler(content_types=['document', 'audio'])
# def handle_docs_audio(message):
#     pass

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Welcome, {message.chat.username}")

@bot.message_handler(content_types=['photo', ])
def handle_photo(message: telebot.types.Message):
    bot.reply_to(message, 'Nice meme XDD')




bot.polling(none_stop=True)