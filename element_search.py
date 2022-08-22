def find(ordered_list, element_to_find):
    for element in ordered_list:
        if element == element_to_find:
            return True
    return False


if __name__ == "__main__":
    new_list = [2, 4, 6, 8, 10]
    print(find(new_list, 5))  # prints False
    print(find(new_list, 10))  # prints True
    print(find(new_list, -1))  # prints False
    print(find(new_list, 2))  # prints True
