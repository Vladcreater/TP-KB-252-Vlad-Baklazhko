from sys import argv
from student_list import StudentList
from utils import FileManager


def main() -> None:
    if len(argv) < 2:
        print("Використання: python lab3.py <шлях_до_csv_файлу>")
        return

    file_manager = FileManager(argv[1])
    try:
        student_list = file_manager.load_students()
        print(f"Успішно завантажено {len(student_list)} записів із файлу '{file_manager.filename}'.")
    except FileNotFoundError:
        print(f"Файл '{file_manager.filename}' не знайдено. Буде створено новий довідник при виході.")
        student_list = StudentList()

    while True:
        choice = input(
            "Оберіть дію [C - додати, U - оновити, D - видалити, F - знайти, P - список, X - вийти та зберегти]: "
        ).strip().lower()

        match choice:
            case "c":
                name = input("Введіть ім'я студента: ")
                phone = input("Введіть номер телефону: ")
                try:
                    student_list.add_student(name, phone)
                    print("Запис успішно додано.")
                except ValueError as e:
                    print(f"Помилка: {e}")
            case "u":
                name = input("Введіть ім'я студента для оновлення: ")
                phone = input("Введіть новий номер телефону: ")
                try:
                    if student_list.update_student(name, phone):
                        print("Дані успішно оновлено.")
                    else:
                        print("Студента не знайдено.")
                except ValueError as e:
                    print(f"Помилка: {e}")
            case "d":
                name = input("Введіть ім'я студента для видалення: ")
                if student_list.delete_student(name):
                    print("Студента видалено.")
                else:
                    print("Студента не знайдено.")
            case "f":
                query = input("Введіть ім'я або телефон для пошуку: ")
                results = student_list.find_students(query)
                student_list.print_all(results)
            case "p":
                student_list.print_all()
            case "x":
                file_manager.save_students(student_list)
                print(f"Дані збережено у файл '{file_manager.filename}'. Роботу завершено.")
                break
            case _:
                print("Невідома команда. Спробуйте ще раз.")


if __name__ == "__main__":
    main()
