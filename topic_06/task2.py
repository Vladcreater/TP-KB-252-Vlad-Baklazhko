def main():
    students = [
        {"name": "Владислав", "grade": 90},
        {"name": "Олександр", "grade": 85},
        {"name": "Марія", "grade": 98},
        {"name": "Анна", "grade": 75},
        {"name": "Дмитро", "grade": 92}
    ]

    print("Початковий список студентів:")
    for student in students:
        print(f"Ім'я: {student['name']:<10} | Оцінка: {student['grade']}")

    sorted_by_name = sorted(students, key=lambda x: x["name"])
    print("\nСортування за ім'ям (абетковий порядок):")
    for student in sorted_by_name:
        print(f"Ім'я: {student['name']:<10} | Оцінка: {student['grade']}")

    sorted_by_grade = sorted(students, key=lambda x: x["grade"])
    print("\nСортування за оцінкою (зростання):")
    for student in sorted_by_grade:
        print(f"Ім'я: {student['name']:<10} | Оцінка: {student['grade']}")

    sorted_by_grade_desc = sorted(students, key=lambda x: x["grade"], reverse=True)
    print("\nСортування за оцінкою (спадання):")
    for student in sorted_by_grade_desc:
        print(f"Ім'я: {student['name']:<10} | Оцінка: {student['grade']}")

if __name__ == "__main__":
    main()