from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

from config import configs

WEBAPP = WebAppInfo(url = configs.WEB_APP_URL)

def main_menu_buttons():
    kbd = ReplyKeyboardMarkup(resize_keyboard = True, keyboard = [
            [
                KeyboardButton(text = "Приложение", web_app = WEBAPP),
            ],
        ]
    )
    return kbd