def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "Помилка: ділення на нуль!"

def calculator_match():
    num1 = float(input("Перше число: "))
    op = input("Операція (+, -, *, /): ").strip()
    num2 = float(input("Друге число: "))

    match op:
        case '+': res = add(num1, num2)
        case '-': res = subtract(num1, num2)
        case '*': res = multiply(num1, num2)
        case '/': res = divide(num1, num2)
        case _: res = "Невідома операція!"

    print(f"Результат: {res}")

if __name__ == "__main__":
    calculator_match()