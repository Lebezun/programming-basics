import os
import telebot
from dotenv import load_dotenv
from api import get_movies_by_genre
from handlers import send_welcome, handle_unknown as handle_unknown_message
from decorators import log_message

load_dotenv('token.env')

TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)

def main():
    @bot.message_handler(commands=['start'])
    def start_welcome(message):
        send_welcome(message, bot)

    @bot.message_handler(func=lambda message: message.text.lower() in ['horror', 'comedy', 'action', 'drama', 'romance', 'thriller'])
    @log_message
    def genre_selected(message):
        genre = message.text.lower()
        movies = get_movies_by_genre(genre)
        if movies:
            response = f"Топ 5 фільмів жанру {genre.capitalize()}:\n"
            for i, movie in enumerate(movies[:5], 1):
                response += f"{i}. {movie}\n"
            bot.send_message(message.chat.id, response)
        else:
            bot.send_message(message.chat.id, "Не вдалося отримати фільми.")

    @bot.message_handler(func=lambda message: True)
    @log_message
    def handle_unknown(message):
        handle_unknown_message(message, bot)

    print("Бот запущено...")
    bot.infinity_polling()

if __name__ == "__main__":
    main()
