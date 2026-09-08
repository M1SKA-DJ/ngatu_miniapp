# handlers/admin.py
from aiogram import Router
from aiogram.types import Message
from keyboards.admin_menu import admin_menu

router = Router()

@router.message(commands=["admin"])
async def admin_cmd(message: Message):
    if not getattr(message, "is_admin", False):
        return await message.answer("⛔ Доступ запрещён")

    await message.answer(
        "Панель администратора НГАТУ:",
        reply_markup=admin_menu()
    )
