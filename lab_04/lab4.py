import math
import re

PRIORITY = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    'u-': 3,
    '^': 4,
}

NUMBER = r'\d+(?:\.\d+)?|\.\d+'
OPERATORS_BEFORE_UNARY = ('+', '-', '*', '/', '^', '(', 'u-')


def format_number(value: float) -> str:
    rounded = round(value, 10)
    if rounded.is_integer():
        return str(int(rounded))
    return str(rounded)


def infix_to_rpn(expression: str) -> list[str]:
    normalized = expression.replace(',', '.')
    tokens = re.findall(NUMBER + r'|[()+\-*/^]', normalized)

    if ''.join(tokens) != re.sub(r'\s+', '', normalized):
        raise ValueError("The expression contains unknown symbols")

    output: list[str] = []
    operators: list[str] = []
    previous = None

    for token in tokens:
        if re.fullmatch(NUMBER, token):
            output.append(token)

        elif token == '(':
            operators.append(token)

        elif token == ')':
            while operators and operators[-1] != '(':
                output.append(operators.pop())

            if not operators:
                raise ValueError("Incorrectly placed parentheses")

            operators.pop()

        else:
            if token == '-' and (previous is None or previous in OPERATORS_BEFORE_UNARY):
                token = 'u-'
                operators.append(token)
                previous = token
                continue

            while operators and operators[-1] != '(':
                top = operators[-1]

                if PRIORITY[top] > PRIORITY[token] or (
                    PRIORITY[top] == PRIORITY[token] and token != '^'
                ):
                    output.append(operators.pop())
                else:
                    break

            operators.append(token)

        previous = token

    while operators:
        if operators[-1] == '(':
            raise ValueError("Incorrectly placed parentheses")

        output.append(operators.pop())

    return output


def calculate_rpn(tokens: list[str]) -> float:
    stack: list[float] = []

    for token in tokens:
        if re.fullmatch(NUMBER, token):
            stack.append(float(token))

        elif token == 'u-':
            if len(stack) < 1:
                raise ValueError("Invalid mathematical expression")

            number = stack.pop()
            stack.append(-number)

        else:
            if len(stack) < 2:
                raise ValueError("Invalid mathematical expression")

            b = stack.pop()
            a = stack.pop()

            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                result = a / b
            elif token == '^':
                try:
                    result = a ** b
                except OverflowError:
                    raise ValueError("The result is too large") from None

                if isinstance(result, complex):
                    raise ValueError("Power of a negative number is undefined")

            stack.append(result)

    if len(stack) != 1:
        raise ValueError("Invalid mathematical expression")

    if math.isinf(stack[0]) or math.isnan(stack[0]):
        raise ValueError("The result is too large")

    return stack[0]


def main() -> None:
    expression = input("Enter a mathematical expression: ")

    try:
        rpn = infix_to_rpn(expression)
        result = calculate_rpn(rpn)

        print("Reverse Polish notation:", ' '.join(rpn))
        print("Calculation result:", format_number(result))

    except ZeroDivisionError:
        print("Error: division by 0!")

    except (ValueError, OverflowError) as error:
        print("Error:", error)


if __name__ == "__main__":
    main()