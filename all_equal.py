def all_equal(new_list):
    return len(set(new_list)) == 1


print(all_equal([1, 1, 1]))


def all_equal(items):
    return all(item1 == item2 for item1 in items for item2 in items)


print(all_equal([1, 1, 1]))


# Longer solutions
def all_equal(items):
    for item1 in items:
        for item2 in items:
            if item1 != item2:
                return False
    return True
