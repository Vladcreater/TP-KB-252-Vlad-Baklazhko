def check_string_methods(line):
    print("Вихідний рядок:", line)
    print("Метод strip():", line.strip())
    print("Метод capitalize():", line.capitalize())
    print("Метод title():", line.title())
    print("Метод upper():", line.upper())
    print("Метод lower():", line.lower())

user_string = input("Введіть рядок для перевірки: ")
check_string_methods(user_string)
