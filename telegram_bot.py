import logging
import requests
from telebot import Update, ReplyKeyboardMarkup
from telebot import Application, CommandHandler, MessageHandler, filters, CallbackContext

API_KEY = "6e1459c841a45c152650b135d1ccc147"
API_URL = "https://api.themoviedb.org/3/discover/movie"

GENRES = {
    'horror': 27,
    'comedy': 35,
    'action': 28,
    'drama': 18,
    'romance': 10749,
    'thriller': 53
}

def get_movies_by_genre(genre_id):
    params = {
        "api_key": API_KEY,
        "with_genres": genre_id,
        "language": "en-US",
        "sort_by": "popularity.desc",
    }
    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()
        data = response.json()
        movies = data.get("results", [])
        return [movie['title'] for movie in movies]
    except requests.RequestException as e:
        logging.error(f"Помилка при запиті до API: {e}")
        return []

def start(update: Update, context: CallbackContext) -> None:
    welcome_message = (
        "Привіт! Виберіть жанр фільмів, для отримання Топ 5:\n"
        "Натисніть одну з кнопок нижче."
    )

    genre_keyboard = [
        ['Horror', 'Comedy'],
        ['Action', 'Drama'],
        ['Romance', 'Thriller']
    ]
    reply_markup = ReplyKeyboardMarkup(genre_keyboard, one_time_keyboard=True, resize_keyboard=True)

    update.message.reply_text(welcome_message, reply_markup=reply_markup)

def genre_selected(update: Update, context: CallbackContext) -> None:
    genre = update.message.text.lower()
    genre_id = GENRES.get(genre)

    if genre_id:
        movies = get_movies_by_genre(genre_id)
        if movies:
            response = f"Топ 5 фільмів жанру {genre.capitalize()}:\n"
            for i, movie in enumerate(movies[:5], 1):
                response += f"{i}. {movie}\n"
            update.message.reply_text(response)
        else:
            update.message.reply_text("Не вдалося отримати фільми.")
    else:
        update.message.reply_text("Жанр не знайдений. Спробуйте ще раз.")

def main():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)

    TOKEN = "7920269200:AAHpB3ytblo6pQTjJfGIPOCUCtwj0lQTdYM"

    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, genre_selected))

    application.run_polling()

if __name__ == '__main__':
    main()
