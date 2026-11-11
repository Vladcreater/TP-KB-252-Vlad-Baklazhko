import functions
import operations

ACTIONS = {
    "+": operations.do_add,
    "-": operations.do_subtract,
    "*": operations.do_multiply,
    "/": operations.do_divide,
}

def main():
    while True:
        op = input("Операція (+, -, *, /) або q для виходу: ").strip()
        if op == "q":
            break
        if op not in ACTIONS:
            print("Невідома операція.")
            continue
        try:
            print("Результат:", ACTIONS[op]())
        except ZeroDivisionError as e:
            print(e)

if __name__ == "__main__":
    main() 