def up_down(numbers):
    new_list = [numbers-1, numbers+1]
    return tuple(new_list)


if __name__ == "__main__":
    print(up_down(5))


# easier solution
# def up_down(x):
#     return x - 1, x + 1
#
#
# if __name__ == "__main__":
#     print(up_down(5))
