import pytest
from lab2 import (
    load_students,
    save_students,
    add_student,
    delete_student,
    update_student,
    find_student,
)


def test_add_student_sorted():
    students = []
    add_student(students, "Шевченко Марія", "+380503334455")
    add_student(students, "Баклажко Владислав", "+380931112233")
    add_student(students, "Коваленко Олександр", "+380672223344")

    assert len(students) == 3
    assert students[0]["Name"] == "Баклажко Владислав"
    assert students[1]["Name"] == "Коваленко Олександр"
    assert students[2]["Name"] == "Шевченко Марія"


def test_add_student_duplicate_raises():
    students = [{"Name": "Баклажко Владислав", "Phone": "+380931112233"}]
    with pytest.raises(ValueError):
        add_student(students, "баклажко владислав", "+380999999999")


def test_add_student_empty_raises():
    students = []
    with pytest.raises(ValueError):
        add_student(students, "", "+380931112233")
    with pytest.raises(ValueError):
        add_student(students, "Іван", "   ")


def test_delete_student():
    students = [
        {"Name": "Баклажко Владислав", "Phone": "+380931112233"},
        {"Name": "Коваленко Олександр", "Phone": "+380672223344"},
    ]
    assert delete_student(students, "Коваленко Олександр") is True
    assert len(students) == 1
    assert delete_student(students, "Неіснуючий Студент") is False


def test_update_student():
    students = [{"Name": "Баклажко Владислав", "Phone": "+380931112233"}]
    assert update_student(students, "Баклажко Владислав", "+380930000000") is True
    assert students[0]["Phone"] == "+380930000000"
    assert update_student(students, "Невідомий", "+380930000000") is False


def test_find_student():
    students = [
        {"Name": "Баклажко Владислав", "Phone": "+380931112233"},
        {"Name": "Коваленко Олександр", "Phone": "+380672223344"},
    ]
    res_name = find_student(students, "влад")
    assert len(res_name) == 1
    assert res_name[0]["Name"] == "Баклажко Владислав"

    res_phone = find_student(students, "2223344")
    assert len(res_phone) == 1
    assert res_phone[0]["Name"] == "Коваленко Олександр"


def test_save_and_load_students(tmp_path):
    file_path = tmp_path / "test_students.csv"
    initial_data = [
        {"Name": "Баклажко Владислав", "Phone": "+380931112233"},
        {"Name": "Шевченко Марія", "Phone": "+380503334455"},
    ]
    save_students(str(file_path), initial_data)
    loaded_data = load_students(str(file_path))

    assert loaded_data == initial_data


def test_load_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        load_students("non_existent_file_12345.csv")
