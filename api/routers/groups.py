from fastapi import APIRouter
from database import get_db
from models import Group

router = APIRouter(prefix="/groups", tags=["groups"])

@router.get("/")
def get_groups():
    db = get_db()
    groups = db.query(Group).all()
    return groups
