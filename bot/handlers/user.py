# handlers/user.py
from aiogram import Router
from aiogram.types import Message
from keyboards.inline import miniapp_button

router = Router()

@router.message(lambda m: m.text == "📅 Расписание")
async def open_schedule(message: Message):
    await message.answer(
        "Открыть мини‑приложение расписания НГАТУ:",
        reply_markup=miniapp_button()
    )

@router.message(lambda m: m.text == "⚙️ Настройки")
async def settings(message: Message):
    await message.answer("Настройки пока в разработке.")
