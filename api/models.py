# models.py
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Time
from sqlalchemy.orm import relationship
from database import Base

class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    full_name = Column(String)
    department_id = Column(Integer, ForeignKey("departments.id"))
    department = relationship("Department")

class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    course = Column(Integer)
    faculty = Column(String)

class Room(Base):
    __tablename__ = "rooms"
    id = Column(Integer, primary_key=True)
    number = Column(String)
    building = Column(String)

class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    type = Column(String)  # лекция / практика / лаба

class WeekType(Base):
    __tablename__ = "week_types"
    id = Column(Integer, primary_key=True)
    name = Column(String)  # "верхняя", "нижняя"

class Lesson(Base):
    __tablename__ = "lessons"
    id = Column(Integer, primary_key=True)
    subject_id = Column(Integer, ForeignKey("subjects.id"))
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    room_id = Column(Integer, ForeignKey("rooms.id"))
    group_id = Column(Integer, ForeignKey("groups.id"))
    day_of_week = Column(Integer)  # 1–7
    week_type = Column(Integer, ForeignKey("week_types.id"))
    lesson_number = Column(Integer)  # 1–6
    start_time = Column(Time)
    end_time = Column(Time)

class Replacement(Base):
    __tablename__ = "replacements"
    id = Column(Integer, primary_key=True)
    lesson_id = Column(Integer, ForeignKey("lessons.id"))
    new_teacher_id = Column(Integer, ForeignKey("teachers.id"))
    new_room_id = Column(Integer, ForeignKey("rooms.id"))
    new_subject_id = Column(Integer, ForeignKey("subjects.id"))
    date = Column(Date)
