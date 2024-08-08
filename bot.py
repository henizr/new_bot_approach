from telebot import TeleBot
from tokens import TOKEN
from telebot import types

bot = TeleBot(token=TOKEN)

BUTTONS_TITLES = ["Новая задача", "Список дел"]


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
        bot.send_message(
            message.chat.id,
            "Введи название задачи: "
        )
    elif message.text.lower() == BUTTONS_TITLES[1]:
        bot.send_message(
            message.chat.id,
            "Здесь будет твой список дел"
        )


bot.polling(non_stop=True, interval=0)