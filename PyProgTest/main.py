import tkinter as tk
import logging as log
import json
import uuid

log.basicConfig(
	filename = "log",
	format   = u'| %(filename)-10s | %(levelname)-8s | %(asctime)s | %(message)s',
	datefmt  = '%d.%m.%Y %H:%M:%S',
	level    = log.DEBUG
)

log.debug("")
log.info("=== start program... =====================")
log.debug("")
log.debug("initialization")

try:
	with open("data.json", 'rt', encoding = "utf-8") as read_file:
		json_str = read_file.read()
		if json_str:
			log.info("success: open file data.json")
			try:
				data = json.loads(json_str)
				log.info("success: load objects from file data.json")
			except json.decoder.JSONDecodeError:
				log.warning("warn: error load objects from file data.json")
		else:
			log.warning("warn: not data in file data.json")
except IOError:
	log.warning("warn: not found file data.json")
	with open("data.json", "w", encoding = "unf8"):
		log.info("create file data.json")


class BaseForm(tk.Tk):
	def __init__(self, title):
		super().__init__()

		self.btn = tk.Button(self, text = "Кнопка с изображением")

		self.title(f"PyProgTest | {title}")

		log.info("--- create base form -------------")

	def create_btn(self, text, column, row, relief = "flat", command = ""):
		log.debug(f"  | create new button ( {text} )")
		return tk.Button(self, text = text, relief = relief, command = command).grid(column = column, row = row)

	def disable_btn(self):
		self.btn.config(state = tk.DISABLED)


class LoginForm(tk.Tk):
	def __init__(self):
		super().__init__()

		self.login    = tk.Entry(self)
		self.password = tk.Entry(self, show = "*")

		self.login_btn = tk.Button(self, text = "Войти", command = self.check_login)
		self.clear_btn = tk.Button(self, text = "Очистить", command = self.clear_form)

		self.login.pack()
		self.password.pack()

		self.login_btn.pack(fill = tk.BOTH)
		self.clear_btn.pack(fill = tk.BOTH)

		log.info("--- create login form ------------")

	def check_login(self):
		log.debug("try login in system")
		log.debug(f"  | login: {self.login.get()}")
		log.debug(f"  | pass:  {self.password.get()}")

	def clear_form(self):
		self.login.delete(0, tk.END)
		self.password.delete(0, tk.END)
		self.login.focus_set()

		self.title("PyProgTest | Вход в систему")

		log.debug("clear login form")


class RegisterForm(tk.Tk):
	def __init__(self):
		super().__init__()

		self.uuid = str(uuid.uuid4())

		self.login    = tk.Entry(self)
		self.username = tk.Entry(self)
		self.email    = tk.Entry(self)
		self.password = tk.Entry(self, show = "*")

		self.register_btn = tk.Button(self, text = "Зарегистрироваться", command = self.check_register)
		self.clear_btn    = tk.Button(self, text = "Очистить", command = self.clear_form)

		self.login.pack()
		self.username.pack()
		self.email.pack()
		self.password.pack()

		self.register_btn.pack(fill = tk.BOTH)
		self.clear_btn.pack(fill = tk.BOTH)

		self.title("PyProgTest | Регистрация")

		log.info("--- create register form ---------")

	def check_register(self):
		data = {
			self.uuid: {
				"username": self.username.get(),
				"login":    self.login.get(),
				"email":    self.email.get(),
				"pass":     self.password.get(),
			}
		}

		with open("data.json", "a") as add_data_file:
			json.dump(data, add_data_file)
			log.info("success: append object in file data.json")

		log.info("success: register in system")
		log.debug(f"  | uuid: {self.uuid}")
		log.debug(f"      | name:  {self.username.get()}")
		log.debug(f"      | login: {self.login.get()}")
		log.debug(f"      | email: {self.email.get()}")
		log.debug(f"      | pass:  {self.password.get()}")

	def clear_form(self):
		self.login.delete(0, tk.END)
		self.username.delete(0, tk.END)
		self.email.delete(0, tk.END)
		self.password.delete(0, tk.END)
		self.login.focus_set()

		log.debug("clear register form")


if __name__ == "__main__":
	app = RegisterForm()

	app.geometry("600x400")

	log.info("start of mainloop")
	app.mainloop()


log.debug("")
log.info("=== end program... =======================")
log.debug("")
