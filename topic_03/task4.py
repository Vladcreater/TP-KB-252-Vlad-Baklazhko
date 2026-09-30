def find_insert_position(sorted_list, val):
    for index, element in enumerate(sorted_list):
        if element >= val:
            return index
    return len(sorted_list)

def insert_into_sorted_list(sorted_list, val):
    pos = find_insert_position(sorted_list, val)
    sorted_list.insert(pos, val)
    return pos

if __name__ == "__main__":
    numbers = [10, 20, 30, 40, 50]
    print("Початковий список:", numbers)

    try:
        new_val = float(input("Введіть число: "))
        pos = insert_into_sorted_list(numbers, new_val)
        print(f"Позиція для вставки: {pos}")
        print("Оновлений список:", numbers)
    except ValueError:
        print("Помилка при введенні числа!")