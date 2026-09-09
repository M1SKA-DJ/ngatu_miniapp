from fastapi import APIRouter
from api.database import get_db
from api.models import Room

router = APIRouter(prefix="/rooms", tags=["rooms"])

@router.get("/")
def get_rooms():
    db = get_db()
    return db.query(Room).all()

@router.post("/")
def add_room(data: dict):
    db = get_db()
    room = Room(number=data["number"], building=data["building"])
    db.add(room)
    db.commit()
    return {"status": "ok"}
