from fastapi import APIRouter
from api.models import Group
from api.database import get_db


router = APIRouter(prefix="/groups", tags=["groups"])

@router.get("/")
def get_groups():
    db = get_db()
    groups = db.query(Group).all()
    return groups
