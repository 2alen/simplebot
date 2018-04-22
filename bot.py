import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
	level=logging.INFO,
	filename='bot.log')

def start_bot(bot, update):
	greeting = """Welcome {}!

I'm just a simple bot and understanf only /start command yet.
But stay tuned - I'll be updating! I promise! =)
""".format(update.message.chat.first_name)
	update.message.reply_text(greeting)

def chat(bot,update):
	text = update.message.text
	logging.info(text)
	update.message.reply_text(text)

def main():
	upd = Updater(settings.TELEGRAM_API_KEY)
	dp = upd.dispatcher
	dp.add_handler(CommandHandler("start", start_bot))
	dp.add_handler(MessageHandler(Filters.text, chat))
	upd.start_polling()
	upd.idle()

if __name__ == '__main__': #чтобы код функции не запускался автоматом при импорте куда-то еще
	logging.info('Bot started')
	main()