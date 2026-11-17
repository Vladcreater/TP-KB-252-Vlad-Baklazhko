from operations import Add, Subtract, Multiply, Divide


class Calculator:
    def __init__(self):
        self._operations = {}
        self.history = []
        for operation in (Add(), Subtract(), Multiply(), Divide()):
            self.register(operation)

    def register(self, operation):
        self._operations[operation.symbol] = operation

    def has_operation(self, symbol):
        return symbol in self._operations

    def calculate(self, symbol, a, b):
        operation = self._operations[symbol]
        result = operation.execute(a, b)
        self.history.append(f"{a} {symbol} {b} = {result}")
        return result
