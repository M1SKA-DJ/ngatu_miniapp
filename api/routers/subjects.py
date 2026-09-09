from fastapi import APIRouter
from api.database import get_db
from api.models import Subject

router = APIRouter(prefix="/subjects", tags=["subjects"])

@router.get("/")
def get_subjects():
    db = get_db()
    return db.query(Subject).all()

@router.post("/")
def add_subject(data: dict):
    db = get_db()
    subject = Subject(name=data["name"], type=data["type"])
    db.add(subject)
    db.commit()
    return {"status": "ok"}
