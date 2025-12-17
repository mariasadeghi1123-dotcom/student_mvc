from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, Student

# 👇 برای گرفتن ID از کاربر
from tkinter import simpledialog, messagebox

class StudentController:
    def __init__(self):
        self.engine = create_engine("sqlite:///students_data.db", echo=False)
        Base.metadata.create_all(self.engine)

        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    # -------- ADD --------
    def add_student(self, student_id, name, age, score1, score2):
        if self.session.get(Student, student_id):
            return False, "Student ID already exists"

        student = Student(
            student_id=student_id,
            name=name,
            age=age,
            score1=score1,
            score2=score2
        )

        self.session.add(student)
        self.session.commit()
        return True, "Student added successfully"

    # -------- DELETE (اصلاح‌شده ✅) --------
    def delete_student(self):
        student_id = simpledialog.askinteger(
            "Delete Student",
            "Enter Student ID to delete:"
        )

        if student_id is None:
            return False, "Delete cancelled"

        student = self.session.get(Student, student_id)
        if not student:
            return False, "Student not found"

        self.session.delete(student)
        self.session.commit()
        return True, f"Student with ID {student_id} deleted successfully"

    # -------- UPDATE --------
    def update_student(self, student_id, field_name, new_value):
        student = self.session.get(Student, student_id)
        if not student:
            return False, "Student not found"

        try:
            if field_name == "name":
                student.name = new_value
            elif field_name == "age":
                student.age = int(new_value)
            elif field_name == "score1":
                student.score1 = float(new_value)
            elif field_name == "score2":
                student.score2 = float(new_value)
            else:
                return False, "Invalid field"
        except:
            return False, "Invalid value type"

        self.session.commit()
        return True, "Student updated successfully"

    # -------- SHOW ALL --------
    def show_all_students(self):
        students = self.session.query(Student).all()
        data = []

        for s in students:
            data.append((
                s.student_id,
                s.name,
                s.age,
                s.score1,
                s.score2,
                round(s.average(), 2)
            ))

        return data

