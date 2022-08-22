def zap(list1, list2):
    result = []
    for a in range(len(list1)):
        for b in range(len(list2)):
            if a == b:
                result.append((list1[a], list2[b]))
    return result


print(zap([0, 1, 2, 3], [5, 6, 7, 8]))


# ugly but understandable solution
def zap(a, b):
    result = []
    for i in range(len(a)):
        item_from_a = a[i]
        item_from_b = b[i]
        tup = (item_from_a, item_from_b)
        result.append(tup)
    return result


# concise solution with list comprehensions
def zap(a, b):
    return [(a[i], b[i]) for i in range(len(a))]