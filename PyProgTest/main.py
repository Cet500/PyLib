import tkinter as tk
import logging as log

log.basicConfig(
	filename = "log",
	format   = u'| %(filename)-10s | %(levelname)-8s | %(asctime)s | %(message)s',
	datefmt  = '%d.%m.%Y %H:%M:%S',
	level    = log.DEBUG
)

log.debug("")
log.debug("=== start program... =====================")
log.debug("")
log.debug("initialization")

data = open('data.txt', 'r')
print(data.read())


class BaseForm(tk.Tk):
	def __init__(self, title):
		super().__init__()

		self.btn = tk.Button(self, text = "Кнопка с изображением")

		self.title(f"PyProgTest | {title}")

		log.debug("--- create base form -------------")

	def create_btn(self, text, column, row, relief = "flat", command = ""):
		log.debug(f"  | create new button ( {text} )")
		return tk.Button(self, text = text, relief = relief, command = command).grid(column = column, row = row)

	def disable_btn(self):
		self.btn.config(state = tk.DISABLED)


class LoginForm(tk.Tk):
	def __init__(self):
		super().__init__()

		self.username = tk.Entry(self)
		self.password = tk.Entry(self, show = "*")

		self.login_btn = tk.Button(self, text = "Войти", command = self.check_login)
		self.clear_btn = tk.Button(self, text = "Очистить", command = self.clear_form)

		self.username.pack()
		self.password.pack()

		self.login_btn.pack(fill = tk.BOTH)
		self.clear_btn.pack(fill = tk.BOTH)

		log.debug("--- create login form ------------")


	def check_login(self):
		log.debug("try login in system")
		log.debug(f"  | login: {self.username.get()}")
		log.debug(f"  | pass:  {self.password.get()}")

	def clear_form(self):
		self.username.delete(0, tk.END)
		self.password.delete(0, tk.END)
		self.username.focus_set()

		self.title("PyProgTest | Вход в систему")

		log.debug("clear login form")


class RegisterForm(tk.Tk):
	def __init__(self):
		super().__init__()

		self.username = tk.Entry(self)
		self.email    = tk.Entry(self)
		self.password = tk.Entry(self, show = "*")

		self.register_btn = tk.Button(self, text = "Зарегистрироваться", command = self.check_register)
		self.clear_btn    = tk.Button(self, text = "Очистить", command = self.clear_form)

		self.username.pack()
		self.email.pack()
		self.password.pack()

		self.register_btn.pack(fill = tk.BOTH)
		self.clear_btn.pack(fill = tk.BOTH)

		self.title("PyProgTest | Регистрация")

		log.debug("--- create register form ---------")

	def check_register(self):
		log.debug("register in system")
		log.debug(f"  | login: {self.username.get()}")
		log.debug(f"  | email: {self.email.get()}")
		log.debug(f"  | pass:  {self.password.get()}")

	def clear_form(self):
		self.username.delete(0, tk.END)
		self.email.delete(0, tk.END)
		self.password.delete(0, tk.END)
		self.username.focus_set()

		log.debug("clear register form")


if __name__ == "__main__":
	app = RegisterForm()

	app.geometry("600x400")

	log.debug("start of mainloop")
	app.mainloop()


log.debug("")
log.debug("=== end program... =======================")
log.debug("")
