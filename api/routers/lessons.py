from fastapi import APIRouter
from api.database import get_db
from api.models import Lesson

router = APIRouter(prefix="/lessons", tags=["lessons"])

@router.get("/")
def get_lessons():
    db = get_db()
    return db.query(Lesson).all()

@router.post("/")
def add_lesson(data: dict):
    db = get_db()
    lesson = Lesson(
        subject_id=data["subject_id"],
        teacher_id=data["teacher_id"],
        room_id=data["room_id"],
        group_id=data["group_id"],
        day_of_week=data["day_of_week"],
        lesson_number=data["lesson_number"],
    )
    db.add(lesson)
    db.commit()
    return {"status": "ok"}
