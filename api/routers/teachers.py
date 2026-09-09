from fastapi import APIRouter
from api.database import get_db
from api.models import Teacher

router = APIRouter(prefix="/teachers", tags=["teachers"])

@router.get("/")
def get_teachers():
    db = get_db()
    return db.query(Teacher).all()

@router.post("/")
def add_teacher(data: dict):
    db = get_db()
    teacher = Teacher(full_name=data["full_name"], department=data["department"])
    db.add(teacher)
    db.commit()
    return {"status": "ok"}
