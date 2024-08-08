from telebot import TeleBot
from tokens import TOKEN
from telebot import types

bot = TeleBot(token=TOKEN)

BUTTONS_TITLES = ["новая задача", "список дел"]

todo_list: list = []

def add_new_task(message):
    bot.send_message(message.chat.id, "Введите имя новой задачи: ")

def show_todo_list(message):
    if todo_list:
        for i, task in enumerate(todo_list):
            bot.send_message(
                message.chat.id,
                f"{i}. {task.name}"
                )
        else:
            bot.send_message(
                message.chat.id,
                "Список пуст"
                )
class Task:
    def __init__(self, name, day=None, time=None) -> None:
        self.name = name
        self.day = day
        self.time = time



@bot.message_handler(commands=["newtask"])
def new_task(message):
    add_new_task(message=message)

@bot.message_handler(commands=["showlist"])
def show_list(message):
    show_todo_list(message=message)

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(
        message.chat.id,
        "Привет! Вот список доступных команд:\n"
        "/start - начало работы\n"
        "/help - список доступных команд\n"
        "/newtask - добавить новую задачу\n"
        "/showlist - посмотреть список дел"
        )

# обработчик, срабатывающий на команду start
@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    new_task_button = types.KeyboardButton(BUTTONS_TITLES[0])
    todo_list_button = types.KeyboardButton(BUTTONS_TITLES[1])
    markup.row(new_task_button, todo_list_button)

    bot.send_message(
        message.chat.id,
        "Привет, напиши, что нужно сделать?",
        reply_markup=markup
    )


# отбаботчик для текстовых сообщений
@bot.message_handler(content_types=["text"])
def answer(message):
    if message.text.lower() == BUTTONS_TITLES[0]:
        add_new_task(message=message)
    elif message.text.lower() == BUTTONS_TITLES[1]:
        show_todo_list(message=message)
    else:
        new_task = Task(name=message.text)
        todo_list.append(new_task)

        bot.send_message(
            message.chat.id,
            f"Добавлена задача\n{new_task.name}"
        )

bot.polling(non_stop=True, interval=0)