import logging
import requests
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

API_KEY = "6e1459c841a45c152650b135d1ccc147"  # замініть на ваш API ключ
API_URL = "https://api.themoviedb.org/3/discover/movie"

# Збереження всіх жанрів і їх ID
GENRES = {
    'horror': 27,  # Horror
    'comedy': 35,  # Comedy
    'action': 28,  # Action
    'drama': 18,   # Drama
    'romance': 10749,  # Romance
    'thriller': 53  # Thriller
}

# Параметри запиту до API
def get_movies_by_genre(genre_id):
    params = {
        "api_key": API_KEY,
        "with_genres": genre_id,
        "language": "en-US",
        "sort_by": "popularity.desc",  # сортування за популярністю
    }
    try:
        response = requests.get(API_URL, params=params)
        response.raise_for_status()
        data = response.json()
        movies = data.get("results", [])
        return [movie['title'] for movie in movies]
    except requests.exceptions.RequestException as e:
        logging.error(f"Помилка при запиті до API: {e}")
        return []

# Обробник команди /start
async def start(update: Update, context: CallbackContext) -> None:
    welcome_message = (
        "Привіт! Виберіть жанр фільмів, для отримання Топ 5:\n"
        "Натисніть одну з кнопок нижче."
    )

    # Клавіатура для вибору жанру
    genre_keyboard = [
        ['Horror', 'Comedy'],
        ['Action', 'Drama'],
        ['Romance', 'Thriller']
    ]
    reply_markup = ReplyKeyboardMarkup(genre_keyboard, one_time_keyboard=True, resize_keyboard=True)

    await update.message.reply_text(welcome_message, reply_markup=reply_markup)

# Обробник вибору жанру
async def genre_selected(update: Update, context: CallbackContext) -> None:
    genre = update.message.text.lower()  # отримуємо текст жанру з повідомлення
    genre_id = GENRES.get(genre)

    if genre_id:
        movies = get_movies_by_genre(genre_id)
        if movies:
            response = f"Топ 5 фільмів жанру {genre.capitalize()}:\n"
            for i, movie in enumerate(movies[:5], 1):
                response += f"{i}. {movie}\n"
            await update.message.reply_text(response)
        else:
            await update.message.reply_text("Не вдалося отримати фільми.")
    else:
        await update.message.reply_text("Жанр не знайдений. Спробуйте ще раз.")

# Основна функція
def main():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)

    TOKEN = "7920269200:AAHpB3ytblo6pQTjJfGIPOCUCtwj0lQTdYM"  # замініть на ваш токен

    application = Application.builder().token(TOKEN).build()

    # Додавання обробників
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, genre_selected))

    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()
