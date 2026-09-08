# keyboards/inline.py
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

# TODO: сюда нужно вставить URL мини‑приложения (хост фронтенда)
MINIAPP_URL = os.getenv("MINIAPP_URL", "https://your-miniapp-url")

def miniapp_button():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="Открыть мини‑приложение",
                    web_app={"url": MINIAPP_URL}
                )
            ]
        ]
    )
