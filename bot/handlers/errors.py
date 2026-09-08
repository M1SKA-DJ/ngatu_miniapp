# handlers/errors.py
from aiogram import Router
from aiogram.types import ErrorEvent

router = Router()

@router.errors()
async def errors_handler(event: ErrorEvent):
    # TODO: можно добавить логирование в файл/БД
    return event.update.message.answer("Произошла ошибка. Мы уже работаем над этим.")
