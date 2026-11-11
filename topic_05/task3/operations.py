import functions

def read_number(prompt):
    while True:
        try:
            return float(input(prompt).replace(",", "."))
        except ValueError:
            print("Введіть число.")

def read_operands():
    a = read_number("Введіть перше число: ")
    b = read_number("Введіть друге число: ")
    return a, b

def do_add():
    a, b = read_operands()
    return functions.add(a, b)

def do_subtract():
    a, b = read_operands()
    return functions.subtract(a, b)

def do_multiply():
    a, b = read_operands()
    return functions.multiply(a, b)

def do_divide():
    a, b = read_operands()
    return functions.divide(a, b)