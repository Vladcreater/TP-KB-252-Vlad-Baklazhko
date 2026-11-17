class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Точка({self.x}, {self.y})"

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.x ** 2 + self.y ** 2 < other.x ** 2 + other.y ** 2

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __len__(self):
        return 2


a = Point(1, 2)
b = Point(3, 4)

print("__str__:", a)
print("__repr__:", repr(a), [a, b])
print("__eq__:", a == Point(1, 2), a == b)
print("__lt__:", a < b)
print("__add__:", a + b)
print("__len__:", len(a))
