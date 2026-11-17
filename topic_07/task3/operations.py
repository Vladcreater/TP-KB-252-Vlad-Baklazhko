class Operation:
    symbol = ""
    name = ""

    def execute(self, a, b):
        raise NotImplementedError("Метод execute() має бути реалізований у класі-нащадку")

    def __str__(self):
        return f"{self.name} ({self.symbol})"


class Add(Operation):
    symbol = "+"
    name = "додавання"

    def execute(self, a, b):
        return a + b


class Subtract(Operation):
    symbol = "-"
    name = "віднімання"

    def execute(self, a, b):
        return a - b


class Multiply(Operation):
    symbol = "*"
    name = "множення"

    def execute(self, a, b):
        return a * b


class Divide(Operation):
    symbol = "/"
    name = "ділення"

    def execute(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Ділення на нуль неможливе")
        return a / b
