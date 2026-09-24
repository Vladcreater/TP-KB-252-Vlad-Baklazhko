def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "Помилка: ділення на нуль!"

def calculator_if_else():
    num1 = float(input("Перше число: "))
    op = input("Операція (+, -, *, /): ").strip()
    num2 = float(input("Друге число: "))

    if op == '+': res = add(num1, num2)
    elif op == '-': res = subtract(num1, num2)
    elif op == '*': res = multiply(num1, num2)
    elif op == '/': res = divide(num1, num2)
    else: res = "Невідома операція!"

    print(f"Результат: {res}")

if __name__ == "__main__":
    calculator_if_else()