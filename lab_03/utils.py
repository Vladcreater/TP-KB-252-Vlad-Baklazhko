import csv
import os
from student import Student
from student_list import StudentList


class FileManager:
    """Клас для завантаження та збереження списку студентів у форматі CSV."""

    def __init__(self, filename: str) -> None:
        self.filename = filename

    def load_students(self) -> StudentList:
        """Зчитує початкові дані з CSV-файлу та формує об'єкт StudentList."""
        if not os.path.exists(self.filename):
            raise FileNotFoundError(f"Файл '{self.filename}' не знайдено.")

        student_list = StudentList()
        with open(self.filename, mode="r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if "Name" in row and "Phone" in row:
                    name = (row["Name"] or "").strip()
                    phone = (row["Phone"] or "").strip()
                    if name and phone:
                        student_list.add_student(name, phone)
        return student_list

    def save_students(self, student_list: StudentList) -> None:
        """Зберігає об'єкти Student із StudentList у CSV-файл."""
        fieldnames = ["Name", "Phone"]
        with open(self.filename, mode="w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for student in student_list.students:
                writer.writerow(student.to_dict())
