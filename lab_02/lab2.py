import csv
import os
from sys import argv
 
 
def load_students(filename: str) -> list[dict[str, str]]:
    """Завантажує список студентів із CSV-файлу."""
    students = []
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Файл '{filename}' не знайдено.")
    with open(filename, mode="r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if "Name" in row and "Phone" in row:
                students.append({
                    "Name": row["Name"].strip(),
                    "Phone": row["Phone"].strip()
                })
    students.sort(key=lambda s: s["Name"].lower())
    return students
 
 
def save_students(filename: str, students: list[dict[str, str]]) -> None:
    """Зберігає список студентів у CSV-файл."""
    fieldnames = ["Name", "Phone"]
    with open(filename, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for student in students:
            writer.writerow({
                "Name": student["Name"],
                "Phone": student["Phone"]
            })
 
 
def add_student(students: list[dict[str, str]], name: str, phone: str) -> list[dict[str, str]]:
    """Додає нового студента у відсортованому за ім'ям порядку."""
    name = name.strip()
    phone = phone.strip()
    if not name or not phone:
        raise ValueError("Ім'я та номер телефону не можуть бути порожніми.")
 
    for student in students:
        if student["Name"].lower() == name.lower():
            raise ValueError(f"Студент '{name}' вже існує у довіднику.")
 
    insert_index = 0
    for item in students:
        if name.lower() > item["Name"].lower():
            insert_index += 1
        else:
            break
    students.insert(insert_index, {"Name": name, "Phone": phone})
    return students
 
 
def delete_student(students: list[dict[str, str]], name: str) -> bool:
    """Видаляє студента за ім'ям. Повертає True, якщо видалено, інакше False."""
    name = name.strip()
    for i, student in enumerate(students):
        if student["Name"].lower() == name.lower():
            del students[i]
            return True
    return False
 
 
def update_student(students: list[dict[str, str]], name: str, new_phone: str) -> bool:
    """Оновлює номер телефону існуючого студента."""
    name = name.strip()
    new_phone = new_phone.strip()
    if not new_phone:
        raise ValueError("Новий номер телефону не може бути порожнім.")
    for student in students:
        if student["Name"].lower() == name.lower():
            student["Phone"] = new_phone
            return True
    return False
 
 
def find_student(students: list[dict[str, str]], query: str) -> list[dict[str, str]]:
    """Шукає студентів за частковим збігом імені або номера телефону."""
    query = query.strip().lower()
    return [
        s for s in students
        if query in s["Name"].lower() or query in s["Phone"].lower()
    ]
 
 
def print_all(students: list[dict[str, str]]) -> None:
    """Виводить усі записи телефонного довідника."""
    if not students:
        print("Довідник порожній.")
        return
    print("\n--- Телефонний довідник студентів ---")
    for idx, item in enumerate(students, start=1):
        print(f"{idx}. Ім'я: {item['Name']} | Телефон: {item['Phone']}")
    print("-------------------------------------\n")
 
 
def main() -> None:
    if len(argv) < 2:
        print("Використання: python lab2.py <шлях_до_csv_файлу>")
        return
 
    filename = argv[1]
    try:
        students = load_students(filename)
        print(f"Успішно завантажено {len(students)} записів із файлу '{filename}'.")
    except FileNotFoundError:
        print(f"Файл '{filename}' не знайдено. Буде створено новий довідник при виході.")
        students = []
 
    while True:
        choice = input(
            "Оберіть дію [C - додати, U - оновити, D - видалити, F - знайти, P - список, X - вийти та зберегти]: "
        ).strip().lower()
 
        match choice:
            case "c":
                name = input("Введіть ім'я студента: ")
                phone = input("Введіть номер телефону: ")
                try:
                    add_student(students, name, phone)
                    print("Запис успішно додано.")
                except ValueError as e:
                    print(f"Помилка: {e}")
            case "u":
                name = input("Введіть ім'я студента для оновлення: ")
                phone = input("Введіть новий номер телефону: ")
                try:
                    if update_student(students, name, phone):
                        print("Дані успішно оновлено.")
                    else:
                        print("Студента не знайдено.")
                except ValueError as e:
                    print(f"Помилка: {e}")
            case "d":
                name = input("Введіть ім'я студента для видалення: ")
                if delete_student(students, name):
                    print("Студента видалено.")
                else:
                    print("Студента не знайдено.")
            case "f":
                query = input("Введіть ім'я або телефон для пошуку: ")
                results = find_student(students, query)
                print_all(results)
            case "p":
                print_all(students)
            case "x":
                save_students(filename, students)
                print(f"Дані збережено у файл '{filename}'. Роботу завершено.")
                break
            case _:
                print("Невідома команда. Спробуйте ще раз.")
 
 
if __name__ == "__main__":
    main()