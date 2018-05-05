import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import ephem
import datetime
import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
	level=logging.INFO,
	filename='bot.log')

def start_bot(bot, update):
	greeting = """Welcome {}!
I'm just a simple bot and understand only /start command yet.
But stay tuned - I'll be updating! I promise! =)
""".format(update.message.chat.first_name)
	logging.info('User {} press /start'.format(update.message.chat.username))
	update.message.reply_text(greeting)

# def stop_bot(bot, update):
# 	logging.info('User {} press /stop. Stopping the bot...'.format(update.message.chat.username))
# 	update.message.reply_text('Stopping the bot...')
# 	update.stop()

# def cancel(bot, update):
#     user = update.message.from_user
#     logging.info("User %s canceled the conversation.", user.first_name)
#     update.message.reply_text('Bye! I hope we can talk again some day.',
#                                reply_markup=ReplyKeyboardRemove())

#     return ConversationHandler.END

# def shutdown():
#     updater.stop()
#     updater.is_idle = False
# def stop_bot(bot, update):
#     threading.Thread(target=shutdown).start()

def chat(bot, update):
	text = update.message.text
	logging.info(text)
	update.message.reply_text(text)

def planet(bot, update, args):
	logging.info('User {} call /planet command for {}'.format(update.message.chat.username, args[0]))
	update.message.reply_text('User {} call /planet command for {}'.format(update.message.chat.username, args[0]))
	if args[0] == "Mars":
		response = (ephem.constellation(ephem.Mars(datetime.datetime.now().strftime('%Y/%m/%d'))))
	elif args[0] == "Venus":
		response = (ephem.constellation(ephem.Venus(datetime.datetime.now().strftime('%Y/%m/%d'))))
	elif args[0] == "Moon":
		response = (ephem.constellation(ephem.Moon(datetime.datetime.now().strftime('%Y/%m/%d'))))
	else:
		response = "Can't find this planet. Use Mars, Venus or Moon"		
	update.message.reply_text(response)

def main():
	upd = Updater(settings.TELEGRAM_API_KEY)
	dp = upd.dispatcher
	dp.add_handler(CommandHandler("start", start_bot))
	# dp.add_handler(CommandHandler("stop", stop_bot))
	# dp.add_handler(CommandHandler("stop", cancel))
	dp.add_handler(CommandHandler("planet", planet, pass_args=True))
	dp.add_handler(MessageHandler(Filters.text, chat))
	upd.start_polling()
	upd.idle()

if __name__ == '__main__': #чтобы код функции не запускался автоматом при импорте куда-то еще
	logging.info('Bot started')
	main()