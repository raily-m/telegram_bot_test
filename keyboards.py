from aiogram import types

BTN_FEED = "🥐Покормить"
BTN_PLAY = "😁Поиграть"
BTN_SLEEP = "😴Спать"
BTN_STATUS = "✨Статус"
BTN_EXIT = "❌Выход"


main_kb = types.ReplyKeyboardMarkup(
keyboard = [
    [types.KeyboardButton(text= BTN_FEED ), types.KeyboardButton(text= BTN_PLAY)],
    [types.KeyboardButton(text= BTN_SLEEP), types.KeyboardButton(text= BTN_STATUS)],
    [types.KeyboardButton(text= BTN_EXIT)]
],

resize_keyboard = True


)


remove_kb = types.ReplyKeyboardRemove()