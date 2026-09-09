# routers/admin.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.database import SessionLocal
from api.models import Teacher, Group, Room, Subject, Lesson
from api.utils.auth import is_admin


router = APIRouter(prefix="/api/admin", tags=["Admin"])

ADMIN_ID = 5028080287

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/check")
def check_admin():
    return {"allowed": True}

@router.post("/add_teacher")
async def add_teacher(
    full_name: str,
    department_id: int,
    user_id: int,
    db: Session = Depends(get_db)
):
    if not is_admin(user_id):
        raise HTTPException(status_code=403, detail="Access denied")

    teacher = Teacher(full_name=full_name, department_id=department_id)
    db.add(teacher)
    db.commit()
    db.refresh(teacher)
    return {"status": "ok", "teacher_id": teacher.id}
