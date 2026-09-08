# routers/groups.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Group
from schemas import GroupSchema

router = APIRouter(prefix="/api/groups", tags=["Groups"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[GroupSchema])
async def get_groups(db: Session = Depends(get_db)):
    return db.query(Group).all()
