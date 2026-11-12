import functions
import operations

ACTIONS = {
    "+": operations.do_add,
    "-": operations.do_subtract,
    "*": operations.do_multiply,
    "/": operations.do_divide,
}

def main():
    print("Калькулятор")
    while True:
        op = input("\nОперація (+, -, *, /) або 'q' для виходу: ").strip()
        if op == "q":
            operations.log_action("Сеанс роботи калькулятора завершено.")
            print("Завершення роботи.")
            break
        
        if op not in ACTIONS:
            print("Помилка: невідома операція.")
            operations.log_action(f"Спроба введення невідомої операції: '{op}'")
            continue
        
        try:
            result = ACTIONS[op]()
            print("Результат:", result)
        except ZeroDivisionError as e:
            print("Помилка:", e)

if __name__ == "__main__":
    operations.log_action("Розпочато новий сеанс роботи калькулятора.")
    main()