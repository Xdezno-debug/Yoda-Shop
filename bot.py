import os
import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters,
)

logging.basicConfig(level=logging.INFO)

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["🛍 Каталог", "🛒 Корзина"],
        ["📦 Мои заказы", "💬 Поддержка"],
    ]

    from telegram import ReplyKeyboardMarkup
    await update.message.reply_text(
        "🐼 Добро пожаловать в YODA SHOP!\n\nВыберите нужный раздел:",
        reply_markup=ReplyKeyboardMarkup(
            keyboard, resize_keyboard=True
        ),
    )

def main():
    if not TOKEN:
        raise ValueError("Не задан BOT_TOKEN")

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
