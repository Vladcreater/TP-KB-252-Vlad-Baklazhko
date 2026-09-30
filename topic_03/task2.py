def test_list_functions():
    my_list = [10, 20, 30]
    print("Початковий список:", my_list)

    my_list.append(40)
    print("append(40):", my_list)

    my_list.extend([50, 60])
    print("extend([50, 60]):", my_list)

    my_list.insert(1, 15)
    print("insert(1, 15):", my_list)

    my_list.remove(30)
    print("remove(30):", my_list)

    my_list.sort()
    print("sort():", my_list)

    my_list.reverse()
    print("reverse():", my_list)

    copied_list = my_list.copy()
    print("copy():", copied_list)

    my_list.clear()
    print("clear():", my_list)

if __name__ == "__main__":
    test_list_functions()