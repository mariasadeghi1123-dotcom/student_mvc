from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True)   # ID دستی
    name = Column(String(100))
    age = Column(Integer)
    score1 = Column(Float)
    score2 = Column(Float)

    def __init__(self, student_id, name, age, score1, score2):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.score1 = score1
        self.score2 = score2

    def average(self):
        return (self.score1 + self.score2) / 2

    def __str__(self):
        return f"Name = {self.name}, Age = {self.age}, Score1={self.score1}, Score2={self.score2}"


