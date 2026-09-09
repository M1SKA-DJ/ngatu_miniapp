from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routers import (
    groups,
    teachers,
    rooms,
    lessons,
    subjects,
    replacements,
    admin
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(groups.router)
app.include_router(teachers.router)
app.include_router(rooms.router)
app.include_router(lessons.router)
app.include_router(subjects.router)
app.include_router(replacements.router)
app.include_router(admin.router)

@app.get("/")
def root():
    return {"status": "ok"}
