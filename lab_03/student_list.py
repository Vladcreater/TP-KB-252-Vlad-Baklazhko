from student import Student


class StudentList:
    def __init__(self, students: list[Student] | None = None) -> None:
        self._students: list[Student] = []
        if students:
            for item in students:
                if isinstance(item, Student):
                    self.add_student(item.name, item.phone)
                else:
                    raise TypeError("Елементи списку мають бути екземплярами класу Student.")

    @property
    def students(self) -> list[Student]:
        return list(self._students)

    def __len__(self) -> int:
        return len(self._students)

    def _find_index_by_name(self, name: str) -> int:
        target = name.strip().lower()
        for idx, student in enumerate(self._students):
            if student.name.lower() == target:
                return idx
        return -1

    def add_student(self, name: str, phone: str) -> Student:
        student = Student(name, phone)
        if self._find_index_by_name(student.name) != -1:
            raise ValueError(f"Студент '{student.name}' вже існує у довіднику.")

        insert_index = 0
        for item in self._students:
            if student.name.lower() > item.name.lower():
                insert_index += 1
            else:
                break

        self._students.insert(insert_index, student)
        return student

    def update_student(self, name: str, new_phone: str) -> bool:
        idx = self._find_index_by_name(name)
        if idx == -1:
            return False
        self._students[idx].update_phone(new_phone)
        return True

    def delete_student(self, name: str) -> bool:
        idx = self._find_index_by_name(name)
        if idx == -1:
            return False
        del self._students[idx]
        return True

    def find_students(self, query: str) -> list[Student]:
        q = query.strip().lower()
        if not q:
            return list(self._students)
        return [
            s for s in self._students
            if q in s.name.lower() or q in s.phone.lower()
        ]

    def print_all(self, subset: list[Student] | None = None) -> None:
        items = self._students if subset is None else subset
        if not items:
            print("Довідник порожній.")
            return
        print("\n--- Телефонний довідник студентів ---")
        for idx, student in enumerate(items, start=1):
            print(f"{idx}. {student}")
        print("-------------------------------------\n")