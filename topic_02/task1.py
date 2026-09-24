def calculate_discriminant(a, b, c):
    return b**2 - 4 * a * c

def find_roots(a, b, c):
    if a == 0:
        return "Це не квадратне рівняння (a ≠ 0)."
    
    d = calculate_discriminant(a, b, c)
    print(f"Дискримінант D = {d}")
    
    if d > 0:
        x1 = (-b + d**0.5) / (2 * a)
        x2 = (-b - d**0.5) / (2 * a)
        return f"Два корені: x1 = {x1}, x2 = {x2}"
    elif d == 0:
        x = -b / (2 * a)
        return f"Один корінь: x = {x}"
    else:
        return "Рівняння не має дійсних коренів (D < 0)."

if __name__ == "__main__":
    a = float(input("Введіть a: "))
    b = float(input("Введіть b: "))
    c = float(input("Введіть c: "))
    print(find_roots(a, b, c))