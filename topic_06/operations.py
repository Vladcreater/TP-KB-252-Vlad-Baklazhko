import datetime
import functions

def log_action(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}\n"
    with open("calc.log", "a", encoding="utf-8") as f:
        f.write(log_entry)

def read_number(prompt):
    while True:
        try:
            return float(input(prompt).replace(",", "."))
        except ValueError:
            print("Помилка: введіть число.")

def read_operands():
    a = read_number("Введіть перше число: ")
    b = read_number("Введіть друге число: ")
    return a, b

def do_add():
    a, b = read_operands()
    res = functions.add(a, b)
    log_action(f"Операція '+', Операнди: a={a}, b={b}, Результат: {res}")
    return res

def do_subtract():
    a, b = read_operands()
    res = functions.subtract(a, b)
    log_action(f"Операція '-', Операнди: a={a}, b={b}, Результат: {res}")
    return res

def do_multiply():
    a, b = read_operands()
    res = functions.multiply(a, b)
    log_action(f"Операція '*', Операнди: a={a}, b={b}, Результат: {res}")
    return res

def do_divide():
    a, b = read_operands()
    try:
        res = functions.divide(a, b)
        log_action(f"Операція '/', Операнди: a={a}, b={b}, Результат: {res}")
        return res
    except ZeroDivisionError as e:
        log_action(f"Помилка при виконанні '/': {e} (операнди: a={a}, b={b})")
        raise e