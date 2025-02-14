import asyncio
import nest_asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Применяем фиксацию для Render
nest_asyncio.apply()

# Токен Telegram-бота
TOKEN = "8064353519:AAGqu6DXLbldnJLJ6OlkxqWH5d4xYbfycI8"

# Переменная для хранения курса
current_rate = 100.00  # Базовый курс

# Команда /start
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text(
        "Привет! Я бот для обменного курса USDT/RUB.\n"
        "📌 Получить курс: /getrate\n"
        "✍ Изменить курс: /setrate <курс>"
    )

# Команда /getrate
async def get_rate(update: Update, context: CallbackContext):
    await update.message.reply_text(f"Текущий курс: 1 USDT = {current_rate} RUB")

# Команда /setrate (изменение курса)
async def set_rate(update: Update, context: CallbackContext):
    global current_rate
    try:
        rate = float(context.args[0])  # Получаем курс из аргумента
        current_rate = rate
        await update.message.reply_text(f"✅ Курс обновлен: 1 USDT = {current_rate} RUB")
    except (IndexError, ValueError):
        await update.message.reply_text("❌ Ошибка! Используй: /setrate <курс>")

# Запуск бота (исправленный)
async def main():
    app = Application.builder().token(TOKEN).build()

    # Регистрируем команды
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("getrate", get_rate))
    app.add_handler(CommandHandler("setrate", set_rate))

    print("🤖 Бот запущен...")
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())  # Без конфликта event loop
