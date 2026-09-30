def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Помилка: ділення на нуль!"
    return a / b

def calculator_loop():
    while True:
        op = input("Введіть операцію (+, -, *, /) або 'q' для виходу: ").strip().lower()
        
        if op in ['q', 'exit']:
            break

        if op not in ['+', '-', '*', '/']:
            print("Невідома операція!")
            continue

        try:
            num1 = float(input("Введіть перше число: "))
            num2 = float(input("Введіть друге число: "))
        except ValueError:
            print("Помилка: некоректне число!")
            continue

        match op:
            case '+': res = add(num1, num2)
            case '-': res = subtract(num1, num2)
            case '*': res = multiply(num1, num2)
            case '/': res = divide(num1, num2)

        print(f"Результат: {res}")

if __name__ == "__main__":
    calculator_loop() 
