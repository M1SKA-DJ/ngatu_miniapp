# dispatcher.py
from aiogram import Dispatcher
from handlers import start, admin, user, errors
from middlewares.admin_check import AdminCheckMiddleware

dp = Dispatcher()

# Middleware для пометки is_admin
dp.message.middleware(AdminCheckMiddleware())

# Регистрация роутеров
dp.include_router(start.router)
dp.include_router(user.router)
dp.include_router(admin.router)
dp.include_router(errors.router)
