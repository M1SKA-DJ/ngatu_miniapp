# handlers/start.py
from aiogram import Router
from aiogram.types import Message
from keyboards.main_menu import main_menu

router = Router()

@router.message(commands=["start"])
async def start_cmd(message: Message):
    await message.answer(
        "Добро пожаловать в расписание НГАТУ!",
        reply_markup=main_menu()
    )
