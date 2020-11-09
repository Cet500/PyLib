import telebot as tbot
import logging as log
import config

from telebot import types

log.basicConfig(
	filename = "log",
	format   = u'| %(filename)-20s | %(levelname)-8s | %(asctime)s | %(message)s',
	datefmt  = '%d.%m.%Y %H:%M:%S',
	level    = log.INFO
)

bot = tbot.TeleBot(config.TOKEN, config.PARSE_MODE)

log.info("")
log.info("=== start bot... =====================")
log.info("")
log.info("initialization")
log.info("")


@bot.message_handler(commands = ['start'])
def welcome(message):
	log.info(f"request  | {message.text}")

	if message.from_user.username == "sergoindustries":
		bot.send_message(message.chat.id, "*Добро пожаловать, Хозяйн*")
		log.info(f"response | *Добро пожаловать, Хозяйн*")
	else:
		bot.send_message(message.chat.id, f"Здравствуй, {message.from_user.first_name}")
		log.info(f"response | Здравствуй, {message.from_user.first_name}")


@bot.message_handler(commands = ['menu'])
def open_menu(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard = True)

	key_settings = types.KeyboardButton("Выведи настройки")
	key_dialog   = types.KeyboardButton("Давай поговорим")
	key_help     = types.KeyboardButton("Что ты можешь?")
	key_exit     = types.KeyboardButton("Закрой меню")

	markup.add(key_settings, key_dialog, key_help, key_exit)

	if message.from_user.username == "sergoindustries":
		bot.send_message(message.chat.id, "Всё для вас", reply_markup = markup)
	else:
		bot.send_message(message.chat.id, "Меню вызвано", reply_markup = markup)


@bot.message_handler(commands = ['close_menu'], )
def close_menu(message):
	if message.from_user.username == "sergoindustries":
		bot.send_message(message.chat.id, "Как скажете", reply_markup = types.ReplyKeyboardRemove())
	else:
		bot.send_message(message.chat.id, "Меню отозвано", reply_markup = types.ReplyKeyboardRemove())


@bot.message_handler(commands = ['help'])
def help_commands(message):
	log.info(f"request  | {message.text}")

	if message.from_user.username == "sergoindustries":
		bot.send_message(message.chat.id, f"Чем могу услужить, Хозяйн?")
		log.info(f"response | Чем могу услужить, Хозяйн?")
	else:
		bot.send_message(message.chat.id, f"Нужна помощь, {message.from_user.first_name}?")
		log.info(f"response | Нужна помощь, {message.from_user.first_name}")

	bot.send_message(message.chat.id, f"""
		Вот, что я могу для вас сделать, {message.from_user.first_name}:
		
		*/start*    - вывести приветствие
		*/menu*     - показать меню
		*/dialog*   - завести диалог
		*/settings* - открыть настройки
		*/help*     - показать это сообщение
	""")


@bot.message_handler(content_types = ['sticker'])
def sticker_info(message):
	bot.send_message(message.chat.id, message.sticker.file_id)
	bot.send_sticker(message.chat.id, message.sticker.file_id)


def send_notice():
	pass


@bot.message_handler(content_types = ['text'])
def text_commands(message):
	log.info(f"request  | {message.text}")

	if message.text.lower() == "выведи настройки":
		pass
	elif message.text.lower() == "давай поговорим":
		pass
	elif message.text.lower() == "что ты можешь?":
		help_commands(message)
	elif message.text.lower() == "закрой меню":
		close_menu(message)
	else:
		bot.send_message(message.chat.id, message.text)
		log.info(f"echo    | {message.text}")


@bot.message_handler(commands = ['stop'])
def stop(message):
	if message.from_user.username == "sergoindustries":
		bot.send_message(message.chat.id, "Goodbye, master")
		bot.stop_bot()
		log.info(f"send | Goodbye, master")
		log.info("")
		log.info("=== end bot... =======================")
		log.info("")


if __name__ == '__main__':
	bot.polling(none_stop = True)
