# def list_xor(n, list1, list2):
#
#     list_one = n in list1
#     list_two = n in list2
#
#     if list_one != list_tow:
#         return True
#
#     if list_one == list_two:
#         return False

def list_xor(n, list1, list2):
    return (n in list1) ^ (n in list2)


print(list_xor(1, [1, 2, 3], [4, 5, 6]))
print(list_xor(1, [0, 2, 3], [1, 5, 6]))
print(list_xor(1, [1, 2, 3], [1, 5, 6]))
print(list_xor(1, [0, 0, 0], [4, 5, 6]))


