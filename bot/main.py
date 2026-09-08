# main.py
import asyncio
from bot import bot
from dispatcher import dp

async def main():
    print("Запускаю бота НГАТУ...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
