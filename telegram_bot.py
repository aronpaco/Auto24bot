from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from auto24_bot import scrape_auto24

TELEGRAM_TOKEN = '6489915608:AAFxCr4yNb5DyicAZNnnywvE0U3HfFAy7BM'  # Replace with your actual bot token
bot = Bot(token=TELEGRAM_TOKEN)

def start(update, context):
    update.message.reply_text('Hello! I am your auto24 bot.')

def handle_message(update, context):
    user_message = update.message.text.lower()
    if 'hello' in user_message:
        update.message.reply_text('Hello there!')

if __name__ == '__main__':
    updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Add command and message handlers
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Start the bot's polling
    updater.start_polling()

    # Run the scraping logic
    scrape_auto24()
