# init_db.py
from database import Base, engine
import models  # важно импортировать, чтобы таблицы зарегистрировались

print("Создаю таблицы НГАТУ...")
Base.metadata.create_all(bind=engine)
print("Готово! База данных ngatu.db создана.")
