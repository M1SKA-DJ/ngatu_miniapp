# utils/auth.py
import os

# TODO: сюда попадёт твой ID админа из .env
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

def is_admin(user_id: int) -> bool:
    return user_id == ADMIN_ID
