import telebot

def send_welcome(message, bot):
    welcome_message = (
        "Привіт! Виберіть жанр фільмів, для отримання Топ 5:\n"
        "Натисніть одну з кнопок нижче."
    )
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add("Horror", "Comedy")
    markup.add("Action", "Drama")
    markup.add("Romance", "Thriller")
    bot.send_message(message.chat.id, welcome_message, reply_markup=markup)

def handle_unknown(message, bot):
    bot.send_message(message.chat.id, "Будь ласка, виберіть жанр з клавіатури.")
