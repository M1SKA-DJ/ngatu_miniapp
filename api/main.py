from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import groups, teachers, rooms, subjects, lessons, replacements, admin

app = FastAPI(title="NGATU Schedule API")

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
app.include_router(subjects.router)
app.include_router(lessons.router)
app.include_router(replacements.router)
app.include_router(admin.router)

@app.get("/")
def root():
    return {"status": "ok", "message": "API is running"}
