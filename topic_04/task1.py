def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    """Ділення з обробкою виняткової ситуації ділення на нуль."""
    try:
        return a / b
    except ZeroDivisionError:
        print("Помилка: ділення на нуль неможливе.")
        return None

OPERATIONS = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def ask_number(prompt):
    """Запитує число в користувача, поки не буде введено коректне значення."""
    while True:
        try:
            return float(input(prompt).replace(",", "."))
        except ValueError:
            print("Помилка: введіть число (наприклад, 5 або 3.14).")
        except (EOFError, KeyboardInterrupt):
            raise  


def ask_operation(prompt):
    """Запитує операцію в користувача, поки не буде введено допустимий знак."""
    while True:
        try:
            op = input(prompt).strip()
            if op.lower() == "q":
                return None
            if op not in OPERATIONS:
                raise KeyError(op)
            return op
        except KeyError:
            print("Помилка: невідома операція. Допустимі: +, -, *, / (або q для виходу).")


def main():
    print("Калькулятор. Для виходу введіть q замість операції.")
    try:
        while True:  
            op = ask_operation("Операція (+, -, *, /) або q: ")
            if op is None:
                break
            a = ask_number("Перше число: ")
            b = ask_number("Друге число: ")

            try:
                result = OPERATIONS[op](a, b)
            except OverflowError:
                print("Помилка: результат завеликий для обчислення.")
                continue

            if result is not None:
                print(f"Результат: {a} {op} {b} = {result}")
    except (EOFError, KeyboardInterrupt):
        print("\nВведення перервано користувачем.")
    finally:
        print("Роботу завершено.")


if __name__ == "__main__":
    main()
