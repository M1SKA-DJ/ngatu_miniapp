# schemas.py
from pydantic import BaseModel
from datetime import time, date

class DepartmentSchema(BaseModel):
    id: int
    name: str
    class Config: orm_mode = True

class TeacherSchema(BaseModel):
    id: int
    full_name: str
    department_id: int
    class Config: orm_mode = True

class GroupSchema(BaseModel):
    id: int
    name: str
    course: int | None = None
    faculty: str | None = None
    class Config: orm_mode = True

class RoomSchema(BaseModel):
    id: int
    number: str
    building: str
    class Config: orm_mode = True

class SubjectSchema(BaseModel):
    id: int
    name: str
    type: str
    class Config: orm_mode = True

class WeekTypeSchema(BaseModel):
    id: int
    name: str
    class Config: orm_mode = True

class LessonSchema(BaseModel):
    id: int
    subject_id: int
    teacher_id: int
    room_id: int
    group_id: int
    day_of_week: int
    week_type: int
    lesson_number: int
    start_time: time
    end_time: time
    class Config: orm_mode = True

class ReplacementSchema(BaseModel):
    id: int
    lesson_id: int
    new_teacher_id: int
    new_room_id: int
    new_subject_id: int
    date: date
    class Config: orm_mode = True
