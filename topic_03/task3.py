def test_dict_functions():
    student = {
        "name": "Влад",
        "group": "КБ-252",
        "course": 2
    }
    print("Початковий словник:", student)

    print("keys():", list(student.keys()))
    print("values():", list(student.values()))
    print("items():", list(student.items()))

    student.update({"course": 3, "city": "Чернігів"})
    print("update():", student)

    del student["city"]
    print("del student['city']:", student)

    student.clear()
    print("clear():", student)

if __name__ == "__main__":
    test_dict_functions()