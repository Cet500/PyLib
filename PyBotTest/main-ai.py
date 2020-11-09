import logging as log
import config

from aiogram import Bot, Dispatcher, executor, md, types

log.basicConfig(
	filename = "log",
	format   = u'| %(filename)-20s | %(levelname)-8s | %(asctime)s | %(message)s',
	datefmt  = '%d.%m.%Y %H:%M:%S',
	level    = log.INFO
)

dp  = Dispatcher( Bot(config.TOKEN, parse_mode = "HTML") )

log.info("")
log.info("=== start bot... =====================")
log.info("")
log.info("initialization")
log.info("")


@dp.message_handler(commands = ['start'])
async def welcome(message):
	log.info(f"request  | {message.text}")

	if message.from_user.username == "sergoindustries":
		await message.answer("*Добро пожаловать, Хозяйн*")
		log.info(f"response | *Добро пожаловать, Хозяйн*")
	else:
		await message.answer(f"Здравствуй, {message.from_user.first_name}")
		log.info(f"response | Здравствуй, {message.from_user.first_name}")

	locale = message.from_user.locale

	await message.answer(md.text(
		md.bold('Info about your language:'),
		md.text('🔸', md.bold('Code:'), md.code(locale.language)),
		md.text('🔸', md.bold('Territory:'), md.code(locale.territory or 'Unknown')),
		md.text('🔸', md.bold('Language name:'), md.code(locale.language_name)),
		md.text('🔸', md.bold('English language name:'), md.code(locale.english_name)),
		sep = '\n',
	))

@dp.message_handler(commands = ['menu'])
async def open_menu(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard = True)

	markup.add("Выведи настройки", "Давай поговорим", "Что ты можешь?")
	markup.add("Закрой меню")

	if message.from_user.username == "sergoindustries":
		await message.answer("Всё для вас", reply_markup = markup)
	else:
		await message.answer("Меню вызвано", reply_markup = markup)


@dp.message_handler(commands = ['close_menu'], )
async def close_menu(message):
	if message.from_user.username == "sergoindustries":
		await message.answer("Как скажете", reply_markup = types.ReplyKeyboardRemove())
	else:
		await message.answer("Меню отозвано", reply_markup = types.ReplyKeyboardRemove())


@dp.message_handler(commands = ['help'])
async def help_commands(message):
	log.info(f"request  | {message.text}")

	if message.from_user.username == "sergoindustries":
		await message.answer(f"""
Чем могу услужить, Хозяйн?
Вот, что я могу для вас сделать:
			
			<b>/start</b>       - вывести приветствие
			<b>/menu</b>      - показать меню
			<b>/dialog</b>    - завести диалог
			<b>/settings</b> - открыть настройки
			<b>/help</b>       - показать это сообщение
		""")
	else:
		await message.answer(f"""
Нужна помощь, {message.from_user.first_name}?

			<b>/start</b>       - вывести приветствие
			<b>/menu</b>      - показать меню
			<b>/dialog</b>    - завести диалог
			<b>/settings</b> - открыть настройки
			<b>/help</b>       - показать это сообщение
		""")


@dp.message_handler(content_types = ['sticker'])
async def sticker_info(message):
	await message.answer(message.sticker.file_id)


async def send_notice():
	pass


@dp.message_handler()
async def text_commands(message):
	log.info(f"request  | {message.text}")

	if message.text.lower() == "выведи настройки":
		pass
	elif message.text.lower() == "давай поговорим":
		pass
	elif message.text.lower() == "что ты можешь?":
		await help_commands(message)
	elif message.text.lower() == "закрой меню":
		await close_menu(message)
	else:
		await message.answer(message.text)
		log.info(f"echo     | {message.text}")


@dp.message_handler(commands = ['stop'])
async def stop(message):
	if message.from_user.username == "sergoindustries":
		await message.answer("Goodbye, master")
		await Dispatcher.stop_polling(dp)

		log.info(f"send | Goodbye, master")
		log.info("")
		log.info("=== end bot... =======================")
		log.info("")


if __name__ == '__main__':
	executor.start_polling(dp, skip_updates = True)
