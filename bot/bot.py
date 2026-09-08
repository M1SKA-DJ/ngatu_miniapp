# bot.py
from aiogram import Bot
from aiogram.enums import ParseMode
import os

# TODO: токен берётся из .env
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
