#Импортирование библиотеки и подключение токена телеграмм бота
import telebot
bot = telebot.TeleBot('1873515847:AAG7RLD_yInLij0AbrQL9MtAiEtJjrh6zMo')

#Обработка текстовых команд /start и /help
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Приятно познакомиться {message.from_user.first_name}. Меня зовут Джарвис.')

#Запуск бота на непрерывное отслеживание сообщений
bot.polling(none_stop=True)
