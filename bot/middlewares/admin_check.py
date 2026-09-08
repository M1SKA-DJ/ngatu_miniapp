# middlewares/admin_check.py
from aiogram import BaseMiddleware
from aiogram.types import Message
import os

# TODO: ADMIN_ID берётся из .env
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

class AdminCheckMiddleware(BaseMiddleware):
    async def __call__(self, handler, event: Message, data):
        # добавляем флаг is_admin в объект message
        event.is_admin = (event.from_user.id == ADMIN_ID)
        return await handler(event, data)
