from calculator import Calculator


class CalculatorApp:
    def __init__(self):
        self.calculator = Calculator()

    @staticmethod
    def read_number(prompt):
        while True:
            try:
                return float(input(prompt).replace(",", "."))
            except ValueError:
                print("Введіть число.")

    def run(self):
        while True:
            symbol = input("Операція (+, -, *, /), h - історія, q - вихід: ").strip()
            if symbol == "q":
                break
            if symbol == "h":
                print("\n".join(self.calculator.history) or "Історія порожня.")
                continue
            if not self.calculator.has_operation(symbol):
                print("Невідома операція.")
                continue
            a = self.read_number("Введіть перше число: ")
            b = self.read_number("Введіть друге число: ")
            try:
                print("Результат:", self.calculator.calculate(symbol, a, b))
            except ZeroDivisionError as e:
                print(e)


if __name__ == "__main__":
    CalculatorApp().run()
