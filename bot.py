import telebot
import random
from telebot import types


bot = telebot.TeleBot("8008957438:AAHWmkjKzxJXbiopw_pPGnHOb0uun1PLj6Y")


advices = [
    "Не бойся начинать с нуля — это лучше, чем оставаться в минусе.",
    "Сегодня идеальный день, чтобы стать лучшим.",
    "Учись каждый день — даже 30 минут в день решают.",
    "Сделай сегодня то, за что завтра себя поблагодаришь.",
    "Пока другие спят — ты двигаешься вперёд."
]


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Я твой бот. Напиши /совет или открой /menu.")


@bot.message_handler(commands=['совет'])
def send_advice(message):
    advice = random.choice(advices)
    bot.send_message(message.chat.id, advice)


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, "/start — запуск\n/совет — случайный совет\n/help — помощь\n/menu — кнопки")

@bot.message_handler(commands=['menu'])
def menu(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("💡 Совет", callback_data="get_advice")
    btn2 = types.InlineKeyboardButton("ℹ️ Помощь", callback_data="get_help")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "Выбери действие:", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "get_advice":
        advice = random.choice(advices)
        bot.send_message(call.message.chat.id, advice)
    elif call.data == "get_help":
        bot.send_message(call.message.chat.id, "Команды:\n/start\n/совет\n/help\n/menu")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    text = message.text.lower()
    if "привет" in text:
        bot.send_message(message.chat.id, "И тебе привет 👋")
    elif "как дела" in text:
        bot.send_message(message.chat.id, "Работаю! А ты?")
    else:
        bot.send_message(message.chat.id, "Я не понял. Попробуй /совет или /menu")

# Запуск
print("Бот запущен. Нажми Ctrl+C для выхода.")
bot.polling()
