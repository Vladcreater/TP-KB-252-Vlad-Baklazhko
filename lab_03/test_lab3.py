import pytest
from student import Student
from student_list import StudentList
from utils import FileManager


def test_student_creation_and_update():
    st = Student("  Баклажко Владислав ", " +380931112233 ")
    assert st.name == "Баклажко Владислав"
    assert st.phone == "+380931112233"

    st.update_phone("+380991234567")
    assert st.phone == "+380991234567"

    with pytest.raises(ValueError):
        Student("", "+380931112233")
    with pytest.raises(ValueError):
        st.update_phone("   ")


def test_student_list_sorted_add():
    group = StudentList()
    group.add_student("Шевченко Марія", "+380503334455")
    group.add_student("Баклажко Владислав", "+380931112233")
    group.add_student("Коваленко Олександр", "+380672223344")

    assert len(group) == 3
    assert all(isinstance(s, Student) for s in group.students)
    assert [s.name for s in group.students] == [
        "Баклажко Владислав",
        "Коваленко Олександр",
        "Шевченко Марія",
    ]


def test_student_list_duplicate_raises():
    group = StudentList()
    group.add_student("Баклажко Владислав", "+380931112233")
    with pytest.raises(ValueError):
        group.add_student("баклажко владислав", "+380990001122")


def test_student_list_update_and_delete():
    group = StudentList()
    group.add_student("Баклажко Владислав", "+380931112233")
    group.add_student("Коваленко Олександр", "+380672223344")

    assert group.update_student("Баклажко Владислав", "+380930000000") is True
    assert group.find_students("Баклажко")[0].phone == "+380930000000"
    assert group.update_student("Неіснуючий", "+380930000000") is False

    assert group.delete_student("Коваленко Олександр") is True
    assert len(group) == 1
    assert group.delete_student("Коваленко Олександр") is False


def test_student_list_find():
    group = StudentList()
    group.add_student("Баклажко Владислав", "+380931112233")
    group.add_student("Мельник Софія", "+380975556677")

    by_name = group.find_students("софія")
    assert len(by_name) == 1
    assert by_name[0].name == "Мельник Софія"

    by_phone = group.find_students("1112233")
    assert len(by_phone) == 1
    assert by_phone[0].name == "Баклажко Владислав"


def test_file_manager_save_and_load(tmp_path):
    csv_file = tmp_path / "students.csv"
    fm = FileManager(str(csv_file))

    original = StudentList()
    original.add_student("Шевченко Марія", "+380503334455")
    original.add_student("Баклажко Владислав", "+380931112233")
    fm.save_students(original)

    loaded = fm.load_students()
    assert len(loaded) == 2
    assert loaded.students[0].name == "Баклажко Владислав"
    assert loaded.students[1].name == "Шевченко Марія"


def test_file_manager_missing_file():
    fm = FileManager("missing_students_file_xyz.csv")
    with pytest.raises(FileNotFoundError):
        fm.load_students()