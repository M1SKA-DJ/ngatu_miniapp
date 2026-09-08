# keyboards/admin_menu.py
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def admin_menu():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Добавить преподавателя")],
            [KeyboardButton(text="Добавить аудиторию")],
            [KeyboardButton(text="Добавить предмет")],
            [KeyboardButton(text="Добавить пару")],
            [KeyboardButton(text="Добавить замену")],
        ],
        resize_keyboard=True
    )
