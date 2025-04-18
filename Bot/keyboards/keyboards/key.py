from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from Bot.texts.ru_texts import Texts_Russian



keyboard_go_menu_callback = ReplyKeyboardMarkup(
    keyboard= [
        [KeyboardButton(text=Texts_Russian.menu_keyboard_key)],
        [KeyboardButton(text=Texts_Russian.menu_keyboard_personal_account),
         KeyboardButton(text=Texts_Russian.menu_keyboard_buy)],
        [KeyboardButton(text=Texts_Russian.menu_keyboard_change_location),
         KeyboardButton(text=Texts_Russian.menu_keyboard_info)],
        [KeyboardButton(text=Texts_Russian.keyboard_start_text)],
        [KeyboardButton(text=Texts_Russian.menu_keyboard_support),
         KeyboardButton(text=Texts_Russian.menu_keyboard_about)]
    ], resize_keyboard=True, one_time_keyboard=False
)