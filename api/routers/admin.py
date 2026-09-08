# routers/admin.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Teacher
from utils.auth import is_admin

router = APIRouter(prefix="/api/admin", tags=["Admin"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

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
