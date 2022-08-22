def flatten(list1):
    new_list = []
    for i in list1:
        for list1 in i:
            new_list.append(list1)
    print(new_list)


def flatten1(list1):
    new_list = [i for sublist in list1 for i in sublist]
    print(new_list)


flatten([[1, 2, 3, 4], [3, 4]])
flatten1([[3, 4, 5], [6, 7, 8]])

