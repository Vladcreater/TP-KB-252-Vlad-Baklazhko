class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Ім'я: {self.name:<10} | Вік: {self.age}"


students = [
    Student("Владислав", 19),
    Student("Олександр", 21),
    Student("Марія", 18),
    Student("Анна", 20),
    Student("Дмитро", 19),
]

print("Сортування за віком:")
for student in sorted(students, key=lambda s: s.age):
    print(student)

print("\nСортування за ім'ям:")
for student in sorted(students, key=lambda s: s.name):
    print(student)
