from fastapi import APIRouter
from api.database import get_db
from api.models import Lesson

router = APIRouter(prefix="/replacements", tags=["replacements"])

@router.get("/")
def get_replacements():
    db = get_db()
    # временно возвращаем пустой список, пока не реализована логика замен
    return []
