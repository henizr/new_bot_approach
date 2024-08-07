from telebot import TeleBot
from tokens import TOKEN

bot = TeleBot(token=TOKEN)



@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "Привет, напиши 'Новая задача' для добавления новой задачи "
        "или 'Список дел' для просмотра твоего списка"
    )




bot.polling(non_stop=True, interval=0)